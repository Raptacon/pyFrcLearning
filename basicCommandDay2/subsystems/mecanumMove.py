import wpilib
from wpilib.command.subsystem import Subsystem

import driveTrain

class MechanumMove(Subsystem): 
    '''
    This subsystem moves a robot using the holomonic driv method which is aimed at autonomous movement.
    '''
     
    def __init__(self):
        super().__init__("MecanumMove")
    
    def setDriveTrain(self,magnitude,directionDeg, rotation):
        driveTrain.driveTrain.setSafetyEnabled(True)
        driveTrain.driveTrain.holonomicDrive(magnitude,directDeg,rotation)
        
    def disableDriveTrain(self):
        driveTrain.driveTrain.holonomicDrive(0,0,0)
        driveTrain.driveTrain.setSafetyEnabled(False)
        
       
    