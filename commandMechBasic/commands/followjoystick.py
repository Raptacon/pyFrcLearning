from wpilib.command import Command
from wpilib import RobotState

import driveTrain
import subsystems

class FollowJoystick(Command):  
    '''
    This command will read the joystick's x,y,z axis and use that value to control
    the speed of the SingleMotor subsystem.
    '''

    def __init__(self, getx, gety, getz, getAngle = None):
        super().__init__('Follow Joystick')
        self.getx = getx;
        self.gety = gety;
        self.getz = getz;
        self.getAngle = getAngle;
        self.requires(subsystems.drive)
        

    def execute(self):
        
        #only run during operator control
        if not RobotState.isOperatorControl():
            return
        if self.getAngle:
            subsystems.drive.setDriveTrain(self.getx(), self.gety(), self.getz(), self.getAngle())
        else:
            subsystems.drive.setDriveTrain(self.getx(), self.gety(), -self.getz(), 0)
            