#!/usr/bin/env python3
'''
    This is a demo program showing how to use Mecanum control with the
    RobotDrive class.
'''

import wpilib
from wpilib import RobotDrive
from robotMap import RobotMap
import ctre

import commandbased

import subsystems

import driveTrain

from commands import autonomous

class MyRobot(commandbased.CommandBasedRobot):
    
    def robotInit(self):
        '''Robot initialization function'''
        self.map = RobotMap()
        self.createMotors(self.map.CAN.driveMotors)
                
        #inti the drive train
        driveTrain.init(self.driveMotors)        

        subsystems.init()
        self.autonomousProgram = autonomous.AutonomousProgram()
        self.driveStick = wpilib.Joystick(self.map.joystickMap.movementJoystick)
    

    def autonomousInit(self):
        print("AutonomousInit")
        self.autonomousProgram.start()

    def teleopInit(self):
        print("TeleopInit")


    def createMotors(self,motorMap):
        driveMotors = {}
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
            driveMotors[motorName] = newMotor
                
        #save motors to the robot class. We will use this to initlize the robot
        self.driveMotors = driveMotors
            

if __name__ == '__main__':
    wpilib.run(MyRobot)

