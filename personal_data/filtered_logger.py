#!/usr/bin/env python3
"""filtered_logger module"""
import re


def filter_datum(fields, redaction, message, separator):
    """Function that returns the log message obfuscated
    Args:
        field: a list of strings representing all
        fields to obfuscate
        redaction: a string representing by
        what the field will be obfuscated
        message: a string representing the log line
        separator: a string representing by which character
        is separating all fields in the log line (message)"""
    for field in fields:
        message = re.sub(rf'{field}=.*?{separator}',
                         f'{field}={redaction}{separator}', message)
    return message
