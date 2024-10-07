# conan_embedded_playground
Conan2 embedded playground based on STM32 target and Renode simulator.

## Create arm-toolchain package
conan create . -pr:b=default -pr:h=stm32f072 --build-require

## Create stm32f072_platform package
conan install . -pr:b=default -pr:h=stm32f072
source build/Release/generators/conanbuild.sh 
conan create . -pr:b=default -pr:h=stm32f072

