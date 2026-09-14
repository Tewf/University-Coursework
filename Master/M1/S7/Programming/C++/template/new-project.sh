#!/usr/bin/env bash
# Start a project from this template: copy it next to nothing that could be
# overwritten, name it, and leave the worked example in place to be replaced.
#   ./new-project.sh <destination> [project_name]
# project_name defaults to the destination's folder name.
set -euo pipefail

template_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
destination="${1:?usage: new-project.sh <destination> [project_name]}"
project_name="${2:-$(basename "$destination")}"

if [ -e "$destination" ]; then
    echo "refusing to overwrite $destination" >&2
    exit 1
fi

rsync -a --exclude build/ --exclude .cache/ --exclude new-project.sh \
    "$template_dir"/ "$destination"/
sed -i "s/^project(change_me /project($project_name /" "$destination/CMakeLists.txt"

echo "created $destination as project '$project_name'"
echo "next: cd $destination && cmake --preset debug && cmake --build --preset debug"
