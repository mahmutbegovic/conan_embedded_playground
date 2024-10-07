import os
from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps
from conan.tools.files import copy


class Stm32f072Platform(ConanFile):
    name = "stm32f072_platform"
    version = "1.0"

    author = "Amar Mahmutbegovic amar@semblie.com"

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "cstdlib_support/*", "hal/*", "platform/*", "util/*"

    generators = "CMakeToolchain", "CMakeDeps"

    def layout(self):
        cmake_layout(self)

    def build_requirements(self):
        self.tool_requires("arm-toolchain/13.3")
        self.tool_requires("cmake/3.26.5")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()
        copy(self, "STM32F072C8Tx_FLASH.ld", src=os.path.join(self.source_folder, "platform"), dst=os.path.join(self.package_folder, "linker_script"))

    def package_info(self):
        self.cpp_info.libs = ["hal_stm32f072", "platform", "cstdlib_support"]
        self.cpp_info.libdirs = ["lib"]
        self.cpp_info.includedirs = ["include"]
        self.cpp_info.exelinkflags = ["-T" + os.path.join(self.package_folder, "linker_script", "STM32F072C8Tx_FLASH.ld")]  # linker flags




    # def generate(self):
    #     tc = CMakeToolchain(self)
    #     print("################################# GENERATE ############################")
    #     print(tc.blocks["arch_flags"].values)
    #     tc.blocks.remove("arch_flags")
    #     tc.generate()
################################# GENERATE ############################
#{'arch_flag': '-m64'}

