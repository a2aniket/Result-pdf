# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 19:42:59 2020

@author: NEXUS
"""

import re

class TextExtraction:
    def textExtraction(text):
        #get name
        set_no=re.search(r"SeatNo *: *([a-zA-Z0-9]*)",text)
        # center code
        center=re.search(r"Centre*: *([0-9]*)",text)
        #prn number
        prn=re.search(r"57 Perm Reg No\(PRN\) *: *([a-zA-z0-9]*)",text)
        #student name
        name=re.search('Student Name : (\w+\s\w+\s\w+)', text)
        #mother name
        mother_name=re.search(r"Mother Name *: *([a-zA-Z]*)",text)
        
        #marks
        marks=re.findall("[0-9]{6}.*",text)
        final={
                "set_no":set_no.group(1),
                "prn":prn.group(1),
                "name":name.group(1),
                "mother_name":mother_name.group(1)
                }
        
        for i in range(1,21):
            result=re.search("([0-9A-Z]{6,7})* ([a-zA-Z &.]*) * ([0-9#]{1,2}) * ([A-Z+]{1,2}) * ([0-9]{2})",marks[i])
            subject_code=result.group(1)
            subject_name=result.group(2)
            cred=result.group(3)
            grd=result.group(4)
            gp=result.group(5)

        final[f"{subject_name}"]=gp
        return final