# Dwell time at each stop is different for all buses depending on their passenger OD table (Bus specific dwell time). 
# Note: Buses that do not have passenger OD table will have 100 seconds of dwell time for all stops.
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

vehicles = []
bus = []
step = 0
flags = []
countN = [] #count number of stops (Northboud)
done = []
y = 0
stop1done = 0
stop2done = 0
stop3done = 0
stop4done = 0
stop5done = 0
stop6done = 0
stop7done = 0
stop8done = 0
stop9done = 0
stop10done = 0
stop11done = 0
stop12done = 0
stop13done = 0
stop14done = 0
stop15done = 0
stop16done = 0
stop17done = 0
stop18done = 0
stop19done = 0
stop20done = 0
stop21done = 0
stop22done = 0
stop23done = 0
stop24done = 0
stop25done = 0
stop26done = 0
stop27done = 0
stop28done = 0
stop29done = 0
stop30done = 0
numOD = len(durationN1)     #number of OD table imported
defaultTime = 100000        #default dwell time for extra buses that does not have input OD matrix

# Begin Simulation
while traci.simulation.getMinExpectedNumber() > 0:
    sim_time = traci.simulation.getCurrentTime()

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
            print(flags)
            print(countN)
            print(done)
            if len(bus) <= numOD and countN[x] == 1:
                bus[x].setBusStopN1(durationN1[stop1done])
                stop1done += 1               
            if len(bus) <= numOD and countN[x] == 2:
                bus[x].setBusStopN2(durationN2[stop2done])
                stop2done += 1
            if len(bus) <= numOD and countN[x] == 3:
                bus[x].setBusStopN3(durationN3[stop3done])
                stop3done += 1
            if len(bus) <= numOD and countN[x] == 4:
                bus[x].setBusStopN4(durationN4[stop4done])
                stop4done += 1
            if len(bus) <= numOD and countN[x] == 5:
                bus[x].setBusStopN5(durationN5[stop5done])
                stop5done += 1
            if len(bus) <= numOD and countN[x] == 6:
                bus[x].setBusStopN6(durationN6[stop6done])
                stop6done += 1  
            if len(bus) <= numOD and countN[x] == 7:
                bus[x].setBusStopN7(durationN7[stop7done])
                stop7done += 1  
            if len(bus) <= numOD and countN[x] == 8:
                bus[x].setBusStopN8(durationN8[stop8done])
                stop8done += 1  
            if len(bus) <= numOD and countN[x] == 9:
                bus[x].setBusStopN9(durationN9[stop9done])
                stop9done += 1
            if len(bus) <= numOD and countN[x] == 10:
                bus[x].setBusStopN10(durationN10[stop10done])
                stop10done += 1  
            if len(bus) <= numOD and countN[x] == 11:
                bus[x].setBusStopN11(durationN11[stop11done])
                stop11done += 1  
            if len(bus) <= numOD and countN[x] == 12:
                bus[x].setBusStopN12(durationN12[stop12done])
                stop12done += 1
            if len(bus) <= numOD and countN[x] == 13:
                bus[x].setBusStopN13(durationN13[stop13done])
                stop13done += 1  
            if len(bus) <= numOD and countN[x] == 14:
                bus[x].setBusStopN14(durationN14[stop14done])
                stop14done += 1  
            if len(bus) <= numOD and countN[x] == 15:
                bus[x].setBusStopN15(durationN15[stop15done])
                stop15done += 1  
            if len(bus) <= numOD and countN[x] == 16:
                bus[x].setBusStopN16(durationN16[stop16done])
                stop16done += 1  
            if len(bus) <= numOD and countN[x] == 17:
                bus[x].setBusStopN17(durationN17[stop17done])
                stop17done += 1  
            if len(bus) <= numOD and countN[x] == 18:
                bus[x].setBusStopN18(durationN18[stop18done])
                stop18done += 1  
            if len(bus) <= numOD and countN[x] == 19:
                bus[x].setBusStopN19(durationN19[stop19done])
                stop19done += 1 
            if len(bus) <= numOD and countN[x] == 20:
                bus[x].setBusStopN20(durationN20[stop20done])
                stop20done += 1
            if len(bus) <= numOD and countN[x] == 21:
                bus[x].setBusStopN21(durationN21[stop21done])
                stop21done += 1 
            if len(bus) <= numOD and countN[x] == 22:
                bus[x].setBusStopN22(durationN22[stop22done])
                stop22done += 1 
            if len(bus) <= numOD and countN[x] == 23:
                bus[x].setBusStopN23(durationN23[stop23done])
                stop23done += 1 
            if len(bus) <= numOD and countN[x] == 24:
                bus[x].setBusStopN24(durationN24[stop24done])
                stop24done += 1 
            if len(bus) <= numOD and countN[x] == 25:
                bus[x].setBusStopN25(durationN25[stop25done])
                stop25done += 1 
            if len(bus) <= numOD and countN[x] == 26:
                bus[x].setBusStopN26(durationN26[stop26done])
                stop26done += 1 
            if len(bus) <= numOD and countN[x] == 27:
                bus[x].setBusStopN27(durationN27[stop27done])
                stop27done += 1 
            if len(bus) <= numOD and countN[x] == 28:
                bus[x].setBusStopN28(durationN28[stop28done])
                stop20done += 1 
            if len(bus) <= numOD and countN[x] == 29:
                bus[x].setBusStopN29(durationN29[stop29done])
                stop29done += 1    
            if len(bus) <= numOD and countN[x] == 30:
                bus[x].setBusStopN30(durationN30[stop30done])
                stop30done += 1
                done[x]=1
                y=sum(done)

            # For additional buses that do not have bus trip OD matrix as an input
            if len(bus) > numOD and countN[x] == 1:
                bus[x].setBusStopN1(durationN1 = defaultTime)
            if len(bus) > numOD and countN[x] == 2:
                bus[x].setBusStopN2(durationN2 = defaultTime)
            if len(bus) > numOD and countN[x] == 3:
                bus[x].setBusStopN3(durationN3 = defaultTime)
            if len(bus) > numOD and countN[x] == 4:
                bus[x].setBusStopN4(durationN4 = defaultTime)
            if len(bus) > numOD and countN[x] == 5:
                bus[x].setBusStopN5(durationN5 = defaultTime)
            if len(bus) > numOD and countN[x] == 6:
                bus[x].setBusStopN6(durationN6 = defaultTime)
            if len(bus) > numOD and countN[x] == 7:
                bus[x].setBusStopN7(durationN7 = defaultTime)
            if len(bus) > numOD and countN[x] == 8:
                bus[x].setBusStopN8(durationN8 = defaultTime)
            if len(bus) > numOD and countN[x] == 9:
                bus[x].setBusStopN9(durationN9 = defaultTime)
            if len(bus) > numOD and countN[x] == 10:
                bus[x].setBusStopN10(durationN10 = defaultTime)
            if len(bus) > numOD and countN[x] == 11:
                bus[x].setBusStopN11(durationN11 = defaultTime)
            if len(bus) > numOD and countN[x] == 12:
                bus[x].setBusStopN12(durationN12 = defaultTime)
            if len(bus) > numOD and countN[x] == 13:
                bus[x].setBusStopN13(durationN13 = defaultTime)
            if len(bus) > numOD and countN[x] == 14:
                bus[x].setBusStopN14(durationN14 = defaultTime)
            if len(bus) > numOD and countN[x] == 15:
                bus[x].setBusStopN15(durationN15 = defaultTime)
            if len(bus) > numOD and countN[x] == 16:
                bus[x].setBusStopN16(durationN16 = defaultTime)
            if len(bus) > numOD and countN[x] == 17:
                bus[x].setBusStopN17(durationN17 = defaultTime)
            if len(bus) > numOD and countN[x] == 18:
                bus[x].setBusStopN18(durationN18 = defaultTime)
            if len(bus) > numOD and countN[x] == 19:
                bus[x].setBusStopN19(durationN19 = defaultTime)
            if len(bus) > numOD and countN[x] == 20:
                bus[x].setBusStopN20(durationN20 = defaultTime)
            if len(bus) > numOD and countN[x] == 21:
                bus[x].setBusStopN21(durationN21 = defaultTime)
            if len(bus) > numOD and countN[x] == 22:
                bus[x].setBusStopN22(durationN22 = defaultTime)
            if len(bus) > numOD and countN[x] == 23:
                bus[x].setBusStopN23(durationN23 = defaultTime)
            if len(bus) > numOD and countN[x] == 24:
                bus[x].setBusStopN24(durationN24 = defaultTime)
            if len(bus) > numOD and countN[x] == 25:
                bus[x].setBusStopN25(durationN25 = defaultTime)
            if len(bus) > numOD and countN[x] == 26:
                bus[x].setBusStopN26(durationN26 = defaultTime)
            if len(bus) > numOD and countN[x] == 27:
                bus[x].setBusStopN27(durationN27 = defaultTime)
            if len(bus) > numOD and countN[x] == 28:
                bus[x].setBusStopN28(durationN28 = defaultTime)
            if len(bus) > numOD and countN[x] == 29:
                bus[x].setBusStopN29(durationN29 = defaultTime)
            if len(bus) > numOD and countN[x] == 30:
                bus[x].setBusStopN30(durationN30 = defaultTime)
                done[x]=1
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