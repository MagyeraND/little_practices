#!/bin/bash

# ========================================
# My First Shell Script
# Description: This script greets the user,
# shows the date, and lists files in the current directory.
# ========================================

echo "👋 Hello, $USER!"
echo "📅 Today is: $(date)"
echo "📂 Current directory: $(pwd)"
echo "📃 Files here:"
ls -lh
