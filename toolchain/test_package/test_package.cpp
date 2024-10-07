// test_package.cpp

// Include necessary headers
#include <sys/types.h>

extern "C" {

// Stub for _close
int _close(int file) {
    return -1; // Indicate error
}

// Stub for _lseek
off_t _lseek(int file, off_t offset, int whence) {
    return -1; // Indicate error
}

// Stub for _read
ssize_t _read(int file, void *ptr, size_t len) {
    return 0; // Return 0 to indicate EOF
}

// Stub for _write
ssize_t _write(int file, const void *ptr, size_t len) {
    return len; // Pretend that all bytes were written successfully
}

} // extern "C"

int main() {
    return 0;
}

