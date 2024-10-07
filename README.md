# conan_embedded_playground
Conan2 embedded playground based on STM32 target and Renode simulator.

## Create arm-toolchain package
conan create . -pr:b=default -pr:h=stm32f072 --build-require

## Create stm32f072_platform package
conan install . -pr:b=default -pr:h=stm32f072

source build/Release/generators/conanbuild.sh 

conan create . -pr:b=default -pr:h=stm32f072

## Create renode package
conan create . -pr:b=default

## Create example app and run in renode
conan install . -pr:b=default -pr:h=stm32f072

cd build

cmake .. -DCMAKE_TOOLCHAIN_FILE=Release/generators/conan_toolchain.cmake -DCMAKE_BUILD_TYPE=Release

cmake --build . --target run_in_renode

