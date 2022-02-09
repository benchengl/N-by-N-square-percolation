import numpy as np
import math
from random import random
import pandas as pd
import matplotlib.pyplot as plt


def createVoltage(n):
  voltage=np.zeros((n+3,n+3),dtype=float)
  voltage[1:n+2,1]=1
  return voltage

def createHr(n):
  hr=np.zeros((n+3,n+2))
  hr[0:n+3,0:n+2]=math.inf
  i=1
  while i<n+2:
    j=1
    while j<n+1:
      v=random()
      if v<0.5:
        hr[i][j]=1
      else:
        hr[i][j]=math.inf
      j+=1
    i+=1
  return hr

def createVr(n):
  vr=np.zeros((n+2,n+3))
  vr[0:n+2,0:n+3]=math.inf
  vr[1:n+1,1]=0
  vr[1:n+1,n+1]=0
  i=1
  while i<n+1:
    j=2
    while j<n+1:
      v=random()
      if v<0.5:
        vr[i][j]=1
      else:
        vr[i][j]=math.inf
      j+=1
    i+=1
  return vr

  
def computeVoltage(voltage,hr,vr,i,j):
  if hr[i][j-1]!=math.inf and hr[i][j]!=math.inf and vr[i-1][j]!=math.inf and vr[i][j]!=math.inf:
    voltage[i][j]=(hr[i][j-1]*hr[i][j]*(voltage[i-1][j]*vr[i][j]+voltage[i+1][j]*vr[i-1][j]))/(hr[i][j-1]*hr[i][j]*(vr[i][j]+vr[i-1][j])+vr[i-1][j]*vr[i][j]*(hr[i][j]+hr[i][j-1]))+(vr[i-1][j]*vr[i][j]*(voltage[i][j-1]*hr[i][j]+voltage[i][j+1]*hr[i][j-1]))/(hr[i][j-1]*hr[i][j]*(vr[i][j]+vr[i-1][j])+vr[i-1][j]*vr[i][j]*(hr[i][j]+hr[i][j-1]))
  elif hr[i][j-1]==math.inf and hr[i][j]!=math.inf and vr[i-1][j]!=math.inf and vr[i][j]!=math.inf:
    voltage[i][j]=(voltage[i-1][j]*hr[i][j]*vr[i][j]+voltage[i][j+1]*vr[i-1][j]*vr[i][j]+voltage[i+1][j]*vr[i-1][j]*hr[i][j])/(vr[i-1][j]*hr[i][j]+vr[i-1][j]*vr[i][j]+hr[i][j]*vr[i][j])
  elif hr[i][j-1]!=math.inf and hr[i][j]==math.inf and vr[i-1][j]!=math.inf and vr[i][j]!=math.inf:
    voltage[i][j]=(voltage[i-1][j]*hr[i][j-1]*vr[i][j]+voltage[i][j-1]*vr[i-1][j]*vr[i][j]+voltage[i+1][j]*vr[i-1][j]*hr[i][j-1])/(vr[i-1][j]*hr[i][j-1]+vr[i-1][j]*vr[i][j]+hr[i][j-1]*vr[i][j])
  elif hr[i][j-1]!=math.inf and hr[i][j]!=math.inf and vr[i-1][j]==math.inf and vr[i][j]!=math.inf:
    voltage[i][j]=(voltage[i+1][j]*hr[i][j-1]*hr[i][j]+voltage[i][j-1]*vr[i][j]*hr[i][j]+voltage[i][j+1]*vr[i][j]*hr[i][j-1])/(vr[i][j]*hr[i][j-1]+vr[i][j]*hr[i][j]+hr[i][j-1]*hr[i][j])
  elif hr[i][j-1]!=math.inf and hr[i][j]!=math.inf and vr[i-1][j]!=math.inf and vr[i][j]==math.inf:
    voltage[i][j]=(voltage[i-1][j]*hr[i][j-1]*hr[i][j]+voltage[i][j-1]*vr[i-1][j]*hr[i][j]+voltage[i][j+1]*vr[i-1][j]*hr[i][j-1])/(vr[i-1][j]*hr[i][j-1]+vr[i-1][j]*hr[i][j]+hr[i][j-1]*hr[i][j])
  elif hr[i][j-1]==math.inf and hr[i][j]==math.inf and vr[i-1][j]!=math.inf and vr[i][j]!=math.inf:
    voltage[i][j]=(voltage[i-1][j]*vr[i][j]+voltage[i+1][j]*vr[i-1][j])/(vr[i-1][j]+vr[i][j])
  elif hr[i][j-1]==math.inf and hr[i][j]!=math.inf and vr[i-1][j]==math.inf and vr[i][j]!=math.inf:
    voltage[i][j]=(voltage[i+1][j]*hr[i][j]+voltage[i][j+1]*vr[i][j])/(hr[i][j]+vr[i][j])
  elif hr[i][j-1]==math.inf and hr[i][j]!=math.inf and vr[i-1][j]!=math.inf and vr[i][j]==math.inf:
    voltage[i][j]=(voltage[i-1][j]*hr[i][j]+voltage[i][j+1]*vr[i-1][j])/(hr[i][j]+vr[i-1][j])
  elif hr[i][j-1]!=math.inf and hr[i][j]==math.inf and vr[i-1][j]==math.inf and vr[i][j]!=math.inf:
    voltage[i][j]=(voltage[i][j-1]*vr[i][j]+voltage[i+1][j]*hr[i][j-1])/(hr[i][j-1]+vr[i][j])
  elif hr[i][j-1]!=math.inf and hr[i][j]==math.inf and vr[i-1][j]!=math.inf and vr[i][j]==math.inf:
    voltage[i][j]=(voltage[i][j-1]*vr[i-1][j]+voltage[i-1][j]*hr[i][j-1])/(hr[i][j-1]+vr[i-1][j])
  elif hr[i][j-1]!=math.inf and hr[i][j]!=math.inf and vr[i-1][j]==math.inf and vr[i][j]==math.inf:
    voltage[i][j]=(voltage[i][j-1]*hr[i][j]+voltage[i][j+1]*hr[i][j-1])/(hr[i][j-1]+hr[i][j])
  elif hr[i][j-1]==math.inf and hr[i][j]==math.inf and vr[i-1][j]==math.inf and vr[i][j]!=math.inf:
    voltage[i][j]=voltage[i+1][j]
  elif hr[i][j-1]!=math.inf and hr[i][j]==math.inf and vr[i-1][j]==math.inf and vr[i][j]==math.inf:
    voltage[i][j]=voltage[i][j-1]
  elif hr[i][j-1]==math.inf and hr[i][j]!=math.inf and vr[i-1][j]==math.inf and vr[i][j]==math.inf:
    voltage[i][j]=voltage[i][j+1]
  elif hr[i][j-1]==math.inf and hr[i][j]==math.inf and vr[i-1][j]!=math.inf and vr[i][j]==math.inf:
    voltage[i][j]=voltage[i-1][j]
  elif hr[i][j-1]==math.inf and hr[i][j]==math.inf and vr[i-1][j]==math.inf and vr[i][j]==math.inf:
    voltage[i][j]=0
  return voltage[i][j]

