# platform/CMakeLists.txt
cmake_minimum_required(VERSION 3.13)
project(cstdlib_support)

# Create the platform library
add_library(${PROJECT_NAME} STATIC)

target_sources(${PROJECT_NAME} PRIVATE
  retarget.cpp
)

target_sources(${PROJECT_NAME} PUBLIC
  nosys_stubs.c
)

# Include directories
target_include_directories(${PROJECT_NAME} PUBLIC
  ${CMAKE_CURRENT_SOURCE_DIR}
)

install(DIRECTORY 
          ./
        DESTINATION include
        FILES_MATCHING PATTERN "*.h" PATTERN "*.hpp")

install(TARGETS cstdlib_support)
