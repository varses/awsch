# -*- coding: utf-8 -*-
"""
    lantz.drivers.newport.aguc8
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Implementation of Agilis UC8 piezo controller

    Author: Kevin Miao
    Date: 12/14/2015

"""

from lantz import Action, Feat
from lantz.messagebased import MessageBasedDriver

class Agilis(MessageBasedDriver):

    DEFAULTS = {
        'ASRL': {
            'write_termination': '\r\n',
            'read_termination': '\r\n',
            'baud_rate': 921600,
        }
    }

    @Action()
    def reset(self):
        """
        Reset controller
        """
        self.send('RS')

    @Action()
    def channel(self, value):
        """
        Set channel
        """
        self.send('CC{}'.format(value))

    #@Feat(values={1, 2, 3, 4})
    @Feat()
    def channel(self):
        return self.query('CC?')
