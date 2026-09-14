#!/usr/bin/env bash
# Start a blank project from one of the templates here. Each template folder
# is a worked example; only its skeleton is copied: the CMake files, cmake/,
# the dotfiles and the README, with the source folders empty.
#   ./new-project.sh <cpp|cpp-python> <destination> [project_name]
# project_name defaults to the destination's folder name.
set -euo pipefail

templates_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
usage="usage: new-project.sh <cpp|cpp-python> <destination> [project_name]"
template="${1:?$usage}"
destination="${2:?$usage}"
project_name="${3:-$(basename "$destination")}"

if [ ! -f "$templates_dir/$template/CMakeLists.txt" ]; then
    echo "no template named '$template' in $templates_dir" >&2
    exit 1
fi
if [ -e "$destination" ]; then
    echo "refusing to overwrite $destination" >&2
    exit 1
fi

# The skeleton: cpp/ first, the chosen template's files over it.
skeleton=(CMakeLists.txt CMakePresets.json cmake .clang-format .gitignore README.md)
mkdir -p "$destination"
for source in cpp "$template"; do
    for item in "${skeleton[@]}"; do
        [ -e "$templates_dir/$source/$item" ] && cp -r "$templates_dir/$source/$item" "$destination/"
    done
done
rm -f "$destination/cmake/README.md"
mkdir -p "$destination"/{include,src,apps,tests}
[ "$template" = cpp-python ] && mkdir -p "$destination/bindings"
sed -i -E "s/^project\([^ ]+ /project($project_name /" "$destination/CMakeLists.txt"

echo "created $destination from $template as project '$project_name'"
echo "next: cd $destination && cmake --preset debug && cmake --build --preset debug"
