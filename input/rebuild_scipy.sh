#!/bin/bash

cd /home/scipy

echo "Checking out commit: $1"
git checkout $1
git submodule update --init --recursive


echo "--- Locating the source file ---"
TARGET_FILE=$(find /home/scipy -name "_fmm_core.cpp" | head -n 1)

if [ -n "$TARGET_FILE" ]; then
    echo "--- Found file at: $TARGET_FILE ---"

    # Execute Python code directly from the shell script
    python3 <<EOF
import os

target = "$TARGET_FILE"
with open(target, 'r') as f:
    content = f.read()

if '#include <cstdint>' not in content:
    with open(target, 'w') as f:
        f.write('#include <cstdint>\n' + content)
    print(f'Successfully patched {target}')
else:
    print('Already patched.')
EOF

fi

python -c "import scipy; print(scipy.__version__)" 

echo "Done"