#!/usr/bin/env python3
"""
Example script demonstrating file operations utilities.

This script shows how to use the file_operations module to:
- List files by extension
- Get file sizes
- Copy files by pattern
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.file_operations import list_files_by_extension, get_file_size_mb, ensure_directory_exists


def main():
    """Demonstrate file operations."""
    print("File Operations Example")
    print("=" * 50)

    # Example 1: List Python files in current directory
    current_dir = Path(__file__).parent.parent
    print(f"\nListing Python files in {current_dir}:")
    py_files = list_files_by_extension(str(current_dir), ".py")
    for py_file in py_files[:5]:  # Show first 5
        print(f"  - {py_file.name}")

    # Example 2: Get file size
    this_file = Path(__file__)
    size_mb = get_file_size_mb(str(this_file))
    print(f"\nThis script size: {size_mb:.4f} MB")

    # Example 3: Ensure directory exists
    temp_dir = ensure_directory_exists("/tmp/test_utils")
    print(f"\nEnsured directory exists: {temp_dir}")


if __name__ == "__main__":
    main()
