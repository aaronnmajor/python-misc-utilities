# Contributing to Python Miscellaneous Utilities

Thank you for considering contributing to this project! This guide will help you add new utilities and scripts effectively.

## 🎯 Purpose

This repository houses miscellaneous utilities and scripts that don't warrant their own dedicated projects. Keep this in mind when adding new content:

- ✅ **DO** add general-purpose utilities that can be reused across projects
- ✅ **DO** add small helper functions that solve common problems
- ✅ **DO** add standalone scripts that demonstrate useful techniques
- ❌ **DON'T** add large frameworks or complex applications
- ❌ **DON'T** add project-specific code that only works in one context
- ❌ **DON'T** add code with many external dependencies (unless necessary)

## 📁 Where to Add Your Code

### Adding a New Utility Function

**Location:** `utils/` directory

1. **Choose the appropriate module** based on functionality:
   - `file_operations.py` - File and directory operations
   - `string_helpers.py` - String manipulation and validation
   - `date_time_utils.py` - Date and time operations
   - Or create a new module for a different category

2. **Follow the existing pattern:**
   ```python
   def your_utility_function(param1: str, param2: int) -> str:
       """
       Brief description of what the function does.
       
       Args:
           param1: Description of first parameter
           param2: Description of second parameter
           
       Returns:
           Description of return value
       """
       # Implementation
       return result
   ```

3. **Add to `utils/__init__.py`** if creating a new module

### Adding a New Script

**Location:** `scripts/` directory

1. **Create a standalone Python file:**
   ```python
   #!/usr/bin/env python3
   """
   Brief description of what the script does.
   
   Longer description with usage examples.
   """
   
   import sys
   from pathlib import Path
   
   # Add parent directory to path for imports
   sys.path.insert(0, str(Path(__file__).parent.parent))
   
   from utils import some_utility
   
   def main():
       """Main function."""
       # Your script logic
       pass
   
   if __name__ == '__main__':
       main()
   ```

2. **Make it executable** (optional):
   ```bash
   chmod +x scripts/your_script.py
   ```

3. **Document it** in `scripts/README.md`

### Adding Tests

**Location:** `tests/` directory

1. **Create or update test file:**
   - Tests for `utils/string_helpers.py` go in `tests/test_string_helpers.py`
   - Follow the naming convention: `test_<module_name>.py`

2. **Write clear test functions:**
   ```python
   def test_your_function():
       """Test description."""
       result = your_function("input")
       assert result == "expected_output"
   ```

3. **Test edge cases:**
   - Empty inputs
   - Invalid inputs
   - Boundary conditions
   - Typical use cases

### Adding Examples

**Location:** `examples/` directory

Add usage examples, sample data files, or demonstration notebooks.

## 🎨 Code Style Guidelines

### General Principles

- **Keep it simple** - Prefer simple, readable code over clever solutions
- **Document everything** - All functions should have docstrings
- **Type hints** - Use type hints for function parameters and returns
- **No side effects** - Functions should not modify global state
- **Pure functions** - Prefer pure functions when possible

### Python Style

- Follow **PEP 8** style guide
- Use **Black** formatter (line length: 100)
- Maximum line length: 100 characters
- Use **4 spaces** for indentation (no tabs)
- Use **snake_case** for functions and variables
- Use **PascalCase** for classes
- Use **UPPER_CASE** for constants

### Documentation Style

Use Google-style docstrings:

```python
def function_name(param1: str, param2: int = 0) -> bool:
    """
    One-line summary.
    
    Longer description if needed.
    Can span multiple lines.
    
    Args:
        param1: Description of param1
        param2: Description of param2 (default: 0)
        
    Returns:
        Description of return value
        
    Raises:
        ValueError: When invalid input provided
        
    Examples:
        >>> function_name("test", 5)
        True
    """
```

## ✅ Checklist Before Submitting

- [ ] Code follows the project style guidelines
- [ ] All functions have docstrings
- [ ] Type hints are included
- [ ] Tests are written and passing
- [ ] No external dependencies added (or justified if necessary)
- [ ] Code works with Python 3.8+
- [ ] Documentation is updated (README, module docs, etc.)
- [ ] Examples are provided for complex functionality

## 🧪 Testing Your Changes

1. **Run all tests:**
   ```bash
   pytest
   ```

2. **Check test coverage:**
   ```bash
   pytest --cov=utils --cov-report=term-missing
   ```

3. **Format code:**
   ```bash
   black utils/ scripts/ tests/
   ```

4. **Check style:**
   ```bash
   flake8 utils/ scripts/ tests/
   ```

5. **Type checking:**
   ```bash
   mypy utils/
   ```

## 🔄 Development Workflow

1. **Create a branch** for your changes
2. **Make your changes** following the guidelines
3. **Test your changes** thoroughly
4. **Update documentation** as needed
5. **Commit with clear messages**
6. **Submit a pull request** with description

## 💡 Tips for Good Utilities

### Characteristics of Good Utilities

- ✅ **Reusable** - Works in multiple contexts
- ✅ **Well-named** - Name clearly describes purpose
- ✅ **Single responsibility** - Does one thing well
- ✅ **Testable** - Easy to write tests for
- ✅ **Documented** - Clear documentation and examples
- ✅ **Minimal dependencies** - Avoids external packages when possible

### Characteristics of Good Scripts

- ✅ **Self-contained** - Can run independently
- ✅ **Documented** - Clear purpose and usage
- ✅ **Example-driven** - Demonstrates utility usage
- ✅ **Error handling** - Handles errors gracefully
- ✅ **Configurable** - Uses arguments or config when appropriate

## 📚 Additional Resources

- [PEP 8 - Style Guide](https://pep8.org/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
- [Type Hints (PEP 484)](https://www.python.org/dev/peps/pep-0484/)
- [Pytest Documentation](https://docs.pytest.org/)

## ❓ Questions?

If you have questions about contributing, feel free to:
- Open an issue for discussion
- Check existing code for examples
- Reach out to maintainers

Thank you for contributing! 🎉
