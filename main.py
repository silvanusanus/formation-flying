# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 16:11:47 2021

@author: z.li
"""

from framework import Framework
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

# simulation parameters
dt = 0.01
t = 15
T = 100 
MC_RUNS = 50
ITR = int(t/dt)

"""
target configurations: {'square', 'pentagon', 'hexagon'}
stress matrix solvers: {'opt', 'LMI'}
estimators: {'MLE','MMSE','Edge_KF'}
"""

# when timing the computation time, better comment out the target.evaluate()
error_MLE = np.zeros((MC_RUNS,ITR))
error_MMSE = np.zeros((MC_RUNS,ITR))
error_KF = np.zeros((MC_RUNS,ITR))

# MLE
start = datetime.now()
target = Framework('square', 'LMI', T, dt, t)
for r in range(MC_RUNS):
    target.run(estimator='MLE')
    error_MLE[r,:] = target.evaluate()
elapse = datetime.now()
time_MLE = elapse-start

mean_error_MLE = np.mean(error_MLE,axis=0)
std_error_MLE = np.std(error_MLE,axis=0)
time_MLE = time_MLE/MC_RUNS
plt.plot(mean_error_MLE)
plt.plot(std_error_MLE)
plt.title('MLE')
plt.show()


"""
# MMSE
start = datetime.now()
target = Framework('square', 'LMI', T, dt, t)
for r in range(MC_RUNS):
    target.run(estimator='MMSE')
    error_MMSE[r,:] = target.evaluate()
elapse = datetime.now()
time_MMSE = elapse-start

mean_error_MMSE = np.mean(error_MMSE,axis=0)
std_error_MMSE = np.std(error_MMSE,axis=0)
time_MMSE = time_MMSE/MC_RUNS
plt.plot(mean_error_MMSE)
plt.plot(std_error_MMSE)
plt.title('MMSE')
plt.show()
    
# KF
start = datetime.now()
target = Framework('square', 'LMI', T, dt, t)
for r in range(MC_RUNS):
    target.run(estimator='Edge_KF')
    error_KF[r,:] = target.evaluate()
elapse = datetime.now()
time_KF = elapse-start

mean_error_KF = np.mean(error_KF,axis=0)
std_error_KF = np.std(error_KF,axis=0)
time_KF = time_KF/MC_RUNS
plt.plot(mean_error_KF)
plt.plot(std_error_KF)
plt.title('KF')
plt.show()

plt.bar(['MLE','MMSE','KF'],[time_MLE.total_seconds(),time_MMSE.total_seconds(),time_KF.total_seconds()])
"""