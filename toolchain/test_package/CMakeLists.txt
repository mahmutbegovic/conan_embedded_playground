cmake_minimum_required(VERSION 3.15)
project(test_package LANGUAGES CXX)

add_executable(${PROJECT_NAME} test_package.cpp)

target_link_options(
  ${PROJECT_NAME}
  PUBLIC
  -specs=nosys.specs
  -specs=nano.specs
)