#!/usr/bin/env python3
'''
    This is a demo program showing how to use Mecanum control with the
    RobotDrive class.
'''

import wpilib
from robotMap import RobotMap
import ctre
import driveTrain
import commandbased
import subsystems

from commands import autonomous
from commands import followjoystick

class MyRobot(commandbased.CommandBasedRobot):
    
    def robotInit(self):
        '''Robot initialization function'''
        self.map = RobotMap()
        self.driveMotors = self.createMotors(self.map.CAN.driveMotors)
        

        driveTrain.init(self.driveMotors)              

        self.driveStick = wpilib.Joystick(self.map.joystickMap.movementJoystick)
    
        
        '''
        This is a good place to set up your subsystems and anything else that
        you will need to access later.
        '''

        subsystems.init()
        self.autonomousProgram = autonomous.AutonomousProgram()
        
        self.teleopMove = followjoystick.FollowJoystick(self.driveStick.getX,self.driveStick.getY,self.driveStick.getZ)


    def createMotors(self,motorMap):
        createMotors = {}
        for motorName in motorMap:
            motor = motorMap[motorName]
            newMotor = None
            if motor['type'] == 'CANTalon':
                print("Found CANTalon for channel ", motor['channel'])
                #create talon
                newMotor = ctre.CANTalon(motor['channel'])
                #set invereted based on property
                newMotor.setInverted(motor['inverted'])
                
            else:
                print("Unknown motor %s of type %s"%(motorName,motor['type']))
                
            #add motor to the drive motor dictonary
            createMotors[motorName] = newMotor
                
        #return this motor list
        return createMotors


    def autonomousInit(self):
        '''
        You should call start on your autonomous program here. You can
        instantiate the program here if you like, or in robotInit as in this
        example. You can also use a SendableChooser to have the autonomous
        program chosen from the SmartDashboard.
        '''

        self.autonomousProgram.start()

    def teleopInit(self):
        #for now we are using the same code as in autonomous.
        subsystems.drive.setDefaultCommand(self.teleopMove)
        #self.teleopMove.start()        
    
    

if __name__ == '__main__':
    wpilib.run(MyRobot)

