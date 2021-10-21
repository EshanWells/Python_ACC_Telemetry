"""
Attempt at constructor-based classes or something like that
"""
import mmap


buf = mmap.mmap(-1, 2732, u"Local\\acpmf_physics")
class SPageFilePhysics:
    def __init__ (self, buf):
        self.packetId               =buf[0]
        self.gas                    =buf[1]
        self.brake                  =buf[2]
        self.fuel                   =buf[3]
        self.gear                   =buf[4]
        self.rpm                    =buf[5]
        self.steerAngle             =buf[6]
        self.speedKmh               =buf[7]
        self.velocity               =[buf[8],buf[9],buf[10]]
        self.accG #array
        self.wheelSlip #array
        self.wheelLoad #nu array
        self.wheelPressure #array
        self.wheelAngularSpeed #array
        self.tyreWear #nu array
        self.tyreDirtyLevel #nu array
        self.TyreCoreTemp #array
        self.camberRAD #nu array
        self.suspensionTravel #array
        self.drs #nu
        self.tc
        self.heading
        self.pitch
        self.roll
        self.cgHeight #nu
        self.carDamage #array
        self.numberOfTyresOut #nu
        self.pitLimiterOn
        self.abs
        self.kersCharge #nu
        self.kersInput #nu
        self.autoshifterOn
        self.rideHeight #nu array
        self.turboBoost
        self.ballast #nu
        self.airDensity #nu
        self.airTemp
        self.roadTemp
        self.localAngualVel #array
        self.finalFF
        self.performanceMeter #nu
        self.engineBrake #nu
        self.ersRecoveryLevel #nu
        self.ersPowerLevel #nu
        self.ersHeatCharging #nu
        self.ersIsCharging #nu
        self.kersCurrentKJ #nu
        self.drsAvailable #nu
        self.drsEnabled #nu
        self.brakeTemp #array
        self.clutch
        self.tyreTempI #nu array
        self.tyreTempM #nu array
        self.tyreTempO #nu array
        self.isAIControlled
        self.tyreContactPoint #multidim array
        self.tyreContactNormal #multidim array
        self.tyreContactHeading #multidim array
        self.brakeBias
        self.localVelocity
        self.P2PActivation #nu
        self.P2PStatus #nu
        self.currentMaxRpm #nu
        self.mz #nu array
        self.fx #nu array
        self.fy #nu array
        self.slipRatio #array
        self.slipAngle #array
        self.tcInAction #nu
        self.absInAction #nu
        self.suspensionDamage #nu array
        self.tyreTemp #nu array
        self.waterTemp
        self.brakePressure #array
        self.frontBrakeCompound
        self.rearBrakeCompound
        self.padLife #array
        self.discLife #array
        self.ignitionOn
        self.starterEngineOn
        self.isEngineRunning
        self.kerbVibrations
        self.slipVibrations
        self.gVibrations
        self.absVibrations

#buf = mmap.mmap(-1, 2732, u"Local\\acpmf_physics")
physics = SPageFilePhysics(buf)
print(physics.velocity)