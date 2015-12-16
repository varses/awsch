# -*- coding: utf-8 -*-
"""
    lantz.drivers.newport.xpsq8
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Implementation of XPS Q8 controller
    NOTE: XPS_Q8_drivers.py must be placed within the same directory
    as this script

    Author: Kevin Miao
    Date: 12/16/2015
"""

from lantz.driver import Driver
import XPS_Q8_drivers

class XPSQ8(Driver):

    def __init__(self, address, port=5001, timeout=20.0):
        super(XPSQ8, self).__init__()
        self._xps = XPS_Q8_drivers.XPS()
        self._socket_id = self._xps.TCP_ConnectToServer(address, port, timeout)
        if self._socket_id == 1:
            self.log_error("Failed to establish XPS connection at {0}:{1}", address, port)
            # how do we proceed gracefully after this?


    @Action()
    def reboot(self):
        self._xps.Reboot(self._socket_id)
        return

    @Feat()
    def abs_position(self):
        pass

    @Action()
    def abs_position(self, channel, position):
        pass

    @Action()
    def rel_position(self, channel, dposition):
        pass
