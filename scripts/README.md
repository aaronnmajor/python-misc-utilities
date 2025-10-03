# Scripts Directory

This directory contains standalone scripts that demonstrate or utilize the utilities in this project.

## Available Scripts

### Example Scripts

- **example_file_processor.py** - Demonstrates file operations utilities
- **example_string_processor.py** - Demonstrates string manipulation utilities  
- **example_datetime_processor.py** - Demonstrates date/time utilities

## Running Scripts

Scripts can be run directly:

```bash
python scripts/example_file_processor.py
python scripts/example_string_processor.py
python scripts/example_datetime_processor.py
```

Or made executable:

```bash
chmod +x scripts/example_file_processor.py
./scripts/example_file_processor.py
```

## Adding Your Own Scripts

1. Create a new Python file in this directory
2. Add a shebang line: `#!/usr/bin/env python3`
3. Import utilities from the `utils` package
4. Document what the script does at the top
5. Make it executable if desired: `chmod +x your_script.py`

See the example scripts for reference on structure and style.
