macro(print_size target_name)
    add_custom_command(
        TARGET ${target_name}
        POST_BUILD
        COMMAND arm-none-eabi-size ${target_name}
    )
endmacro()

macro(hush_linker_nosys_warnings)
    target_sources(${EXECUTABLE} PRIVATE app/src/nosys_stubs.c)
endmacro()
