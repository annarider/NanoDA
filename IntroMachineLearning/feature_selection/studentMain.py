# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 20:28:03 2015

@author: horsepower
"""

#!/usr/bin/python

import os
import sys
import zipfile
from poi_flag_email import poiFlagEmail, getToFromStrings

data_dict = {}

with zipfile.ZipFile('emails.zip', "r") as z:
    z.extractall()

for email_message in os.listdir("emails"):
    if email_message == ".DS_Store":
        continue
    print sys.path
    message = open(os.getcwd()+"/emails/"+email_message, "r")
    to_addresses, from_addresses, cc_addresses = getToFromStrings(message) 
    
    to_poi, from_poi, cc_poi = poiFlagEmail(message)
    
    for recipient in to_addresses:
        if recipient not in data_dict:
            data_dict[recipient] = {"from_poi_to_this_person":0}
        else:
            if from_poi:
                data_dict[recipient]["from_poi_to_this_person"] += 1
                break

    message.close()

for item in data_dict:
    print item, data_dict[item]
    
#######################################################    
def submitData():
    return data_dict