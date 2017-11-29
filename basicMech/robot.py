#!/usr/bin/env python3
'''
    This is a demo program showing how to use Mecanum control with the
    RobotDrive class.
'''

import wpilib
from wpilib import RobotDrive
from robotMap import RobotMap
import ctre



class MyRobot(wpilib.SampleRobot):
    
    def robotInit(self):
        '''Robot initialization function'''
        self.map = RobotMap()
        self.createMotors(self.map.CAN.driveMotors)
        
        #pass in the drive motors. We are using keyboard expansion. this is the same as
        #wpilib.RobotDrive(self.driveMotors['frontLeftMotor'],self.driveMotors['rearLeftMotor'],
        #                  self.driveMotors['frontRightMotor'], self.driveMotors['rearRightMotor'])
        #or (note the random order) using named parameters
        #wpilib.RobotDrive(rearLeftMotor = self.driveMotors['rearLeftMotor'], 
        #                  frontRightMotor = self.driveMotors['frontRightMotor'],
        #                  frontLeftMotor = self.driveMotors['frontLeftMotor'],
        #                  rearRightMotor = self.driveMotors['rearRightMotor'])
        self.robotDrive = wpilib.RobotDrive(**self.driveMotors)
        
        self.robotDrive.setExpiration(0.1)
        
                

        self.driveStick = wpilib.Joystick(self.map.joystickMap.movementJoystick)
    
    def operatorControl(self):
        '''Runs the motors with Mecanum drive.'''
        print("Starting driver mode")
        self.robotDrive.setSafetyEnabled(True)
        while self.isOperatorControl() and self.isEnabled():
            
            # Use the joystick X axis for lateral movement, Y axis for forward movement, and Z axis for rotation.
            # This sample does not use field-oriented drive, so the gyro input is set to zero.
            
            #self.robotDrive.mecanumDrive_Cartesian(gyroAngle = 0, **self.map.joystickMap.movement);
            self.robotDrive.mecanumDrive_Cartesian(self.driveStick.getX(),
                                                   self.driveStick.getY(),
                                                   self.driveStick.getZ(), 0);
            #print(self.driveMotors['rearLeftMotor'].get())
            print("FR:%0.2f FL:%0.2f RR:%0.2f RL:%0.2f"%(
                    self.driveMotors['frontRightMotor'].get(),
                    self.driveMotors['frontLeftMotor'].get(),
                    self.driveMotors['rearRightMotor'].get(),
                    self.driveMotors['rearLeftMotor'].get()
                    ))
            wpilib.Timer.delay(0.05)   # wait 5ms to avoid hogging CPU cycles
        print("Drive Mode Done")


    def test(self):
        """
        Test will run the motors forward for 1 second then backwoards for 1 second. The robot should end up near the same rotation
        After that the robot will rotate for 5 seconds.
        """
        
        #I just did these quick. I'm sure there are better ways.
        print("Test: Starting Forward")
        delay = 0.005
        delayed = 0.0
        
        while delayed < 1.0:
            self.robotDrive.holonomicDrive(.5, 0, 0)
            wpilib.Timer.delay(delay)
            delayed+=delay
        print("Test: Starting Back")
        delayed = 0.0
        while delayed < 1.0:
            self.robotDrive.holonomicDrive(-.5, 0.0, 0)
            wpilib.Timer.delay(delay)
            delayed+=delay
        print("Test: Starting Spin")
        delayed = 0.0
        while delayed < 1.0:
            self.robotDrive.holonomicDrive(0.5, 0, 1.0)
            wpilib.Timer.delay(delay)
            delayed+=delay
           
        self.robotDrive.holonomicDrive(0.0, 0.0, 0.0)
        print("Spin Done")
        print("Test Done")
        
        

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

