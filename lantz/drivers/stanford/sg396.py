# -*- coding: utf-8 -*-
"""
    lantz.drivers.stanford.sg396
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Implementation of SG396 signal generator

    Author: Kevin Miao
    Date: 12/15/2015
"""

import numpy as np
from lantz import Action, Feat, DictFeat, ureg
from lantz.messagebased import MessageBasedDriver

class SG396(MessageBasedDriver):

        DEFAULTS = {
            'COMMON': {
                'write_termination': '\n',
                'read_termination': '\n',
            }
        }

        # Signal synthesis commands

        @Feat()
        def lf_amplitude(self):
            """
            low frequency amplitude (BNC output)
            """
            return self.query('AMPL?')

        @lf_amplitude.setter
        def lf_amplitude(self, value):
            self.send('AMPL{:.2f}'.format(value))

        @Feat()
        def rf_amplitude(self):
            """
            RF amplitude (Type N output)
            """
            return self.query('AMPR?')

        @rf_amplitude.setter
        def rf_amplitude(self, value):
            self.send('AMPR{:.2f}'.format(value))

        @Feat(values={True: 1, False: 0})
        def lf_toggle(self):
            """
            low frequency output state
            """
            return self.query('ENBL?')

        @lf_enable.setter
        def lf_toggle(self, value):
            self.send('ENBL{:d}'.format(value))

        @Feat(values={True: 1, False: 0})
        def rf_toggle(self):
            """
            RF output state
            """
            return self.query('ENBR?')

        @rf_enable.setter
        def rf_toggle(self, value):
            self.send('ENBR{:d}'.format(value))
