cmake_minimum_required(VERSION 3.10)
project(nanovg)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

add_library(nanovg
  src/fontstash.h
  src/nanovg_gl.h
  src/nanovg.h
  src/stb_truetype.h
  src/nanovg.c
  src/nanovg_gl_utils.h
  src/stb_image.h
  )

target_include_directories(nanovg SYSTEM PUBLIC .)
target_link_libraries(nanovg PUBLIC CONAN_PKG::glfw)

# Rule to install the compiled library
install(TARGETS nanovg DESTINATION lib)

# Rule to install the headers
install(FILES
  src/fontstash.h
  src/nanovg_gl.h
  src/nanovg.h
  src/stb_truetype.h
  src/nanovg_gl_utils.h
  src/stb_image.h
  DESTINATION include
  )
