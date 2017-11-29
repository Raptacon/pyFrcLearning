import wpilib
from wpilib.command.subsystem import Subsystem

from commands.followjoystick import FollowJoystick


import driveTrain

class MechenumDrive(Subsystem):
    '''
    This example subsystem controls a mecanum drive train for use with joysticks
    '''

    def __init__(self):
        '''Instantiates the drive train to be used with direction and speed commands'''
        super().__init__('MecanumDrive')


    def setDriveTrain(self, x, y, rot, dirOffsetDeg = 0):
        driveTrain.driveTrain.mecanumDrive_Cartesian(x,y,rot,dirOffsetDeg)
