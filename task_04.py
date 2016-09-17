#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module will ensure we have at least on litter box for each kitten."""


def too_many_kittens(kittens, litterboxes, catfood):
    """Compares the number of kittens to litterboxes.

    Args:
      kittens: interger variable. number of kittens.
      litterboxes: integer variable. number of litterboxes
      catfood: boolean variable. do we have cat food

    Returns: boolean value comparing if we have enough litterboxes
      compared to the number of kittens

    Example:
      >>> too_many_kittens(12, 12, False)
      True
    """
    return not (litterboxes >= kittens and catfood)
