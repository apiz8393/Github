# Dwell time at each stop is the same for all buses if it happens to stop at the same time period (Average dwell time). 
# Note: Currently we only have 2 periods of time, before 1000 sec and after 1000 sec.
# Load libraries
import os
import sys
import pandas as pd

from pandas import ExcelWriter
from pandas import ExcelFile

# Set the configuration file for sumo and simulation label
config_file = "C:/Users/MohammadHafiz/Desktop/Cummins/cmax/cmax.sumocfg"
label = "sim1"

df = pd.read_excel('C:/Users/MohammadHafiz/Desktop/Cummins/OD.xlsx', sheetname='Sheet2')
durationN1=(df['Stop1'])
durationN2=(df['Stop2'])
durationN3=(df['Stop3'])
durationN4=(df['Stop4'])
durationN5=(df['Stop5'])
durationN6=(df['Stop6'])
durationN7=(df['Stop7'])
durationN8=(df['Stop8'])
durationN9=(df['Stop9'])
durationN10=(df['Stop10'])
durationN11=(df['Stop11'])
durationN12=(df['Stop12'])
durationN13=(df['Stop13'])
durationN14=(df['Stop14'])
durationN15=(df['Stop15'])
durationN16=(df['Stop16'])
durationN17=(df['Stop17'])
durationN18=(df['Stop18'])
durationN19=(df['Stop19'])
durationN20=(df['Stop20'])
durationN21=(df['Stop21'])
durationN22=(df['Stop22'])
durationN23=(df['Stop23'])
durationN24=(df['Stop24'])
durationN25=(df['Stop25'])
durationN26=(df['Stop26'])
durationN27=(df['Stop27'])
durationN28=(df['Stop28'])
durationN29=(df['Stop29'])
durationN30=(df['Stop30'])

if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("please declare environment variable 'SUMO_HOME'")
import traci

from Vehicle import Vehicle

# Start TraCI GUI
traci.start(["sumo-gui", "-c", config_file, "--step-length", "1.0"], label=label)

# Parameters
vehicles = []
bus = []
step = 0
flags = []
countN = [] #count number of stops (Northboud)
done = []
y = 0
period = 0

# Begin Simulation
while traci.simulation.getMinExpectedNumber() > 0:
    sim_time = traci.simulation.getCurrentTime()
    if sim_time > 1000000:
    	period = 1

    # Add new bus fo every 500 seconds
    if sim_time % 500000 == 0:
        newVehicle = Vehicle(traci)
        vehicles.append(newVehicle)
        print("BusB is added")
    
    # New vector to keep track bus added
        busAdded = newVehicle
        bus.append(busAdded)
        countN.append(0)
        flags.append(0)
        done.append(0)

    # Add new car for every 10 seconds
    if sim_time % 10000 == 0:
        newVehicle = Vehicle(traci,type="CarA",routeID="route01")
        vehicles.append(newVehicle)
        print("CarA is added")
    
    # Change stop durations for all northbound stops
    for x in range (y,len(bus)):        #to run simulation even bus left network
        if (bus[x].isStopped()) == True and flags[x] == 0 and done[x] == 0:
            flags[x] = 1
            countN[x] += 1
            # print(y)
            # print(len(bus))
            # print(flags)
            # print(countN)
            # print(done)
            if countN[x] == 1:
                bus[x].setBusStopN1(durationN1[period])
            if countN[x] == 2:
                bus[x].setBusStopN2(durationN2[period])
            if countN[x] == 3:
                bus[x].setBusStopN3(durationN3[period])
            if countN[x] == 4:
                bus[x].setBusStopN4(durationN4[period])
            if countN[x] == 5:
                bus[x].setBusStopN5(durationN5[period])
            if countN[x] == 6:
                bus[x].setBusStopN6(durationN6[period])
            if countN[x] == 7:
                bus[x].setBusStopN7(durationN7[period])
            if countN[x] == 8:
                bus[x].setBusStopN8(durationN8[period])
            if countN[x] == 9:
                bus[x].setBusStopN9(durationN9[period])
            if countN[x] == 10:
                bus[x].setBusStopN10(durationN10[period])
            if countN[x] == 11:
                bus[x].setBusStopN11(durationN11[period])
            if countN[x] == 12:
                bus[x].setBusStopN12(durationN12[period])
            if countN[x] == 13:
                bus[x].setBusStopN13(durationN13[period])
            if countN[x] == 14:
                bus[x].setBusStopN14(durationN14[period])
            if countN[x] == 15:
                bus[x].setBusStopN15(durationN15[period])
            if countN[x] == 16:
                bus[x].setBusStopN16(durationN16[period])    
            if countN[x] == 17:
                bus[x].setBusStopN17(durationN17[period])
            if countN[x] == 18:
                bus[x].setBusStopN18(durationN18[period])
            if countN[x] == 19:
                bus[x].setBusStopN19(durationN19[period])
            if countN[x] == 20:
                bus[x].setBusStopN20(durationN20[period])
            if countN[x] == 21:
                bus[x].setBusStopN21(durationN21[period])
            if countN[x] == 22:
                bus[x].setBusStopN22(durationN22[period])
            if countN[x] == 23:
                bus[x].setBusStopN23(durationN23[period])
            if countN[x] == 24:
                bus[x].setBusStopN24(durationN24[period])
            if countN[x] == 25:
                bus[x].setBusStopN25(durationN25[period])
            if countN[x] == 26:
                bus[x].setBusStopN26(durationN26[period])
            if countN[x] == 27:
                bus[x].setBusStopN27(durationN27[period])
            if countN[x] == 28:
                bus[x].setBusStopN28(durationN28[period])
            if countN[x] == 29:
                bus[x].setBusStopN29(durationN29[period])
            if countN[x] == 30:
                bus[x].setBusStopN30(durationN30[period])
                y=sum(done)
        	 
        if (bus[x].isStopped()) == False and flags[x] == 1:
        	flags[x] = 0
    
    # Print steps and vehicle location
    print "step", step 
    # print traci.vehicle.getSubscriptionResults()
    # print sim_time
    # print vehicles
    step += 1

    newVehicle=0

    # Step once in the simulation
    traci.simulationStep()