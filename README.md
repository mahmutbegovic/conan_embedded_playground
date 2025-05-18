# conan_embedded_playground
Conan2 embedded playground based on STM32 target and Renode simulator.
In this example we create the following packages
- `arm-toolchain` - contains GCC arm-none-eabi toolchain
- `stm32f072_platfrom` - conatins STM provided HAL wrapped in C++, exports static library and headers
- `renode` - conains Renode simulator and CMake macro used to integrate it in a project
- `example_app` - uses all the above packages to build a simple firmware and run it in Renode simulator 

# Copy profiles
cp -v profiles/* "$HOME/.conan2/profiles/"

## Create arm-toolchain package
cd toolchain

conan create . -pr:b=default -pr:h=stm32f072 --build-require

## Create stm32f072_platform package
cd stm32f072_platform 

conan install . -pr:b=default -pr:h=stm32f072

source build/Release/generators/conanbuild.sh 

conan create . -pr:b=default -pr:h=stm32f072

## Create renode package
cd renode 

conan create . -pr:b=default

## Create example app and run in renode
cd example_app

conan install . -pr:b=default -pr:h=stm32f072

cd build

cmake .. -DCMAKE_TOOLCHAIN_FILE=Release/generators/conan_toolchain.cmake -DCMAKE_BUILD_TYPE=Release

cmake --build . --target run_in_renode

