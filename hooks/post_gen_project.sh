#!/bin/bash

# Generate lock file
uv lock

# Initiate git repository with an initial commit
git init
git add -A
git commit -m "chore: initial commit"
