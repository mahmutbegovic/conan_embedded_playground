macro(add_run_in_renode_target RENODE_SCRIPT EXECUTABLE_FULL_PATH)
    add_custom_target(
        run_in_renode
        COMMAND renode
            --console 
            --disable-xwt 
            ${RENODE_SCRIPT}
            -e "logLevel 3 sysbus"
            -e "sysbus LoadELF @${EXECUTABLE_FULL_PATH}"
            -e start 
        DEPENDS ${EXECUTABLE_FULL_PATH}
    )
endmacro()