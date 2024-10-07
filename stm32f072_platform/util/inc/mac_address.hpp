#pragma once

#include <span>
#include <algorithm>
#include <array>
#include <string_view>
#include <charconv>

namespace util {
struct mac_address {
    static constexpr std::size_t c_bytes_num = 6;
    static constexpr std::size_t c_mac_addr_str_size = 17;

    std::array<uint8_t, c_bytes_num> bytes{};
    bool is_valid = false;

    constexpr mac_address(std::string_view str) {
        if (str.size() != c_mac_addr_str_size) {
            return;
        }

        for (size_t i = 0; i < c_bytes_num; ++i) {
            const std::string_view byte_str = str.substr(i * 3, 2);

            uint8_t value = 0;
            auto result = std::from_chars(byte_str.data(), byte_str.data() + byte_str.size(), value, 16);
            if (result.ec != std::errc()) {
                return;
            }
            bytes[i] = value;
        }
        is_valid = true;
    }
};

void print_48bit_mac(std::span<const uint8_t> mac) {
    printf("%02X:%02X:%02X:%02X:%02X:%02X\r\n", mac[0], mac[1], mac[2],
                                               mac[3], mac[4], mac[5]);
}

};