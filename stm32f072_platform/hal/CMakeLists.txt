# platform/CMakeLists.txt
cmake_minimum_required(VERSION 3.13)
project(hal_stm32f072)

# Create the hal library
add_library(${PROJECT_NAME} STATIC)

target_sources(${PROJECT_NAME} PRIVATE
  uart/src/uart_stm32.cpp
  gpio/src/gpio.cpp
  gpio/src/gpio_interrupt_manager.cpp
  adc/src/adc_stm32.cpp
)

# Include directories
target_include_directories(${PROJECT_NAME} PUBLIC
  ${CMAKE_CURRENT_SOURCE_DIR}/uart/inc
  ${CMAKE_CURRENT_SOURCE_DIR}/inc
  ${CMAKE_CURRENT_SOURCE_DIR}/gpio/inc
  ${CMAKE_CURRENT_SOURCE_DIR}/adc/inc
)

# Compile definitions
target_compile_definitions(${PROJECT_NAME} PUBLIC USE_HAL_DRIVER STM32F072xB)

# Include the platform library
add_subdirectory(
    "${CMAKE_SOURCE_DIR}/platform"   # Source directory
    "${CMAKE_BINARY_DIR}/platform"   # Binary directory
)

if(NOT TARGET util)
    # Include util
    add_subdirectory(
        "${CMAKE_SOURCE_DIR}/util"
        "${CMAKE_BINARY_DIR}/util")
endif()

target_link_libraries(${PROJECT_NAME} PUBLIC platform util)

install(DIRECTORY 
          inc/ 
          adc/inc/
          gpio/inc/
          uart/inc/
        DESTINATION include
        FILES_MATCHING PATTERN "*.h" PATTERN "*.hpp")

install(TARGETS hal_stm32f072)
