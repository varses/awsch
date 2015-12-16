# -*- coding: utf-8 -*-
"""
    AG-UC8.py

    :brief Implements the drivers for the agilis controller

    :author AlexBourassa
"""

from lantz import Feat, DictFeat, Action
from lantz.errors import InstrumentError
from lantz.messagebased import MessageBasedDriver

import pyvisa.resources.serial as _s

jog_modes = {'no move': '0','1700 step/s' : '3', '666 step/s' : '4',  '100 step/s' : '2',  '5 step/s': '1',
                            '-1700 step/s': '-3','-666 step/s': '-4', '-100 step/s': '-2', '-5 step/s': '-1'}

class AG_UC8(MessageBasedDriver):
    """
    Implements the drivers for the agilis controller
    """
    
    DEFAULTS = {'ASRL': {'write_termination': '\n',
                                'read_termination': '\n'}}

    def __init__(self, resource_name, name='AG-UC8', baud_rate=921600, data_bits=8, stop_bits = _s.constants.StopBits.one, timeout = 20, parity=_s.constants.Parity.none,**kwargs):
        MessageBasedDriver.__init__(self, resource_name=resource_name, name=name, baud_rate=baud_rate, data_bits=data_bits, parity=parity, stop_bits =stop_bits, timeout=timeout, **kwargs)

    @Feat()
    def limit_status(self):
        """Tell limit status
        """
        return self.query('PH?')

    @DictFeat(keys=[1,2], values=jog_modes)
    def jog_mode(self, key):
        """Start jog motion or get jog mode
        """
        try:
            ans= self.query(str(key) + 'JA?')
            return ans[-2]
        except:
            return '0' #This is never actually returned... That is, if there is no motion the controller won't respond

    @jog_mode.setter
    def jog_mode(self, key, value):
        self.write('{}JA{}'.format(key, value))


    @Feat()
    def error_status(self):
        """Get error of previous command
             0  No error
            -1  Unknown command
            -2  Axis out of range (must be 1 or 2, or must not be specified)
            -3  Wrong format for parameter nn (or must not be specified)
            -4  Parameter nn out of range
            -5  Not allowed in local mode
            -6  Not allowed in current state
        """
        return self.query('TE?')


    @DictFeat(keys=[1,2], values=jog_modes)
    def move_to_limit(self, key):
        """Move to limit
        """
        try:
            ans= self.query(str(key) + 'MV?')
            return ans[-2]
        except:
            return '0' #This is never actually returned... That is, if there

    @move_to_limit.setter
    def move_to_limit(self, key, value):
        self.write('{}MV{}'.format(key, value))


    @Action()
    def stop_all(self):
        """Throw all the stop command in the book!
            Hopefully one of them works...
        """
        for i in [1,2]: self.move_to_limit[i] = 'no move'
        for i in [1,2]: self.jog_mode[i] = 'no move'
        # for stop_cmd in ['1MV0','2MV0','1JA0','2JA0']:
        #     self.write(stop_cmd)


    def check_connect(self):
        pass