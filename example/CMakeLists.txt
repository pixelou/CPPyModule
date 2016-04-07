cmake_minimum_required(VERSION 3.0)
project(GeneralizedDistanceTransform)


# Settings --------------------------------------------------------------------

set(PYTHON_VERSION "" CACHE STRING "Desired python version for the bindings")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -g -Wl,--no-undefined -O0 -Wall")
list(APPEND CMAKE_MODULE_PATH ${CMAKE_CURRENT_SOURCE_DIR}/cmake)


# Dependencies ----------------------------------------------------------------

find_package(OpenCV REQUIRED)
include(cmake/OpenCVPythonModule.cmake)


# Import or compile external project ------------------------------------------

add_library(flipping SHARED
    some_project/flipping.cpp)
target_include_directories(flipping PUBLIC
  ${OpenCV_INCLUDE_DIRS})
target_link_libraries(flipping
    ${OpenCV_LIBS})
set_property(TARGET flipping
    PROPERTY INTERFACE_POSITION_INDEPENDENT_CODE ON)


# Python module binding -------------------------------------------------------

as_python_module(pyflipping_module
    NAMESPACE flipping
    # This is the name of the python module and of the wrapping namespace in 
    # the c++ wrappers.
    MODULE_NAME pyflipping
    # Specify headers to parse for exported symbols
    HEADERS flipping_wrapper.h
    # Specify source files of wrapping functions
    SOURCES flipping_wrapper.cpp
    )
target_link_libraries(pyflipping_module flipping)


# Install ---------------------------------------------------------------------

# TODO


# Testing ---------------------------------------------------------------------
    
# TODO

