import wpilib
from wpilib.command.subsystem import Subsystem

from commands.followjoystick import FollowJoystick


import driveTrain

class MechenumMove(Subsystem):
    '''
    This example subsystem controls a single CAN Talon SRX in PercentVBus mode.
    '''

    def __init__(self):
        '''Instantiates the drive train to be used with direction and speed commands'''
        super().__init__('MecanumMove')


    def setDriveTrain(self, magnitude, directionDeg, rotation):
        driveTrain.driveTrain.setSafetyEnabled(True)
        driveTrain.driveTrain.holonomicDrive(magnitude,directionDeg,rotation)
        
    def disableDriveTrain(self):
        driveTrain.driveTrain.holonomicDrive(0,0,0)
        driveTrain.driveTrain.setSafetyEnabled(False)


