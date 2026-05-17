#!/bin/bash
set -e

cd /home/pandas

git checkout -f $1

echo "Re-installing to compile the patch..."
python -c 'import pandas; print(pandas.__version__)'