if(CMAKE_EXPORT_COMPILE_COMMANDS)
  # This dreadful mess is to communicate to clang-tidy the C++ system includes.
  # It seems that CMake doesn't support using its own compile_commands.json
  # database, and that clang-tidy doesn't pick up non-default system headers.
  execute_process(
    COMMAND
      bash -c
      "${CMAKE_CXX_COMPILER} -x c++ -Wp,-v /dev/null 2>&1 > /dev/null | grep '^ /' | grep -w 'c++'"
    OUTPUT_VARIABLE COMPILER_HEADERS
    OUTPUT_STRIP_TRAILING_WHITESPACE)
  string(REGEX REPLACE "[ \n\t]+" ";" INCLUDE_COMPILER_HEADERS
                       ${COMPILER_HEADERS})
  set(CMAKE_CXX_STANDARD_INCLUDE_DIRECTORIES ${INCLUDE_COMPILER_HEADERS})
  message(STATUS "${CMAKE_CXX_STANDARD_INCLUDE_DIRECTORIES}")

  execute_process(
    COMMAND
      bash -c
      "${CMAKE_C_COMPILER} -x c -Wp,-v /dev/null 2>&1 > /dev/null | grep '^ /' "
    OUTPUT_VARIABLE COMPILER_HEADERS
    OUTPUT_STRIP_TRAILING_WHITESPACE)
  string(REGEX REPLACE "[ \n\t]+" ";" INCLUDE_COMPILER_HEADERS
                       ${COMPILER_HEADERS})
  set(CMAKE_C_STANDARD_INCLUDE_DIRECTORIES ${INCLUDE_COMPILER_HEADERS})
  message(STATUS "${CMAKE_C_STANDARD_INCLUDE_DIRECTORIES}")

  set(CMAKE_CXX_STANDARD_INCLUDE_DIRECTORIES
      "${CMAKE_CXX_STANDARD_INCLUDE_DIRECTORIES} ${CMAKE_C_STANDARD_INCLUDE_DIRECTORIES}"
  )
endif()