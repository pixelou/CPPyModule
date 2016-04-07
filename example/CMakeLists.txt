cmake_minimum_required(VERSION 3.0)
project(GeneralizedDistanceTransform)


# Dependencies ----------------------------------------------------------------

find_package(OpenCV REQUIRED)
include(cmake/CPPyModule.cmake)


# Import or compile external project ------------------------------------------

add_library(flipping SHARED
    some_project/flipping.cpp)
target_include_directories(flipping PUBLIC
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/some_project>
    $<INSTALL_INTERFACE:include/some_project>
    ${OpenCV_INCLUDE_DIRS})
target_link_libraries(flipping
    ${OpenCV_LIBS})
#set_property(TARGET flipping
#    PROPERTY INTERFACE_POSITION_INDEPENDENT_CODE ON)


# Python module binding -------------------------------------------------------

as_python_module(pyflipping_module
    # root wrapping namespace in the c++ wrappers
    NAMESPACE flipping
    # name of the python module
    MODULE_NAME pyflipping
    # headers to parse for exported symbols
    HEADERS flipping_wrapper.h
    # source files of wrapping functions
    SOURCES flipping_wrapper.cpp
    )
target_link_libraries(pyflipping_module flipping)


# Install ---------------------------------------------------------------------

install(TARGETS flipping
    EXPORT flipping_tgt
    RUNTIME DESTINATION lib
    LIBRARY DESTINATION lib
    PUBLIC_HEADER DESTINATION include/flipping)
install(EXPORT flipping_tgt 
    FILE flipping.cmake
    DESTINATION lib/cmake/flipping)

install_module(pyflipping_module)
