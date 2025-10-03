# Quick Start Guide

Get started with python-misc-utilities in minutes!

## Installation

### Option 1: Install from source (Development)

```bash
git clone https://github.com/aaronnmajor/python-misc-utilities.git
cd python-misc-utilities
pip install -e .
```

### Option 2: Install development dependencies

```bash
pip install -r requirements-dev.txt
```

## Basic Usage

### Using Utilities in Python

```python
# Import utilities
from utils import string_helpers, file_operations, date_time_utils

# String manipulation
username = string_helpers.to_snake_case("HelloWorld")  # "hello_world"
is_valid = string_helpers.is_valid_email("test@example.com")  # True

# File operations
files = file_operations.list_files_by_extension("/path", ".py")
file_operations.ensure_directory_exists("/tmp/my_dir")

# Date/time operations
timestamp = date_time_utils.get_current_timestamp()
is_weekend = date_time_utils.is_weekend(datetime.now())
```

### Running Example Scripts

```bash
# See string utilities in action
python scripts/example_string_processor.py

# See date/time utilities
python scripts/example_datetime_processor.py

# See file operations
python scripts/example_file_processor.py

# Comprehensive examples
python examples/basic_usage.py
```

## Running Tests

```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=utils --cov-report=term-missing

# Run specific test file
pytest tests/test_string_helpers.py -v
```

## Code Quality

```bash
# Format code with Black
black utils/ scripts/ tests/

# Check code style with flake8
flake8 utils/ scripts/ tests/

# Type checking with mypy
mypy utils/
```

## Project Structure

```
python-misc-utilities/
├── utils/              # Core utility modules (import these)
├── scripts/            # Example scripts (run these)
├── tests/              # Unit tests
├── examples/           # Usage examples
└── docs/               # Documentation
```

## What's Included?

### Utility Modules

1. **string_helpers** - String manipulation and validation
   - Case conversions (snake_case, camelCase, PascalCase)
   - Email validation
   - Text processing (truncate, clean, extract)

2. **file_operations** - File and directory utilities
   - Directory creation
   - File listing and filtering
   - File size calculations
   - Read/write operations

3. **date_time_utils** - Date and time helpers
   - Date formatting and parsing
   - Date calculations (days ago/ahead)
   - Date information (weekend, quarter, day name)

### Test Coverage

- ✅ 24 tests, all passing
- ✅ 89% code coverage
- ✅ Tests for all major functionality

## Next Steps

1. **Explore the utilities** - Check out `utils/` to see what's available
2. **Run the examples** - Execute scripts in `scripts/` and `examples/`
3. **Read the docs** - See `CONTRIBUTING.md` and `RECOMMENDATIONS.md`
4. **Add your own** - Follow the guidelines to add your utilities

## Common Tasks

### Add a new utility function

1. Choose or create appropriate module in `utils/`
2. Add function with docstring and type hints
3. Write tests in `tests/`
4. Run tests and ensure they pass
5. Update documentation

### Add a new script

1. Create script in `scripts/`
2. Add shebang: `#!/usr/bin/env python3`
3. Import utilities from `utils/`
4. Document what it does
5. Make executable: `chmod +x scripts/your_script.py`

## Getting Help

- **Documentation**: See `README.md`, `CONTRIBUTING.md`, and `docs/`
- **Examples**: Check `scripts/` and `examples/` directories
- **Issues**: Open an issue on GitHub for questions or bugs

## Tips

- 💡 All utilities have comprehensive docstrings
- 💡 Check existing code for examples
- 💡 Tests show how to use each function
- 💡 Keep utilities simple and focused
- 💡 Document everything you add

Happy coding! 🚀
