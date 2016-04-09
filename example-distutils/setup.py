import subprocess
from setuptools import setup
from cppymodule import generate_extension
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

flipping_extension = generate_extension(
    root_ns='flipping', module_name='flipping', 
    headers=['flipping_wrapper.h'],
    sources=['flipping_wrapper.cpp', 'some_project/flipping.cpp'],
    depends=['flipping_wrapper.h', 'some_project/flipping.h'],
    extra_compile_args=[
        subprocess.check_output(
            ["pkg-config", "--cflags", "opencv"]).decode("utf-8"),
        subprocess.check_output(
            ["pkg-config", "--libs", "opencv"]).decode("utf-8")])

setup(
    name='flipping',
    version='0.0.1-dev1',
    description='Python version of the flipping library',
    long_description=long_description,
    author='Foo Barr',
    author_email='foo.barr@barrinc.com',
    license='BSD',
    keywords='CV',
    packages=['cppymodule'],
    ext_modules = [flipping_extension],
    install_requires=['cv2'])
