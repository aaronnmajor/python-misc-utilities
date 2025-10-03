# Python Miscellaneous Utilities

A well-organized collection of miscellaneous Python utilities, helper functions, and standalone scripts that don't warrant their own dedicated projects. This repository serves as a centralized location for reusable code snippets and tools.

## 📋 Overview

This project provides:
- **Utility modules** - Reusable functions for common tasks
- **Example scripts** - Standalone scripts demonstrating utility usage
- **Organized structure** - Clean separation of concerns
- **Well-tested code** - Unit tests for all utilities
- **Easy to extend** - Simple guidelines for adding new utilities

## 🗂️ Project Structure

```
python-misc-utilities/
├── utils/                     # Main utility package
│   ├── __init__.py
│   ├── file_operations.py     # File and directory utilities
│   ├── string_helpers.py      # String manipulation functions
│   └── date_time_utils.py     # Date and time utilities
├── scripts/                   # Standalone scripts
│   ├── example_file_processor.py
│   ├── example_string_processor.py
│   └── example_datetime_processor.py
├── tests/                     # Unit tests
│   ├── test_file_operations.py
│   ├── test_string_helpers.py
│   └── test_date_time_utils.py
├── examples/                  # Usage examples
├── docs/                      # Additional documentation
├── pyproject.toml             # Project configuration
├── requirements.txt           # Runtime dependencies
└── requirements-dev.txt       # Development dependencies
```

## 🚀 Getting Started

### Installation

1. Clone the repository:
```bash
git clone https://github.com/aaronnmajor/python-misc-utilities.git
cd python-misc-utilities
```

2. Install dependencies (optional):
```bash
pip install -r requirements.txt
```

3. Install development dependencies (for testing and linting):
```bash
pip install -r requirements-dev.txt
```

### Usage

#### Using Utilities in Your Code

```python
from utils.string_helpers import to_snake_case, is_valid_email
from utils.file_operations import list_files_by_extension
from utils.date_time_utils import get_current_timestamp

# Convert strings
snake = to_snake_case("HelloWorld")  # Returns: "hello_world"

# Validate email
is_valid = is_valid_email("test@example.com")  # Returns: True

# List files
py_files = list_files_by_extension("/path/to/dir", ".py")

# Get timestamp
timestamp = get_current_timestamp()  # Returns: "2024-01-15 10:30:45"
```

#### Running Example Scripts

```bash
python scripts/example_file_processor.py
python scripts/example_string_processor.py
python scripts/example_datetime_processor.py
```

## 🧪 Testing

Run all tests:
```bash
pytest
```

Run tests with coverage:
```bash
pytest --cov=utils --cov-report=term-missing
```

Run specific test file:
```bash
pytest tests/test_string_helpers.py
```

## 🛠️ Available Utilities

### File Operations (`utils.file_operations`)

- `ensure_directory_exists()` - Create directories safely
- `list_files_by_extension()` - Find files by extension
- `get_file_size_mb()` - Get file size in MB
- `copy_files_by_pattern()` - Copy files matching pattern
- `read_file_lines()` - Read file lines into list
- `write_file_lines()` - Write list of lines to file

### String Helpers (`utils.string_helpers`)

- `to_snake_case()` - Convert to snake_case
- `to_camel_case()` - Convert to camelCase
- `to_pascal_case()` - Convert to PascalCase
- `truncate_string()` - Truncate with suffix
- `remove_extra_whitespace()` - Normalize whitespace
- `extract_numbers()` - Extract numbers from text
- `count_words()` - Count words in string
- `is_valid_email()` - Validate email format
- `reverse_words()` - Reverse word order
- `remove_punctuation()` - Strip punctuation

### Date/Time Utils (`utils.date_time_utils`)

- `format_datetime()` - Format datetime to string
- `parse_datetime()` - Parse string to datetime
- `get_current_timestamp()` - Get current timestamp
- `get_date_n_days_ago()` - Calculate past dates
- `get_date_n_days_ahead()` - Calculate future dates
- `days_between_dates()` - Calculate day difference
- `is_weekend()` - Check if date is weekend
- `get_day_name()` - Get day name
- `get_month_name()` - Get month name
- `get_quarter()` - Get quarter of year

## 📝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on adding new utilities and scripts.

## 📄 License

MIT License - feel free to use this code in your own projects!

## 💡 Recommendations

See [docs/RECOMMENDATIONS.md](docs/RECOMMENDATIONS.md) for best practices and suggestions for organizing your utilities.

## ⭐ Features

- ✅ Clean, organized structure
- ✅ Well-documented code
- ✅ Comprehensive unit tests
- ✅ Type hints for better IDE support
- ✅ Easy to extend and customize
- ✅ No external dependencies (core utilities)
- ✅ Python 3.8+ compatible

## 🤝 Support

For questions, issues, or suggestions, please open an issue on GitHub.