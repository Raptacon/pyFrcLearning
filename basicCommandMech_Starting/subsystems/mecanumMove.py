import wpilib
from wpilib.command.subsystem import Subsystem



import driveTrain

class MechenumMove(Subsystem):

    '''
    This subsystem moves a robot using the holonomic drive 
    method which
    is aimed at autonmous movement.
    '''

    def __init__(self):
        super().__init__("MecanumMove")


    def setDriveTrain(self,magnitude, directionDeg, rotation):
        driveTrain.driveTrain.setSafteyEnabled(True)
        driveTrain.driveTrain.holonomicDrive(magnitude,
                                             directionDeg,
                                             rotation)

    def disableDriveTrain(self):
        driveTrain.driveTrain.holonomicDrive(0,0,0)
        driveTrain.driveTrain.setSafteyEnabled(False)


