#pragma once

#include <functional>

namespace retarget 
{

void set_stdio_write(std::function<void(char*,int)>);

};