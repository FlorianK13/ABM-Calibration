#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 10:10:59 2020

@author: flo
"""

import numpy as np

def P_gauss(x,sigma=0.7):
    return sigma**2/np.exp(-1/2*sigma**2)*(np.exp(-x**2/(2*sigma**2))-np.exp(-1/(2*sigma**2)))

def SimpleOpinionStep(Opinion,t,D=P_gauss):
    eta=np.random.uniform(-.1,.3,size=len(Opinion[0]))
    Opinion[t]=Opinion[t-1]+eta*D(Opinion[t-1])
    return Opinion




def MakeAgentArray(Countypd,Agent_Scale):

    
    AgentsPerCity=np.round(np.array(Countypd["number agents"])*Agent_Scale)

    Number_Agents=int(AgentsPerCity.sum())
    Agent_Array=np.zeros((Number_Agents,3)).transpose()
    Agent_Array[0]=np.arange(Number_Agents)   # Give a number to each agent
    Agent_Array=Agent_Array.transpose()


    # Here the Landkreis number is given to each agent
    Ag_index=0
    for index,town in enumerate(AgentsPerCity):
        for n in range(int(town)):
            try:
                Agent_Array[Ag_index][1]=index
                Ag_index+=1
            except:
                print(Ag_index)
                break
            
    

    Agent_Array=Agent_Array.astype(int)
    Agent_Array=Agent_Array.transpose()


    
    return Agent_Array.transpose()

def Load_PVData():
    Savename=f"../data/Timemat_Landkreis_PVCap_OnlyAnzahl_2000-2018"
    Timemat=np.load(Savename+".npy")
    
    Timemat_yearly=np.zeros((19,len(Timemat)))
    Timemat_yearly_kumm=np.zeros((19,len(Timemat)))


    for i in range(19):
        Timemat_yearly[i]=Timemat.transpose()[12*i:12*i+12].sum(axis=0)
        Timemat_yearly_kumm[i:]+=Timemat.transpose()[12*i:12*i+12].sum(axis=0)
    
    return Timemat_yearly,Timemat_yearly_kumm
