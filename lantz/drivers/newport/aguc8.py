# -*- coding: utf-8 -*-
"""
    lantz.drivers.newport.ag_uc8
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Implementation of Agilis UC8 piezo controller

    Author: Kevin Miao
    Date: 12/14/2015

"""

from lantz.foreign import LibraryDriver, RetValue, RetStr



class Base(LibraryDriver):

    LIBRARY_NAME = 'AgilisCmdLib'
