from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout


class LibTessConan(ConanFile):
    name = "libtess2"
    version = "1.0.3"

    license = "SGI FREE SOFTWARE LICENSE B Version 2.0."
    author = "Mikko Mononen"

    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    exports_sources = "CMakeLists.txt","Source/*","Include/*"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def layout(self):
        cmake_layout(self)

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.components["libtess2"].libs = ["tess2"]