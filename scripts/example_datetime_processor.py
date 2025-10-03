#!/usr/bin/env python3
"""
Example script demonstrating date/time utilities.

This script shows how to use the date_time_utils module for:
- Date formatting
- Date calculations
- Day/month information
"""

import sys
from pathlib import Path
from datetime import datetime

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.date_time_utils import (
    get_current_timestamp,
    get_date_n_days_ago,
    get_date_n_days_ahead,
    is_weekend,
    get_day_name,
    get_month_name,
    get_quarter,
)


def main():
    """Demonstrate date/time operations."""
    print("Date/Time Operations Example")
    print("=" * 50)

    # Example 1: Current timestamp
    print(f"\nCurrent timestamp: {get_current_timestamp()}")

    # Example 2: Date calculations
    print("\nDate calculations:")
    print(f"  7 days ago: {get_date_n_days_ago(7).strftime('%Y-%m-%d')}")
    print(f"  7 days ahead: {get_date_n_days_ahead(7).strftime('%Y-%m-%d')}")

    # Example 3: Day information
    now = datetime.now()
    print("\nCurrent date information:")
    print(f"  Day: {get_day_name(now)}")
    print(f"  Month: {get_month_name(now)}")
    print(f"  Quarter: Q{get_quarter(now)}")
    print(f"  Is weekend: {'Yes' if is_weekend(now) else 'No'}")


if __name__ == "__main__":
    main()
