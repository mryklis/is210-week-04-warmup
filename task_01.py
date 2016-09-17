#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" This module provides a function that
    knows what you mean
"""


def know_what_i_mean(wink, numwink=2):
    """Returns a string, replacing the number of winks and nudges.

    Uses format to insert the number of winks and nudges into retstr.

    Args:
      wink: string variable consisting of wink repeated by the number
      of numwink.
      numwink: integer variable set to 2

    Returns:
        retstr: string variable that knows what I mean

    Example:

    >>> know_what_i_mean('maxim', 2)
    'Know what I mean? maximmaxim nudge nudge'
    """
    winks = (wink * numwink).strip()
    nudges = ('nudge ' * numwink).strip()
    retstr = 'Know what I mean? {0}, {1}'.format(winks, nudges)
    return retstr
