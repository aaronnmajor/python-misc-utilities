# Recommendations and Best Practices

This document provides recommendations for organizing and maintaining your miscellaneous Python utilities.

## 🎯 Project Organization

### When to Add Code Here

**✅ GOOD candidates for this repository:**
- General-purpose helper functions (string manipulation, file operations, etc.)
- Common algorithms you use across projects
- Data conversion utilities
- Configuration file parsers
- Simple CLI tools and scripts
- Code snippets you frequently reference
- Proof-of-concept implementations
- Learning exercises and experiments

**❌ AVOID adding to this repository:**
- Large applications or frameworks
- Project-specific business logic
- Code with extensive external dependencies
- Deprecated or broken code
- Proprietary or sensitive code
- Copyrighted code you don't own

### Directory Structure Tips

**Keep the structure flat and simple:**
```
utils/
├── category1_utils.py      # Group related functions
├── category2_helpers.py    # Use descriptive names
└── specific_tool.py        # Or standalone for complex utilities
```

**Avoid deep nesting:**
- ❌ `utils/web/http/requests/helpers.py` (too deep)
- ✅ `utils/web_requests.py` (better)

### Module Organization

**Group related functions together:**
```python
# Good: Related functions in one module
# utils/text_processing.py
def clean_text(text): ...
def normalize_whitespace(text): ...
def extract_urls(text): ...

# Avoid: Overly generic module names
# utils/helpers.py  # Too generic!
```

## 🧪 Testing Strategy

### Write Tests for Everything

Even small utilities benefit from tests:
```python
def test_simple_utility():
    """Even simple functions deserve tests."""
    assert capitalize_first("hello") == "Hello"
    assert capitalize_first("") == ""
    assert capitalize_first("123") == "123"
```

### Test Edge Cases

Always test:
- Empty inputs
- None values
- Invalid types
- Boundary conditions
- Error conditions

### Keep Tests Simple

Tests should be readable:
```python
# Good: Clear and simple
def test_sum_numbers():
    assert sum_numbers([1, 2, 3]) == 6

# Avoid: Over-complicated tests
def test_sum_numbers_complex():
    input_data = generate_test_data()
    expected = calculate_expected(input_data)
    assert sum_numbers(input_data) == expected  # What are we testing?
```

## 📝 Documentation Guidelines

### Document Everything

**Module-level documentation:**
```python
"""
Module for handling file operations.

This module provides utilities for common file system tasks
including reading, writing, copying, and searching for files.
"""
```

**Function-level documentation:**
```python
def process_file(path: str, mode: str = 'r') -> List[str]:
    """
    Process a file and return its contents.
    
    Detailed description of what the function does,
    any important notes, and usage examples.
    
    Args:
        path: Path to the file
        mode: File open mode (default: 'r')
        
    Returns:
        List of processed lines
        
    Raises:
        FileNotFoundError: If file doesn't exist
        
    Examples:
        >>> process_file('data.txt')
        ['line1', 'line2']
    """
```

### Add Usage Examples

Create example scripts in the `examples/` or `scripts/` directory to show how utilities work together.

## 🔧 Dependency Management

### Minimize Dependencies

**Core utilities should have zero dependencies:**
```python
# Good: Uses standard library
from pathlib import Path
import json

# Avoid: Adds unnecessary dependency
import some_large_library  # For one small feature
```

### When Dependencies Are Necessary

1. **Document why it's needed** in requirements.txt
2. **Pin versions** for reproducibility
3. **Consider alternatives** from standard library
4. **Add to optional dependencies** if not universally needed

```toml
# pyproject.toml
[project.optional-dependencies]
web = ["requests>=2.28"]
data = ["pandas>=2.0"]
```

## 🎨 Code Quality

### Use Type Hints

Type hints improve IDE support and documentation:
```python
from typing import List, Optional, Dict

def process_items(
    items: List[str],
    config: Optional[Dict[str, any]] = None
) -> List[str]:
    """Process items with optional config."""
    ...
```

### Keep Functions Small

**Single Responsibility Principle:**
```python
# Good: Each function does one thing
def read_file(path: str) -> str:
    with open(path) as f:
        return f.read()

def parse_json(content: str) -> dict:
    return json.loads(content)

def load_json_file(path: str) -> dict:
    content = read_file(path)
    return parse_json(content)

# Avoid: Function doing too much
def load_and_process_and_validate_and_save(path: str): ...
```

### Use Descriptive Names

```python
# Good names
def calculate_average(numbers: List[float]) -> float:
def is_valid_email(email: str) -> bool:
def convert_to_snake_case(text: str) -> str:

# Poor names
def calc(nums):  # Too abbreviated
def do_stuff():  # Not descriptive
def helper():    # Too generic
```

