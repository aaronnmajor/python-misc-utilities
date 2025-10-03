# Scripts Directory

This directory contains standalone scripts that demonstrate or utilize the utilities in this project.

## Available Scripts

### Example Scripts

- **example_file_processor.py** - Demonstrates file operations utilities
- **example_string_processor.py** - Demonstrates string manipulation utilities  
- **example_datetime_processor.py** - Demonstrates date/time utilities

### Utility Scripts

- **batch_rename_files.py** - Batch rename files using different naming conventions (snake_case, camelCase, PascalCase)

## Running Scripts

Example scripts can be run directly:

```bash
python scripts/example_file_processor.py
python scripts/example_string_processor.py
python scripts/example_datetime_processor.py
```

Utility scripts accept arguments:

```bash
# Preview batch renaming (dry-run)
python scripts/batch_rename_files.py /path/to/files snake

# Actually rename files
python scripts/batch_rename_files.py /path/to/files camel --execute
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
