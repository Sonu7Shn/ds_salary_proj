# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 09:06:51 2021

@author: sonu7
"""

import glassdoor_scraper as gs
import pandas as pd
path = "C:/Applications/chromedriver"
df = gs.get_jobs('data scientist',15,False,path ,15)