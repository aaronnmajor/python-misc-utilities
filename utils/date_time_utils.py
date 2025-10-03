"""
Date and time utilities for common datetime operations.
"""

from datetime import datetime, timedelta


def format_datetime(dt: datetime, format_string: str = "%Y-%m-%d %H:%M:%S") -> str:
    """
    Format a datetime object to a string.

    Args:
        dt: Datetime object
        format_string: Format string (default: 'YYYY-MM-DD HH:MM:SS')

    Returns:
        Formatted datetime string
    """
    return dt.strftime(format_string)


def parse_datetime(date_string: str, format_string: str = "%Y-%m-%d %H:%M:%S") -> datetime:
    """
    Parse a string to a datetime object.

    Args:
        date_string: Date string to parse
        format_string: Format string (default: 'YYYY-MM-DD HH:MM:SS')

    Returns:
        Datetime object
    """
    return datetime.strptime(date_string, format_string)


def get_current_timestamp() -> str:
    """
    Get current timestamp as a formatted string.

    Returns:
        Current timestamp in 'YYYY-MM-DD HH:MM:SS' format
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def get_date_n_days_ago(n: int) -> datetime:
    """
    Get date n days ago from today.

    Args:
        n: Number of days ago

    Returns:
        Datetime object for n days ago
    """
    return datetime.now() - timedelta(days=n)


def get_date_n_days_ahead(n: int) -> datetime:
    """
    Get date n days ahead from today.

    Args:
        n: Number of days ahead

    Returns:
        Datetime object for n days ahead
    """
    return datetime.now() + timedelta(days=n)


def days_between_dates(date1: datetime, date2: datetime) -> int:
    """
    Calculate the number of days between two dates.

    Args:
        date1: First datetime
        date2: Second datetime

    Returns:
        Number of days between the dates (absolute value)
    """
    return abs((date2 - date1).days)


def is_weekend(dt: datetime) -> bool:
    """
    Check if a given date falls on a weekend.

    Args:
        dt: Datetime object to check

    Returns:
        True if weekend (Saturday or Sunday), False otherwise
    """
    return dt.weekday() >= 5


def get_day_name(dt: datetime) -> str:
    """
    Get the day name for a given date.

    Args:
        dt: Datetime object

    Returns:
        Day name (e.g., 'Monday', 'Tuesday')
    """
    return dt.strftime("%A")


def get_month_name(dt: datetime) -> str:
    """
    Get the month name for a given date.

    Args:
        dt: Datetime object

    Returns:
        Month name (e.g., 'January', 'February')
    """
    return dt.strftime("%B")


def get_quarter(dt: datetime) -> int:
    """
    Get the quarter of the year for a given date.

    Args:
        dt: Datetime object

    Returns:
        Quarter number (1-4)
    """
    return (dt.month - 1) // 3 + 1
