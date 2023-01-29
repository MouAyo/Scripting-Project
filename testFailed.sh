#!/bin/bash

# Navigate to the local repository
cd path/to/local/repo

# Fetch the latest changes
git fetch

# Switch to the branch you want to delete
git checkout dev

# Remove all files in the branch
git rm -r .

# Commit the changes with a commit message
git commit -m "Test Failed"


