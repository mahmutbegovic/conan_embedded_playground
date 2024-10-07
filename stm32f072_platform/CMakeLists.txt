# Top-level CMakeLists.txt
cmake_minimum_required(VERSION 3.13)
set(CMAKE_TRY_COMPILE_TARGET_TYPE STATIC_LIBRARY)

project(stm32f072_platform VERSION 1.0.6)

enable_language(C CXX ASM)

set(CMAKE_CXX_STANDARD 23)

add_subdirectory(util)
add_subdirectory(hal)
add_subdirectory(cstdlib_support)

# add_library(stm32f072_platform STATIC)

# target_link_libraries(stm32f072_platform PUBLIC hal_stm32f072 util cstdlib_support)

# install(TARGETS stm32f072_platform hal_stm32f072 util cstdlib_support)
