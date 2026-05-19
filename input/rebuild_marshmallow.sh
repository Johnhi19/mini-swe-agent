#!/bin/bash
set -e

cd /home/marshmallow

git checkout -f $1

echo "Re-installing to compile the patch..."
python -m pip install -e '.[dev]'

python -c 'import marshmallow;'

echo "Done rebuilding Marshmallow"