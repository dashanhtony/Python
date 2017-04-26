#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

jobName='aaaaab'
if re.match('.*aaaaa.*',jobName):
    print('yes,you are right')
else:
    print('no')
