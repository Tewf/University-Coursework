#!/usr/bin/env bash
# Start a project from one of the templates here: copy cpp/, lay the chosen
# template over it when it is another one, and name it. The folders come
# empty; the .gitkeep files that hold them in the repository stay behind.
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

copy=(rsync -a --exclude build/ --exclude .cache/ --exclude .gitkeep --exclude worked-example.md)
"${copy[@]}" "$templates_dir/cpp"/ "$destination"/
if [ "$template" != cpp ]; then
    "${copy[@]}" "$templates_dir/$template"/ "$destination"/
fi
sed -i "s/^project(change_me /project($project_name /" "$destination/CMakeLists.txt"

echo "created $destination from $template as project '$project_name'"
echo "next: cd $destination && cmake --preset debug && cmake --build --preset debug"
