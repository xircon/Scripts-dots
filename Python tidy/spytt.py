#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 01:14:21 2017

@author: steve
"""

from sh import inxi
print(inxi("-Fxzc0"))