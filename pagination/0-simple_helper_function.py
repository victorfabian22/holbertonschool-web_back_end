#!/usr/bin/env python3
"""Simple helper function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
    Args:
        page: int
        page_size: int
    """
    index = (page - 1) * page_size
    end = index + page_size
    return (index, end)
