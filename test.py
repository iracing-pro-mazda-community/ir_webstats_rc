#!/usr/bin/python
import sys
from ir_webstats_rc import constants as ct
from ir_webstats_rc.client import iRWebStats
from ir_webstats_rc.util import clean

irw = iRWebStats()
irw.login('rob.crouch@gmail.com', 'cYFVPo%^Gs03')

if irw.logged:
    print(irw.current_series_images())

