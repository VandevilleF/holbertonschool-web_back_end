#!/usr/bin/env python3
"""filtered_logger module"""
import re


def filter_datum(fields, redaction, message, separator):
    """
    Return the log message obfuscated
    """
    pattern = f"({'|'.join(fields)})=[^{separator}]*"
    return re.sub(pattern, f'\\1={redaction}', message)
