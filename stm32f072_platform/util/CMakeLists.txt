# platform/CMakeLists.txt
cmake_minimum_required(VERSION 3.13)
project(util)

# Create the platform library
add_library(${PROJECT_NAME} STATIC)

target_sources(${PROJECT_NAME} PRIVATE
  src/units.cpp
)

# Include directories
target_include_directories(${PROJECT_NAME} PUBLIC
  ${CMAKE_CURRENT_SOURCE_DIR}/inc
)