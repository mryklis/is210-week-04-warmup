#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module will ensure we have at least on litter box for each kitten."""

def too_many_kittens(kittens, litterboxes, catfood):
    return not (litterboxes >= kittens and catfood)
    
