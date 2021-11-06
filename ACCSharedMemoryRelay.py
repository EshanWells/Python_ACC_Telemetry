"""

"""

from ctypes import *
import mmap

class SPageFilePhysics(Structure):                  #changes at graphic step
    _fields_ = [
		("yPacketID",               c_int),
		("rGas",                    c_float),
		("rBrake",                  c_float),
		("wFuel",                   c_float),
		("NGear",                   c_int),
		("nRPM",                    c_int),
		("aSteerInput",             c_float),
		("vSpeed",                  c_float),
		("vVelGlobal",              c_float * 3),
		("gAccGlobal",              c_float * 3),
		("rWheelSlip",              c_float * 4),
		("FWheelLoad",              c_float * 4),   #not used in ACC
		("pTyrePressure",           c_float * 4),
		("nWheelAngularSpeed",      c_float * 4),
		("rTyreWear",               c_float * 4),   #not used in ACC
		("rTyreDirtyLevel",         c_float * 4),   #not used in ACC
		("TTyreCoreTemperature",    c_float * 4),
		("aCamberRAD",              c_float * 4),   #not used in ACC
		("xSuspensionTravel",       c_float * 4),
		("BDRS",                    c_float),       #not used in ACC
		("BTC",                     c_float),
		("aHeading",                c_float),
		("aPitch",                  c_float),
		("aRoll",                   c_float),
		("xCGHeight",               c_float),       #not used in ACC
		("rCarDamage",              c_float * 5),
		("numberOfTyresOut",        c_int),         #not used in ACC
		("BPitLimiter",             c_int),
		("BABS",                    c_float),
		("fKERSCharge",             c_float),       #not used in ACC
		("zKERSInput",              c_float),       #not used in ACC
		("BAutoShifter",            c_int),
		("xRideHeight",             c_float * 2),   #not used in ACC
		("pTurboBoost",             c_float),
		("WBallast",                c_float),       #not used in ACC
		("zAirDensity",             c_float),       #not used in ACC
		("TAir",                    c_float),
		("TRoad",                   c_float),
		("nLocalAngularVel",        c_float * 3),
		("zFinalFF",                c_float),
		("zperformanceMeter",       c_float),       #not used in ACC
		("zEngineBrake",            c_int),         #not used in ACC
		("zERSRecoveryLevel",       c_int),         #not used in ACC
		("zERSPowerLevel",          c_int),         #not used in ACC
		("zERSHeatCharging",        c_int),         #not used in ACC
		("zERSIsCharging",          c_int),         #not used in ACC
		("zKERSCurrentKJ",          c_float),       #not used in ACC
		("BDRSAvailable",           c_int),         #not used in ACC
		("BDRSEnabled",             c_int),         #not used in ACC
		("TBrakeTemp",              c_float * 4),
		("rClutch",                 c_float),
		("TTyreTempI",              c_float * 4),   #not used in ACC
		("TTyreTempM",              c_float * 4),   #not used in ACC
		("TTyreTempO",              c_float * 4),   #not used in ACC
		("BAIControlled",           c_int),
		("CTyreContactPoint",       c_float * 4 * 3),
		("CTyreContactNormal",      c_float * 4 * 3),
		("CTyreContactHeading",     c_float * 4 * 3),
		("rBrakeBias",              c_float),
		("vLocalVelocity",          c_float * 3),
		("zP2PActivations",         c_int),         #not used in ACC
		("zP2PStatus",              c_int),         #not used in ACC
		("nCurrentMaxRpm",          c_int),         #not used in ACC
		("zmz",                     c_float * 4),   #not used in ACC
		("zfx",                     c_float * 4),   #not used in ACC
		("zfy",                     c_float * 4),   #not used in ACC
		("rSlipRatio",              c_float * 4),
		("aSlipAngle",              c_float * 4),
		("BTCinAction",             c_int),         #not used in ACC
		("BABSInAction",            c_int),         #not used in ACC
		("zSuspensionDamage",       c_float * 4),   #not used in ACC
		("TTyre",                   c_float * 4),   #not used in ACC
        ("TWater",                  c_float),
        ("pBrake",                  c_float * 4),
        ("NFrontBrakeCompound",     c_int),
        ("NRearBrakeCompound",      c_int),
        ("rPadLife",                c_float * 4),
        ("rDiscLife",               c_float * 4)
        ("BIgnitionSwitch",         c_int),
        ("BStarterSwitch",          c_int),
        ("zKerbVibration",          c_float),
        ("zSlipVibrations",         c_float),
        ("zgVibrations",            c_float),
        ("zABSVibrations",          c_float)
	]

