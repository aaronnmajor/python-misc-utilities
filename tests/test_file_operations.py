"""Tests for file_operations module."""

import tempfile
from pathlib import Path
from utils.file_operations import (
    ensure_directory_exists,
    list_files_by_extension,
    get_file_size_mb,
    read_file_lines,
    write_file_lines,
)


def test_ensure_directory_exists():
    """Test directory creation."""
    with tempfile.TemporaryDirectory() as tmpdir:
        test_path = Path(tmpdir) / "test" / "nested" / "dir"
        result = ensure_directory_exists(str(test_path))
        assert result.exists()
        assert result.is_dir()


def test_list_files_by_extension():
    """Test listing files by extension."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create test files
        (Path(tmpdir) / "test1.txt").touch()
        (Path(tmpdir) / "test2.txt").touch()
        (Path(tmpdir) / "test.py").touch()

        txt_files = list_files_by_extension(tmpdir, ".txt")
        assert len(txt_files) == 2

        py_files = list_files_by_extension(tmpdir, "py")  # Test without dot
        assert len(py_files) == 1


def test_get_file_size_mb():
    """Test file size calculation."""
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(b"x" * 1024 * 1024)  # Write 1MB
        tmp.flush()
        size = get_file_size_mb(tmp.name)
        assert 0.9 < size < 1.1  # Allow small margin
        Path(tmp.name).unlink()


def test_read_write_file_lines():
    """Test reading and writing file lines."""
    with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".txt") as tmp:
        tmp_path = tmp.name

    try:
        # Write lines
        test_lines = ["Line 1", "Line 2", "Line 3"]
        write_file_lines(tmp_path, test_lines)

        # Read lines
        read_lines = read_file_lines(tmp_path)
        assert read_lines == test_lines

        # Test append
        write_file_lines(tmp_path, ["Line 4"], append=True)
        read_lines = read_file_lines(tmp_path)
        assert len(read_lines) == 4

    finally:
        Path(tmp_path).unlink()


def test_read_file_lines_with_whitespace():
    """Test reading file lines with whitespace handling."""
    with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".txt") as tmp:
        tmp.write("  Line 1  \n")
        tmp.write("Line 2\n")
        tmp_path = tmp.name

    try:
        # Test with strip
        lines = read_file_lines(tmp_path, strip_whitespace=True)
        assert lines == ["Line 1", "Line 2"]

        # Test without strip
        lines = read_file_lines(tmp_path, strip_whitespace=False)
        assert lines[0] == "  Line 1  \n"

    finally:
        Path(tmp_path).unlink()
