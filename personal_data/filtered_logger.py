#!/usr/bin/env python3
"""filtered_logger module"""
import re


def filter_datum(fields, redaction, message, separator):
    """Return the log message obfuscated"""
    return re.sub(rf'({"|".join(fields)})=[^ {separator}]*',
                  rf'\1={redaction}', message)