class SPageFileGraphic(Structure):                  #changes at graphic step
    _fields_ = [
		("yPacketId",               c_int),
		("yAC_STATUS",              c_int),         #enum acc status
		("yAC_SESSION_TYPE",        c_int),         #enum acc session type
		("tCurrentTime",            c_wchar * 15),
		("tLastTime",               c_wchar * 15),
		("tBestTime",               c_wchar * 15),
		("tSplit",                  c_wchar * 15),
		("NCompletedLaps",          c_int),
		("NPosition",               c_int),
		("tCurrentTimeMs",          c_int),
		("tLastTimeMs",             c_int),
		("tBestTimeMs",             c_int),
		("tSessionTimeLeft",        c_float),
		("sDistanceTraveled",       c_float),
		("BInPit",                  c_int),
		("NCurrentSectorIndex",     c_int),
		("tLastSectorTimeMs",       c_int),
		("NNumberOfLaps",           c_int),
		("yTyreCompound",           c_wchar * 33),
		("zReplayTimeMultiplier",   c_float),       #not used in ACC
		("sNormalizedCarPosition",  c_float),
		("NActiveCars",             c_int),
		("CCarCoordinates",         c_float * 60 * 3),
		("yCarID",                  c_int * 60),
		("yPlayerCarID",            c_int),
		("tPenaltyTime",            c_float),
		("NFlag",                   c_int),
		("NPenalty",                c_int),
		("BIdealLineOn",            c_int),
		("BIsInPitLane",            c_int),
		("rSurfaceGrip",            c_float),       #always returns 0. Use as error check.
		("BMandatoryPitDone",       c_int),
		("vWindSpeed",              c_float),
		("aWindDirection",          c_float),
		("BSetupMenuVisible",       c_int),
		("NMainDisplayIndex",       c_int),         #appendix 1
		("NSecondaryDisplayIndex",  c_int),
		("NTC",                     c_int),
		("NTCCut",                  c_int),
		("NEngineMap",              c_int),
		("NABS",                    c_int),
		("lFuelXLap",               c_int),
		("BRainLights",             c_int),
		("BFlashingLights",         c_int),
		("NLightsStage",            c_int),
		("TExhaustTemperature",     c_float),
		("NWiperStage",             c_int),
		("tStintTotalTimeLeft",     c_int),
		("tStintTimeLeft",          c_int),
		("BRainTyres",              c_int),
        ("NSessionIndex",           c_int),
        ("LUsedFuel",               c_float),
        ("tDeltaLapTime",           c_wchar * 15),
        ("tDeltaLapTimeMs",         c_int),
        ("tEstLapTime",             c_wchar * 15),
        ("tEstLapTimeMs",           c_int),
        ("BPositiveDelta",          c_int),
        ("TSplitMs",                c_int),
        ("BValidLap",               c_int),
        ("NLapsPossibleEstimate",   c_float),
        ("yTrackStatus",            c_wchar * 33),
        ("NRemMandatoryPits",       c_int),
        ("tTimeOfDay",              c_float),
        ("BIndicatorLeft",          c_int),
        ("BIndicatorRight",         c_int),
        ("BFlagYellowGlobal",       c_int),
        ("BFlagYellowSect1",        c_int),
        ("BFlagYellowSect2",        c_int),
        ("BFlagYellowSect3",        c_int),
        ("BFlagWhiteGlobal",        c_int),
        ("BFlagGreenGlobal",        c_int),
        ("BFlagCheckeredGlobal",    c_int),
        ("BFlagRedGlobal",          c_int),
        ("NTyreSetMFD",             c_int),
        ("LFuelToAdd",              c_float),
        ("pTyrePressureLFMFD",      c_float),
        ("pTyrePressureRFMFD",      c_float),
        ("pTyrePressureLRMFD",      c_float),
        ("pTyrePressureRRMFD",      c_float),
        ("NTrackGripStatus",        c_int),         #enum acc track grip status
        ("NRainIntensity",          c_int),         #enum acc rain intensity
        ("NRainIntensity10Min",     c_int),         #enum acc rain intensity
        ("NRainIntensity30Min",     c_int),         #enum acc rain intensity
        ("NCurrentTyreSet",         c_int),
        ("NStrategyTyreSet",        c_int)
	]

class SPageFileStatic(Structure):                   #reported once at session startup/memory read
    _fields_ = [
		("yShMemVersion",           c_wchar * 15),
		("yAcVersion",              c_wchar * 15),
		("NNumberOfSessions",       c_int),
		("NNumCars",                c_int),
		("yCarModel",               c_wchar * 33),  #Appendix 2
		("yTrack",                  c_wchar * 33),
		("yPlayerName",             c_wchar * 33),
		("yPlayerSurname",          c_wchar * 33),
		("yPlayerNick",             c_wchar * 33),
		("NSectorCount",            c_int),
		("MMaxTorque",              c_float),       #not used in ACC
		("PMaxPower",               c_float),       #not used in ACC
		("nMaxRpm",                 c_int),
		("LMaxFuel",                c_float),
		("sSuspensionMaxTravel",    c_float * 4),   #not used in ACC
		("sTyreRadius",             c_float * 4),   #not used in ACC
		("pMaxTurboBoost",          c_float * 4),   #not used in ACC
		("zDeprecated_1",           c_float),
		("zDeprecated_2",           c_float),
		("BPenaltiesEnabled",       c_int),
		("rFuelRateAid",            c_float),
		("rTireRateAid",            c_float),
		("rMechanicalDamageAid",    c_float),
		("rAllowTyreBlanketsAid",   c_int),
		("rStabilityAid",           c_float),
		("rAutoClutchAid",          c_int),
		("rAutoBlipAid",            c_int),         #always returns 1
		("BHasDRS",                 c_int),         #not used in ACC
		("BHasERS",                 c_int),         #not used in ACC
		("BHasKERS",                c_int),         #not used in ACC
		("EKERSMaxJ",               c_float),       #not used in ACC
		("NEngineBrakeSettings",    c_int),         #not used in ACC
		("NERSPowerController",     c_int),         #not used in ACC
		("sTrackSPlineLength",      c_float),       #not used in ACC
		("sTrackConfiguration",     c_wchar * 33),  #not used in ACC
		("EERSMaxJ",                c_float),       #not used in ACC
		("BIsTimedRace",            c_int),         #not used in ACC
		("BHasExtraLap",            c_int),         #not used in ACC
		("yCarSkin",                c_wchar * 33),  #not used in ACC
		("BReverseGridPositions",   c_int),         #not used in ACC
		("tPitWindowStart",         c_int),
		("tPitWindowEnd",           c_int),
		("BIsOnline",               c_int),
        ("yDryTyresName",           c_wchar * 33),
        ("yWetTyresName",           c_wchar * 33)
	]