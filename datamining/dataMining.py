# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 19:31:34 2020

@author: Aniket
"""
import pdfplumber
from regex.text_extraction import TextExtraction as tx
import pandas as pd

class DataMining:
    """extraction of data from the pdf"""
    def text_mining():
        """ get valuble text from the pdf"""
        
        # open pdf file
        with pdfplumber.open('data/source/one.pdf') as pdf:
            first_page = pdf.pages[0]
            #extract text from pdf file
            text=first_page.extract_text()
            extracted_data=tx.textExtraction(text)
            file_name=extracted_data["prn"]
            #data to csv
            extracted_data=[extracted_data]
            dataFrame=pd.DataFrame(extracted_data)
            dataFrame.to_csv("output/"+file_name+".csv")
            
            
              

