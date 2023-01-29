#!/bin/bash

# Navigate to the local repository
cd path/to/local/repo

# Fetch the latest changes
git fetch

# Checkout the feature branch
git checkout feature

# Rebase it onto the main branch
git rebase main

# Checkout the main branch
git checkout main

# Merge the feature branch and fast-forward
git merge --ff-only feature

# Push the changes to the main branch
git push origin main