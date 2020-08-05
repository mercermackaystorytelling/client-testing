# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 03:44:54 2020

@author: Gupta
"""


import numpy as np
import scipy
import matplotlib.pyplot as plt

from time import time
import pdb
import os

import pandas as pd







class basicClient:
    """ 
    This is your basic version of a client. This means that this class will 
    handle data and methods common to every client. Whatever you offer to every client
    in the marketing report is defined here. 
    
    """
    
    # class attributes here 






    def __init__(self, name, viewID, analyticsObject, startDate, endDate):
        """
        initializes every instance 

        Parameters
        ----------
        name : TYPE
            DESCRIPTION.
        viewID : TYPE
            DESCRIPTION.
        analyticsObject: TYPE 
            DESCRIPTION.
        startDate: TYPE
            DESCRIPTION.
        endDate: TYPE
            DESCRIPTION

        Returns
        -------
        None.

        """
        
        self.clientName = name
        self.viewID = viewID
        self.analyticsObject = analyticsObject
        self.startDate = startDate
        self.endDate = endDate
    
    
    
    
    def printviewID(self):
        print("{}'s View ID on Google Analytics is {}".format(self.clientName, self.viewID))



    
        
    def parseAndPrint(self, response):
        """
        Function to parse the json response file and 
        print and plot the data

        NEEDS TO BE SUBDIVIDED INTO SMALLER FUNCTIONS 
        
        Parameters
        ----------
        response : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        
        
       
        # metricHeaderList = []
        # metricHeaderarray = np.zeros()
      
      
        # df = pd.DataFrame(response[''])
      
        # print(df)
      
        # print(response)
        
        # metricValueArray = np.zeros(6)
      
        # count = 0
      
        for report in response.get('reports', []):
            columnHeader = report.get('columnHeader', {})
            dimensionHeaders = columnHeader.get('dimensions', [])
            metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])
        
        
            # print(dimensionHeaders)
            # print(metricHeaders)
    
            totalMetric = 0
            metricList = [] 
            metricValueList = []
            dimensionList = []
    
            for row in report.get('data', {}).get('rows', []):
                dimensions = row.get('dimensions', [])
                dateRangeValues = row.get('metrics', [])
    
            
                for header, dimension in zip(dimensionHeaders, dimensions):
                    print(header[3:] + ': ' + dimension)
                    dimensionList.append(dimension)
                    # print(dimension)
                    # print(header + ': ', dimension)

                            
                for i, values in enumerate(dateRangeValues):
                     # print('Date range:', i)
                     for metricHeader, value in zip(metricHeaders, values.get('values')):
                         print(metricHeader.get('name') + ':', value)
                         print(value)
                         metricList.append(metricHeader.get('name'))
                         metricValueList.append(int(value))
                         totalMetric = totalMetric + int(value) 
                         print("---",totalMetric)
                    #this dot index method assumes there is only one maximum value
                    #add a case for when two or more highest exist
        
            print('For date range:', dimensionList[metricValueList.index(max(metricValueList))], 
                          'drove the highest amount of traffic with', (max(metricValueList)/totalMetric)*100, 
                          '% of the total')
                         
            print("-----------------------------------------------------")
                    
                   
                
                # for metricHeader, value in zip(metricHeaders, values.get('values')):
                #     print(metricHeader.get('name')[3:]) #+ ': ' + value
                #     metricHeaderList.append(value)
                #     metricValueArray[count] = value
                #     count += 1 
                    
    #                 print(value)
    
        
        
    #     plt.bar(dimensionList, height=metricValueArray, width=0.4, align='center', color='g')
    #     # plt.xlabel('source/Medium')
    #     # plt.ylabel('organic searches')
    #     plt.xticks(fontsize=10)
    #     plt.yticks(fontsize=10)
    #     # plt.title('Which source/medium drove the highest organic searches?')
    
    #     print('haha am done with parse and print function')
    #     print('dimensionList is', dimensionList)
    #     print('metricHeaderList is', metricHeaderList)
    #     print('metricValueArray is', metricValueArray)
    


    def getReport(self, expression, dimension):
        return self.analyticsObject.reports().batchGet(
                                            body={
                                                'reportRequests': 
                                                    [
                                                        {
                                                            'viewId':  self.viewID,
                                                            'dateRanges': 
                                                                [
                                                                    {'startDate': self.startDate, 'endDate': self.endDate}
                                                                ],
                                                            'metrics': 
                                                                [
                                                                    {'expression': expression}
                                                                ],
                                                            'dimensions': 
                                                                [
                                                                    {'name': dimension}
                                                                ]
                                                        }
                                                    ]
                                                }
                                            ).execute()




    def channelTraffic(self):
        
        expression = 'ga:sessions'
        dimension = 'ga:channelGrouping'
        response   =  self.getReport(expression, dimension)
        self.parseAndPrint(response)    


    def channelConversion(self):
        
        expression = 'ga:goalCompletionsAll'
        dimension = 'ga:channelGrouping'
        response   =  self.getReport(expression, dimension)
        self.parseAndPrint(response)    


    def campaignTraffic(self):
        
        expression = 'ga:sessions'
        dimension = 'ga:campaign'
        response   =  self.getReport(expression, dimension)
        self.parseAndPrint(response)    


    def campaignConversion(self):
        
        expression = 'ga:goalCompletionsAll'
        dimension = 'ga:campaign'
        response   =  self.getReport(expression, dimension)
        self.parseAndPrint(response)    


    def referralTraffic(self):
        
        expression = 'ga:sessions'
        dimension = 'ga:fullReferrer'
        response   =  self.getReport(expression, dimension)
        self.parseAndPrint(response)    


    def referralConversion(self):
        
        expression = 'ga:goalCompletionsAll'
        dimension = 'ga:fullReferrer'
        response   =  self.getReport(expression, dimension)
        self.parseAndPrint(response)    

        
    def deviceTraffic(self):
        
        expression = 'ga:sessions'
        dimension = 'ga:deviceCategory'
        response   =  self.getReport(expression, dimension)
        self.parseAndPrint(response)    


    def deviceConversion(self):
        
        expression = 'ga:goalCompletionsAll'
        dimension = 'ga:deviceCategory'
        response   =  self.getReport(expression, dimension)
        self.parseAndPrint(response)    

    
    def genderTraffic(self):
        
        expression = 'ga:sessions'
        dimension = 'ga:userGender'
        response   =  self.getReport(expression, dimension)
        self.parseAndPrint(response)   
        

    def genderConversion(self):
        
        expression = 'ga:goalCompletionsAll'
        dimension = 'ga:userGender'
        response   =  self.getReport(expression, dimension)
        self.parseAndPrint(response)    



    def ageTraffic(self):
        
        expression = 'ga:sessions'
        dimension = 'ga:userAgeBracket'
        response   =  self.getReport(expression, dimension)
        self.parseAndPrint(response)   
        

    def ageConversion(self):
        
        expression = 'ga:goalCompletionsAll'
        dimension = 'ga:userAgeBracket'
        response   =  self.getReport(expression, dimension)
        self.parseAndPrint(response)    


