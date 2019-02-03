from conans import ConanFile, CMake, tools
import os
import shutil
import glob


class ImguisfmlConan(ConanFile):
    name = "nanovg"
    version = "f4069e6a1ad5da430fb0a9c57476d5ddc2ff89b2"
    license = "https://raw.githubusercontent.com/memononen/nanovg/master/LICENSE.txt"
    author = "Darlan Cavalcante Moreira (darcamo@gmail.com)"
    url = "https://github.com/darcamo/conan-nanovg"
    description = ( "Antialiased 2D vector drawing library on top of OpenGL for"
                    "UI and visualizations. " )
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    exports_sources = "CMakeLists.txt"
    requires = "glfw/3.2.1@bincrafters/stable"

    def source(self):
        git = tools.Git(folder="nanovg")

        git.clone("https://github.com/memononen/nanovg.git")
        git.checkout(self.version)
        os.rename("nanovg".format(self.version), "sources")

        # Copy the CMakeLists.txt file to the sources folder
        shutil.move("CMakeLists.txt", "sources/")

    def build(self):
        os.mkdir("build")
        shutil.move("conanbuildinfo.cmake", "build/")
        cmake = CMake(self)
        cmake.configure(source_folder="sources", build_folder="build")
        cmake.build()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["nanovg"]