def fix(voltage,n):
  voltage[1:n+2,1]=1
  voltage[1:n+2,n+1]=0
  return voltage

def updateVoltage(voltage,hr,vr,n,m):
  a=1
  while a<m+1:
    i=1
    while i<n+2:
      j=2
      while j<n+1:
        if (i+j)%2==1:
          computeVoltage(voltage,hr,vr,i,j)
          fix(voltage,n)
        elif (i+j)%2==0:
          computeVoltage(voltage,hr,vr,i,j)
          fix(voltage,n)
        j+=1
      i+=1
    a+=1
  #print("After "+str(m)+" iterations, voltage matrix is")
  return voltage

a=1
errortimes=0
sumR=0
Rlist=[]
while a<401:
  Hr=createHr(3)
  Vr=createVr(3)
  voltage=updateVoltage(createVoltage(3),Hr,Vr,3,200)

  #print(voltage)
  b=1
  singlesumCurrent=0
  singlesumFC=0
  while b<5: 
    if voltage[b][3]-voltage[b][4]<0.01 or 1-voltage[b][3]+voltage[b][4]<0.01:
      singlesumCurrent+=0
    else:
      singlesumCurrent+=voltage[b][3]-voltage[b][4]
    singlesumFC+=voltage[b][1]-voltage[b][2]
    b+=1
  if singlesumCurrent==0:
    errortimes+=1
    #print("Error")
  else:
    #print(singlesumFC)
    sumR+=(1/singlesumFC)
    Rlist.append(1/singlesumFC)
  a+=1
print("Error times is "+str(errortimes))
print("Mean resistance is "+str(sumR/(400-errortimes)))
plt.hist(Rlist, bins=40)
plt.show()
