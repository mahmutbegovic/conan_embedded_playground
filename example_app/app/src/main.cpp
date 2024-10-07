#include <cstdio>

#include <retarget.hpp>

#include <hal.hpp>
#include <uart_stm32.hpp>

int main()
{
    hal::init();

    hal::uart_stm32 uart(USART2);
    uart.init();

    retarget::set_stdio_write([&](char *ptr, int len) {
        uart.write_array(ptr, len);
    });

    printf("Hello embeddedBa! \r\n");
    
    while(true)
    {
    }
}
