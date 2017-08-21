import shortuuid
import traci.constants as tc

class Vehicle(object): 
    def __init__(self, traci, routeID="busroute01", type="BusB", departLane="1", line="1"):
        self.id = shortuuid.uuid()
        self.traci = traci
        self.type= type


        traci.vehicle.addFull(vehID=self.id, routeID=routeID, typeID=type, departLane=departLane, line=line)
        traci.vehicle.subscribe(self.id, (tc.VAR_ROAD_ID, tc.VAR_LANEPOSITION, tc.VAR_SPEED))


    def getSpeed(self):
        return self.traci.vehicle.getSpeed(self.id)

    def getType(self):
        return self.type

    # def getRouteID(self):
    # 	return self.traci.vehicle.getRouteID(self.id)

    # def getStopState(self):
    # 	return self.traci.vehicle.getStopState(self.id)


    def isStopped(self):
    	return self.traci.vehicle.isStopped(self.id)

    def setBusStopN1(self,durationN1):
    	return self.traci.vehicle.setBusStop(self.id, "BusStop_1_N_Rich", durationN1, until=-1, flags=0)

    def setBusStopN2(self,durationN2):
    	return self.traci.vehicle.setBusStop(self.id, "BusStop_2_N_Broad", durationN2, until=-1, flags=0)

    def setBusStopN3(self,durationN3):
    	return self.traci.vehicle.setBusStop(self.id, "BusStop_3_N_Gay", durationN3, until=-1, flags=0)

    def setBusStopN4(self,durationN4):
    	return self.traci.vehicle.setBusStop(self.id, "BusStop_4_N_Nationwide", durationN4, until=-1, flags=0)

    def setBusStopN5(self,durationN5):
    	return self.traci.vehicle.setBusStop(self.id, "BusStop_5_N_Naghten", durationN5, until=-1, flags=0)

    def setBusStopN6(self,durationN6):
        return self.traci.vehicle.setBusStop(self.id, "BusStop_6_N_Vernon", durationN6, until=-1, flags=0)

    def setBusStopN7(self,durationN7):
        return self.traci.vehicle.setBusStop(self.id, "BusStop_7_N_Abbott", durationN7, until=-1, flags=0)

    def setBusStopN8(self,durationN8):
        return self.traci.vehicle.setBusStop(self.id, "BusStop_8_N_2nd", durationN8, until=-1, flags=0)

    def setBusStopN9(self,durationN9):
        return self.traci.vehicle.setBusStop(self.id, "BusStop_9_N_5th", durationN9, until=-1, flags=0)

    def setBusStopN10(self,durationN10):
        return self.traci.vehicle.setBusStop(self.id, "BusStop_10_N_11th", durationN10, until=-1, flags=0)

    def setBusStopN11(self,durationN11):
        return self.traci.vehicle.setBusStop(self.id, "BusStop_11_N_17th", durationN11, until=-1, flags=0)

    def setBusStopN12(self,durationN12):
        return self.traci.vehicle.setBusStop(self.id, "BusStop_12_N_25th", durationN12, until=-1, flags=0)

    def setBusStopN13(self,durationN13):
        return self.traci.vehicle.setBusStop(self.id, "BusStop_13_N_Hudson", durationN13, until=-1, flags=0)

    def setBusStopN14(self,durationN14):
        return self.traci.vehicle.setBusStop(self.id, "BusStop_14_N_Genessee", durationN14, until=-1, flags=0)

    def setBusStopN15(self,durationN15):
        return self.traci.vehicle.setBusStop(self.id, "BusStop_15_N_Weber", durationN15, until=-1, flags=0)

    def setBusStopN16(self,durationN16):
        return self.traci.vehicle.setBusStop(self.id, "BusStop_16_N_OaklandPark", durationN16, until=-1, flags=0)

    def setBusStopN17(self,durationN17):
        return self.traci.vehicle.setBusStop(self.id, "BusStop_17_N_Huy", durationN17, until=-1, flags=0)

    def setBusStopN18(self,durationN18):
        return self.traci.vehicle.setBusStop(self.id, "BusStop_18_N_Elmore", durationN18, until=-1, flags=0)

    def setBusStopN19(self,durationN19):
        return self.traci.vehicle.setBusStop(self.id, "BusStop_19_N_Pegg", durationN19, until=-1, flags=0)

    def setBusStopN20(self,durationN20):
        return self.traci.vehicle.setBusStop(self.id, "BusStop_20_N_MorseCreek", durationN20, until=-1, flags=0)

    def setBusStopN21(self,durationN21):
        return self.traci.vehicle.setBusStop(self.id, "BusStop_21_N_Morse", durationN21, until=-1, flags=0)

    def setBusStopN22(self,durationN22):
        return self.traci.vehicle.setBusStop(self.id, "BusStop_22_N_Wallcrest", durationN22, until=-1, flags=0)

    def setBusStopN23(self,durationN23):
        return self.traci.vehicle.setBusStop(self.id, "BusStop_23_N_BlendonWoods", durationN23, until=-1, flags=0)

    def setBusStopN24(self,durationN24):
        return self.traci.vehicle.setBusStop(self.id, "BusStop_24_N_CommunityPark", durationN24, until=-1, flags=0)

    def setBusStopN25(self,durationN25):
        return self.traci.vehicle.setBusStop(self.id, "BusStop_25_N_CopperShrock", durationN25, until=-1, flags=0)

    def setBusStopN26(self,durationN26):
        return self.traci.vehicle.setBusStop(self.id, "BusStop_26_N_StAnns", durationN26, until=-1, flags=0)

    def setBusStopN27(self,durationN27):
        return self.traci.vehicle.setBusStop(self.id, "BusStop_27_N_MainSt", durationN27, until=-1, flags=0)

    def setBusStopN28(self,durationN28):
        return self.traci.vehicle.setBusStop(self.id, "BusStop_28_N_Westar", durationN28, until=-1, flags=0)

    def setBusStopN29(self,durationN29):
        return self.traci.vehicle.setBusStop(self.id, "BusStop_29_N_PolarisClev", durationN29, until=-1, flags=0)

    def setBusStopN30(self,durationN30):
        return self.traci.vehicle.setBusStop(self.id, "BusStop_30_N_OhioHealth", durationN30, until=-1, flags=0)

    def setBusStopN31(self,durationN31):
        return self.traci.vehicle.setBusStop(self.id, "BusStop_31_N_Last", durationN31, until=-1, flags=0)
