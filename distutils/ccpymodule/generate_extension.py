import os
import re
import tempfile

from . gen2 import PythonWrapperGenerator
from distutils.core import Extension


def generate_extension(root_ns, headers, module_name, sources, **kwargs):
    # here = os.path.abspath(os.path.dirname(__file__))
    gen_path = os.path.join("cppymodule", "_src_" + module_name)
    if not os.path.isdir(gen_path):
        os.mkdir(gen_path)
        generator = PythonWrapperGenerator(root_ns=root_ns, 
                                           module_name=module_name)
        generator.gen(sources, gen_path)
        
        init_tplt = os.path.join("cppymodule", "src", "init_func.cpp.in")
        with open(init_tplt) as model:
            with open(os.path.join(gen_path, "init_func.cpp"), "w") as output:
                output.write(
                    re.sub(r"@ARG_MODULE_NAME@", module_name, model.read()))
        
        with open('MANIFEST.in', 'a') as manifest:
            if 'depends' not in kwargs:
                kwargs['depends'] = list()
            kwargs['depends'].extend([
                os.path.join(gen_path, "pyopencv_generated_funcs.h"),
                os.path.join(gen_path, "pyopencv_generated_ns_reg.h"),
                os.path.join(gen_path, "pyopencv_generated_type_reg.h"),
                os.path.join(gen_path, "pyopencv_generated_types.h"),
                os.path.join(gen_path, "pyopencv_generated_include.h"),
                os.path.join("cppymodule", "src", "module.hpp"),
                os.path.join("cppymodule", "src", "pycompat.hpp"),
                os.path.join("cppymodule", "src", "py_cv_converters.hpp"),
                os.path.join("cppymodule", "src", "utils.hpp")])
            for d in kwargs['depends']:
                manifest.write('include '+ d +'\n')
        
    sources.append(os.path.join(gen_path, "init_func.cpp"))
    if 'include_dirs' not in kwargs:
        kwargs['include_dirs'] = list()
    kwargs['include_dirs'].extend([os.path.join("cppymodule", "src"), 
                                   gen_path])
                
    return Extension(module_name, sources=sources, **kwargs)
