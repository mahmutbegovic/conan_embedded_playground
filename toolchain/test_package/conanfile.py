from io import StringIO
from conan import ConanFile
from conan.tools.cmake import CMake, cmake_layout
import os


class TestPackageConan(ConanFile):
    settings = "os", "arch", "compiler", "build_type"
    generators = "CMakeToolchain", "VirtualBuildEnv"

    def build_requirements(self):
        self.tool_requires(self.tested_reference_str)

    def layout(self):
        cmake_layout(self)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        toolchain = "arm-none-eabi"
        stdout = StringIO()
        self.run(f"{toolchain}-gcc --version", stdout=stdout)
        assert "Arm GNU Toolchain 13.3.Rel1" in stdout.getvalue()
