#!/bin/bash

scripts=($(find ./tests -type f -name "*.sh"))

for script in "${scripts[@]}"; do
    echo "=== ${script#./} ==="
    cat $script
    echo "=== End of ${script#./} ==="
    echo "### ${script#./} result:"
    bash "$script"
    echo ""
    echo ""
done
