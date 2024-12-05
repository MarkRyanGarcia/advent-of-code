#!/bin/bash

# Get the current year
CURRENT_YEAR=$(date +%Y)

# Check if the user provided a year as an argument
if [ $# -eq 1 ]; then
    YEAR=$1
else
    YEAR=$CURRENT_YEAR
    echo "No year provided. Using the current year: $YEAR"
fi

# Check if the specified year directory exists
if [ ! -d "$YEAR" ]; then
    echo "Directory for year $YEAR does not exist."
    exit 1
fi

# Loop through each day's directory and run the solution
for day in "$YEAR"/day*/; do
    if [ -f "${day}sol.py" ]; then
        echo "Running solution for $(basename "$day")..."
        # Change to the day directory
        cd "$day" || { echo "Failed to enter directory $day"; exit 1; }
        # Run the solution with input redirection
        python3 sol.py
        # Go back to the original directory
        cd - > /dev/null
    else
        echo "No solution file found for $(basename "$day")."
    fi
done
