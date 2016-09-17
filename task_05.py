#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This function performs logical operations"""


def defaults(my_required, my_optional=True):
    """compare two boolean values.

    Args:
      my_required:boolean value. required for function.
      my_optional: boolean value. optional. default set to True.

    Returns:
        boolean value. compares my_required with my_optional.

    Examples:
      >>>defaults(True)
      True
      >>>defaults(False, True)
      False
    """
    return my_optional is my_required
