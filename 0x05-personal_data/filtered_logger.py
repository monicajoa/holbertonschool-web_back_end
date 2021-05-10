#!/usr/bin/env python3
"""[This module holds a Regex-ing task]
"""

import logging
from typing import List
import re


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """[The function should use a regex to replace
    occurrences of certain field values]

    Args:
        fields (List[str]): [Strings representing all fields]
        redaction (str): [String representing by what the
        field will be obfuscated]
        message (str): [String representing the log line]
        separator (str): [String representing by which character
        is separating all fields]

    Returns:
        str: [The log message obfuscated]
    """
    for index in fields:
        message = re.sub(index + "=[^=]*" + separator,
                         index + "=" + redaction + separator, message)
    return message
