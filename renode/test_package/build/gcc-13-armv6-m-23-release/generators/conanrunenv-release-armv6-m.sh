script_folder="/home/amar/projects/conan_playground/renode/test_package/build/gcc-13-armv6-m-23-release/generators"
echo "echo Restoring environment" > "$script_folder/deactivate_conanrunenv-release-armv6-m.sh"
for v in 
do
    is_defined="true"
    value=$(printenv $v) || is_defined="" || true
    if [ -n "$value" ] || [ -n "$is_defined" ]
    then
        echo export "$v='$value'" >> "$script_folder/deactivate_conanrunenv-release-armv6-m.sh"
    else
        echo unset $v >> "$script_folder/deactivate_conanrunenv-release-armv6-m.sh"
    fi
done

