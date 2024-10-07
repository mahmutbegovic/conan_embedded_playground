# platform/CMakeLists.txt
cmake_minimum_required(VERSION 3.13)
project(platform)

# Create the platform library
add_library(${PROJECT_NAME} STATIC)

target_sources(${PROJECT_NAME} PRIVATE
  STM32F0xx_HAL_Driver/Src/stm32f0xx_hal.c
  STM32F0xx_HAL_Driver/Src/stm32f0xx_hal_cortex.c
  STM32F0xx_HAL_Driver/Src/stm32f0xx_hal_gpio.c
  STM32F0xx_HAL_Driver/Src/stm32f0xx_hal_rcc.c
  STM32F0xx_HAL_Driver/Src/stm32f0xx_hal_uart.c
  STM32F0xx_HAL_Driver/Src/stm32f0xx_hal_uart_ex.c
  STM32F0xx_HAL_Driver/Src/stm32f0xx_hal_adc.c
  STM32F0xx_HAL_Driver/Src/stm32f0xx_hal_adc_ex.c
  src/stm32f0xx_hal_msp.c
  src/stm32f0xx_it.c
  src/system_stm32f0xx.c
  startup_stm32f072xb.s
)

# Include directories
target_include_directories(${PROJECT_NAME} PUBLIC
  ${CMAKE_CURRENT_SOURCE_DIR}/inc
  ${CMAKE_CURRENT_SOURCE_DIR}/CMSIS/Device/ST/STM32F0xx/Include
  ${CMAKE_CURRENT_SOURCE_DIR}/CMSIS/Include
  ${CMAKE_CURRENT_SOURCE_DIR}/STM32F0xx_HAL_Driver/Inc
)

install(DIRECTORY 
          inc/ 
          STM32F0xx_HAL_Driver/Inc/
          CMSIS/Device/ST/STM32F0xx/Include/
          CMSIS/Include/
        DESTINATION include
        FILES_MATCHING PATTERN "*.h" PATTERN "*.hpp")

install(TARGETS platform)
