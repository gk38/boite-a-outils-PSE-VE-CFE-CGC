# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 10:53:13 2025

@author: gabri
"""


import streamlit as st



def calcul_conv(salaire,anc,age,classif):
    
    if classif=="A,B,C,D,E":
        if (anc<=10):
            indemnite=1/4*salaire/12*anc
        else:
            indemnite=1/4*salaire/12*10+1/3*salaire/12*(anc-10)
        
    else:
        if anc<=7:
            indemnite=1/5*salaire/12*anc
        else:
            indemnite=1/5*salaire/12*7+3/5*salaire/12*(anc-7)
        
    
    
    return indemnite


st.title("calcul indemnites conventionnelles")

salaire=st.number_input("Salaire annuel", key="salaire")
anc=st.number_input("ancienneté", key="anc")
age=st.number_input("age", key="age")
classif=st.selectbox("classification",["A,B,C,D,E","F,G,H"])

st.metric("montant conventionnelle",calcul_conv(salaire,anc,age,classif))