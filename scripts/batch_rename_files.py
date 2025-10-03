#!/usr/bin/env python3
"""
Batch rename files with various naming conventions.

This script demonstrates how to use string helpers to batch rename files
in a directory according to different naming conventions.
"""

import sys
from pathlib import Path
import argparse

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.string_helpers import to_snake_case, to_camel_case, to_pascal_case


def batch_rename(directory: str, convention: str, dry_run: bool = True):
    """
    Batch rename files in a directory to a specific naming convention.

    Args:
        directory: Path to directory containing files
        convention: Naming convention ('snake', 'camel', or 'pascal')
        dry_run: If True, only show what would be renamed without actually renaming
    """
    path = Path(directory)

    if not path.exists():
        print(f"Error: Directory '{directory}' does not exist")
        return

    # Map conventions to functions
    converters = {
        "snake": to_snake_case,
        "camel": to_camel_case,
        "pascal": to_pascal_case,
    }

    if convention not in converters:
        print(f"Error: Unknown convention '{convention}'")
        print(f"Available: {', '.join(converters.keys())}")
        return

    converter = converters[convention]

    # Get all files (not directories)
    files = [f for f in path.iterdir() if f.is_file()]

    if not files:
        print(f"No files found in {directory}")
        return

    print(f"\nBatch rename using {convention} convention")
    print("=" * 60)

    renamed_count = 0
    for file_path in files:
        # Split filename and extension
        stem = file_path.stem
        suffix = file_path.suffix

        # Convert the filename (without extension)
        new_stem = converter(stem)
        new_name = new_stem + suffix

        if stem + suffix == new_name:
            # Skip if name doesn't change
            continue

        new_path = file_path.parent / new_name

        # Check if target already exists
        if new_path.exists() and new_path != file_path:
            print(f"⚠ Skip: {file_path.name} (target exists)")
            continue

        if dry_run:
            print(f"Would rename: {file_path.name} → {new_name}")
        else:
            file_path.rename(new_path)
            print(f"✓ Renamed: {file_path.name} → {new_name}")

        renamed_count += 1

    if renamed_count == 0:
        print("\nNo files needed renaming.")
    elif dry_run:
        print(f"\nWould rename {renamed_count} file(s)")
        print("Run with --execute to perform the renaming")
    else:
        print(f"\nSuccessfully renamed {renamed_count} file(s)")


def main():
    """Main function with argument parsing."""
    parser = argparse.ArgumentParser(
        description="Batch rename files using different naming conventions",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Preview snake_case renaming in current directory
  python batch_rename_files.py . snake

  # Actually rename files to camelCase
  python batch_rename_files.py /path/to/files camel --execute

  # Convert to PascalCase
  python batch_rename_files.py ./documents pascal --execute
        """,
    )

    parser.add_argument("directory", help="Directory containing files to rename")
    parser.add_argument(
        "convention",
        choices=["snake", "camel", "pascal"],
        help="Naming convention to use",
    )
    parser.add_argument(
        "--execute",
        action="store_true",
        help="Actually perform the renaming (default is dry-run)",
    )

    args = parser.parse_args()

    batch_rename(args.directory, args.convention, dry_run=not args.execute)


if __name__ == "__main__":
    main()
