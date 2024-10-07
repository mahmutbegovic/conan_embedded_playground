import os
from conan import ConanFile
from conan.tools.files import get, copy, download
from conan.errors import ConanInvalidConfiguration
from conan.tools.scm import Version
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps

class RenodePackage(ConanFile):
    name = "renode"
    version = "1.15.3"

    license = "MIT"
    homepage = "https://developer.arm.com/downloads/-/arm-gnu-toolchain-downloads"
    description = "Renode was created by Antmicro as a virtual development tool for multi-node embedded networks (both wired and wireless) and is intended to enable a scalable workflow for creating effective, tested and secure IoT systems."
    settings = "os", "arch", "build_type"
    package_type = "application"

    renode_macros = "renode_macros.cmake"
    exports_sources = renode_macros
    generators = "CMakeDeps", "CMakeToolchain"


    def source(self):
        download(self, "https://raw.githubusercontent.com/renode/renode/refs/heads/master/LICENSE", "LICENSE", verify=False)

    def layout(self):
        cmake_layout(self)

    def build(self):
        get(self, f"https://github.com/renode/renode/releases/download/v1.15.3/renode-1.15.3.linux-portable.tar.gz",
            destination="bin", strip_root=True)            

    def package(self):
        dirs_to_copy = ["bin"]
        for dir_name in dirs_to_copy:
            copy(self, pattern=f"{dir_name}/*", src=self.build_folder, dst=self.package_folder, keep_path=True)
        copy(self, "LICENSE", src=self.build_folder, dst=os.path.join(self.package_folder, "licenses"), keep_path=False)
        copy(self, self.renode_macros, self.source_folder, self.package_folder)

    def package_info(self):
        self.cpp_info.set_property("cmake_build_modules", [self.renode_macros])
        self.cpp_info.includedirs = []
        self.cpp_info.libdirs = []
        self.cpp_info.builddirs = ["."]
