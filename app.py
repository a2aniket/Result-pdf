# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 19:34:07 2020

@author: NEXUS
"""
from flask import Flask,render_template
from datamining.dataMining import DataMining as dm

app=Flask("__name__")

@app.route("/",methods=["GET","POST"])
def Home():
    dm.text_mining()
    return render_template("Home.html")


              



app.run(debug=True)