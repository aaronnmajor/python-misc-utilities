"""
File operation utilities for common file and directory tasks.
"""

import os
import shutil
from pathlib import Path
from typing import List


def ensure_directory_exists(directory_path: str) -> Path:
    """
    Create a directory if it doesn't exist.

    Args:
        directory_path: Path to the directory

    Returns:
        Path object of the directory
    """
    path = Path(directory_path)
    path.mkdir(parents=True, exist_ok=True)
    return path


def list_files_by_extension(directory: str, extension: str) -> List[Path]:
    """
    List all files with a specific extension in a directory.

    Args:
        directory: Directory path to search
        extension: File extension (e.g., '.txt', '.py')

    Returns:
        List of Path objects matching the extension
    """
    path = Path(directory)
    if not extension.startswith("."):
        extension = f".{extension}"
    return list(path.glob(f"*{extension}"))


def get_file_size_mb(file_path: str) -> float:
    """
    Get file size in megabytes.

    Args:
        file_path: Path to the file

    Returns:
        File size in MB
    """
    size_bytes = os.path.getsize(file_path)
    return size_bytes / (1024 * 1024)


def copy_files_by_pattern(source_dir: str, dest_dir: str, pattern: str) -> int:
    """
    Copy files matching a pattern from source to destination directory.

    Args:
        source_dir: Source directory path
        dest_dir: Destination directory path
        pattern: Glob pattern (e.g., '*.txt', '**/*.py')

    Returns:
        Number of files copied
    """
    source_path = Path(source_dir)
    dest_path = Path(dest_dir)
    ensure_directory_exists(str(dest_path))

    count = 0
    for file_path in source_path.glob(pattern):
        if file_path.is_file():
            shutil.copy2(file_path, dest_path / file_path.name)
            count += 1

    return count


def read_file_lines(file_path: str, strip_whitespace: bool = True) -> List[str]:
    """
    Read all lines from a file.

    Args:
        file_path: Path to the file
        strip_whitespace: Whether to strip whitespace from each line

    Returns:
        List of lines from the file
    """
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        if strip_whitespace:
            lines = [line.strip() for line in lines]
        return lines


def write_file_lines(file_path: str, lines: List[str], append: bool = False) -> None:
    """
    Write lines to a file.

    Args:
        file_path: Path to the file
        lines: List of lines to write
        append: Whether to append to existing file or overwrite
    """
    mode = "a" if append else "w"
    with open(file_path, mode, encoding="utf-8") as f:
        for line in lines:
            f.write(f"{line}\n")
