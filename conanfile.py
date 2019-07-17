from conans import ConanFile, CMake, tools
import os
import shutil
import glob


class NanovgConan(ConanFile):
    name = "nanovg"
    version = "2019-04-22-1f9c886"
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
    requires = "glfw/[>=3.3]@bincrafters/stable"
    homepage = "https://github.com/memononen/nanovg.git"

    def source(self):
        git = tools.Git(folder="sources")
        commit_sha1 = self.version.split("-")[-1]
        git.clone(self.homepage)
        git.checkout(commit_sha1)

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
