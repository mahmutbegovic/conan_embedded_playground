cmake_minimum_required(VERSION 3.25)
# supress creating executable in config phase
set(CMAKE_TRY_COMPILE_TARGET_TYPE STATIC_LIBRARY)

project(embedded_ba_demo VERSION 1.0.0)

set(EXECUTABLE ${PROJECT_NAME}.elf)

add_executable(
  ${EXECUTABLE}
  app/src/main.cpp
)

find_package(stm32f072_platform CONFIG REQUIRED)
target_link_libraries(${EXECUTABLE} stm32f072_platform::stm32f072_platform)

include(macros.cmake)
print_size(${EXECUTABLE})
hush_linker_nosys_warnings(${EXECUTABLE})

include(renode_macros)
add_run_in_renode_target(
                "${CMAKE_SOURCE_DIR}/renode_scripts/stm32f072.resc" 
                "${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}.elf"
              )