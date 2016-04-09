==========
CPPyModule
==========

This repository contains tools to automatically generate python modules out of
C++ source files for OpenCV based projects. Most of the credit should go to 
the OpenCV project from which the conversion tools were taken.


Use cases
=========

Your project uses the python bindings of OpenCV, but you need to use an 
external library in C++. You can write an parser-frendly wrapper for this 
library and have the python binding automatically generated.

Your project is written in C++ and you which to distribute an python binding.

Your project is written in python but you need to use optimzed C++ code. This
code will be compiled into a python module which you can load back into your
project.

WIP: You wish to compile one module from OpenCV source tree (to test an update
from the source tree for example) and generate the python bindings without 
messing up your OpenCV installation.


Documentation
=============

Python extensions
-----------------

Python can load compiled libraries that are completely written in C++. The 
interpreter simply runs a sort of main() function that declares functions, 
modules, classes... using python's C API.

However, The python C API is rather low level which makes the process of 
declaring the exported features rather tedious and complicated. The Boost 
library provides tools to facilitate this task for C++, but it is still up to 
the binding developper to specify the functions, their inputs and arguments, 
the classes, the modules.... 

The OpenCV project uses bindings generator that can convert simple C++ 
features, using extra annotations to disabiguate the interpretation.


Annotations
-----------

Refer to [the OpenCV documentation](http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_bindings/py_bindings_basics/py_bindings_basics.html) for a complete specification of
the annotations.


CMake based project
-------------------

TODO


setuptools based project
------------------------

TODO


Examples
========

[Examples](examples/)
