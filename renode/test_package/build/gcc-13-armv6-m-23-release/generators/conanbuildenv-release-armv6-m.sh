script_folder="/home/amar/projects/conan_playground/renode/test_package/build/gcc-13-armv6-m-23-release/generators"
echo "echo Restoring environment" > "$script_folder/deactivate_conanbuildenv-release-armv6-m.sh"
for v in SIZE OBJCOPY LD CXX CC PATH
do
    is_defined="true"
    value=$(printenv $v) || is_defined="" || true
    if [ -n "$value" ] || [ -n "$is_defined" ]
    then
        echo export "$v='$value'" >> "$script_folder/deactivate_conanbuildenv-release-armv6-m.sh"
    else
        echo unset $v >> "$script_folder/deactivate_conanbuildenv-release-armv6-m.sh"
    fi
done


export SIZE="arm-none-eabi-size"
export OBJCOPY="arm-none-eabi-objcopy"
export LD="arm-none-eabi-ld"
export CXX="arm-none-eabi-g++"
export CC="arm-none-eabi-gcc"
export PATH="/home/amar/.conan2/p/b/renod5a76f2f8fcd28/p/bin:$PATH"