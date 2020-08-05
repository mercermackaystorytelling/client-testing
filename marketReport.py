# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 03:44:54 2020

@author: Gupta
"""



from basicClient import basicClient
import utilityFunctions as uf


import numpy
import scipy 
import matplotlib.pyplot as plt

from time import time
import pdb
import os

import pandas as pd


# from apiclient.discovery import build 
#the previous is the old version and the next one is the new version, but both work 
#since they are an alias of each other 
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials











def initialize_analyticsreporting(keyfilelocation, scopes):
  """Initializes an Analytics Reporting API V4 service object.

  Returns
  -------
  An authorized Analytics Reporting API V4 service object.
  
  """
  
  credentials = ServiceAccountCredentials.from_json_keyfile_name(
      keyfilelocation, scopes)

  # Build the service object.
  analyticsObject = build('analyticsreporting', 'v4', credentials=credentials)

  return analyticsObject




def main():
    """
    This is the main function for defining instances of the client classes 
    and the marketing reporting strategy


    Returns
    -------
    None.

    """
    
    
    SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
    KEY_FILE_LOCATION = 'client_secrets.json'
    



    analyticsObject = initialize_analyticsreporting(KEY_FILE_LOCATION, SCOPES)
    
    
    #define a new instance of a basicClient and send personal info like viewID 
    FlexPod = basicClient("FlexPod", "124843615", analyticsObject, '2020-01-01', '2020-01-30')
    
    
    
    #what functions do you want to run for the marketing report? 
    print(FlexPod.viewID)
    FlexPod.printviewID()

    FlexPod.channelTraffic()
    FlexPod.channelConversion()
    
    FlexPod.campaignTraffic()
    FlexPod.campaignConversion()
    
    FlexPod.referralTraffic()
    FlexPod.referralConversion()
    
    FlexPod.deviceTraffic()
    FlexPod.deviceConversion()
    
    FlexPod.genderTraffic()
    FlexPod.genderConversion()
    
    FlexPod.ageTraffic()
    FlexPod.ageConversion()





    

    
if __name__=='__main__':   
    main() 

