## 🚀 Performance Considerations

### Profile Before Optimizing

Don't optimize prematurely:
```python
# Start with clear, simple code
def find_duplicates(items: List[str]) -> List[str]:
    return [item for item in items if items.count(item) > 1]

# Optimize only if needed (after profiling)
def find_duplicates_fast(items: List[str]) -> List[str]:
    counts = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    return [item for item, count in counts.items() if count > 1]
```

### Document Performance Characteristics

```python
def linear_search(items: List[int], target: int) -> int:
    """
    Find target in items.
    
    Time complexity: O(n)
    Space complexity: O(1)
    
    Note: Consider using binary search for sorted lists.
    """
```

## 🔒 Error Handling

### Fail Gracefully

```python
def safe_divide(a: float, b: float) -> Optional[float]:
    """
    Divide a by b, returning None on error.
    
    Args:
        a: Numerator
        b: Denominator
        
    Returns:
        Result or None if division fails
    """
    try:
        return a / b
    except ZeroDivisionError:
        return None
```

### Validate Inputs

```python
def process_file(path: str) -> str:
    """Process file with input validation."""
    if not path:
        raise ValueError("path cannot be empty")
    
    path_obj = Path(path)
    if not path_obj.exists():
        raise FileNotFoundError(f"File not found: {path}")
    
    # Process file...
```

## 📊 Version Control

### Commit Messages

Use clear, descriptive commit messages:
```
✅ Good:
- "Add string truncation utility"
- "Fix edge case in email validator"
- "Update documentation for file operations"

❌ Avoid:
- "Update"
- "Fix stuff"
- "Changes"
```

### Keep Commits Focused

One logical change per commit:
- ✅ "Add email validation function"
- ✅ "Add tests for email validation"
- ✅ "Update README with email validation example"

Rather than:
- ❌ "Add features, fix bugs, update docs"

## 🎓 Learning and Experimentation

### Use This Repository for Learning

This is a great place to:
- Implement algorithms for learning
- Try new Python features
- Experiment with design patterns
- Practice TDD (Test-Driven Development)
- Document your learnings

### Keep Experimental Code Separate

```
utils/          # Stable, tested utilities
scripts/        # Working scripts
examples/       # Usage examples
experiments/    # Experimental code (not in git)
```

Add `experiments/` to `.gitignore` for work-in-progress code.

## 🔄 Maintenance

### Regular Cleanup

Periodically review and:
- Remove unused code
- Update documentation
- Refactor duplicated code
- Improve test coverage
- Update dependencies

### Keep Dependencies Updated

```bash
# Check for outdated packages
pip list --outdated

# Update requirements files
pip freeze > requirements.txt
```

## 📚 Useful Patterns

### Builder Pattern for Complex Objects

```python
class ConfigBuilder:
    """Build configuration step by step."""
    
    def __init__(self):
        self._config = {}
    
    def set_host(self, host: str):
        self._config['host'] = host
        return self
    
    def set_port(self, port: int):
        self._config['port'] = port
        return self
    
    def build(self) -> dict:
        return self._config

# Usage
config = ConfigBuilder().set_host('localhost').set_port(8080).build()
```

### Decorator Pattern for Common Operations

```python
import time
from functools import wraps

def timing_decorator(func):
    """Measure function execution time."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end-start:.2f}s")
        return result
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(1)
```

### Context Managers for Resource Management

```python
from contextlib import contextmanager

@contextmanager
def temp_directory():
    """Create and cleanup temporary directory."""
    import tempfile
    import shutil
    
    tmpdir = tempfile.mkdtemp()
    try:
        yield tmpdir
    finally:
        shutil.rmtree(tmpdir)

# Usage
with temp_directory() as tmpdir:
    # Use temporary directory
    pass
# Automatically cleaned up
```

## 💡 Additional Tips

1. **README First**: Document before coding helps clarify requirements
2. **Small PRs**: Easier to review and merge
3. **Consistent Style**: Use formatters like Black
4. **Code Review**: Review your own code before committing
5. **Automate**: Use pre-commit hooks for quality checks
6. **Learn from Others**: Study well-written Python projects
7. **Keep Learning**: Python evolves, stay updated

## 📖 Recommended Reading

- "Clean Code" by Robert C. Martin
- "The Pragmatic Programmer" by Hunt & Thomas
- "Fluent Python" by Luciano Ramalho
- Python official documentation: https://docs.python.org/
- Real Python tutorials: https://realpython.com/

## 🎯 Summary

The key to a successful miscellaneous utilities repository:
1. Keep it simple and organized
2. Document everything
3. Test everything
4. Minimize dependencies
5. Make it easy to find and use utilities
6. Review and refactor regularly

Happy coding! 🚀
