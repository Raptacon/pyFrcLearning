# -*- coding: utf-8 -*-




class RobotMap():
    def __init__(self):
        self.CAN = CANMap()
        self.joystickMap = controllerMap()
        
        
        
class CANMap():
    def __init__(self):
        motors = {}
        #motors['frontRightMotor'] = {'channel':0, 'inverted':True, 'type':'CANTalon'}
        #motors['frontLeftMotor']  = {'channel':1, 'inverted':False, 'type':'CANTalon'}
        #motors['rearRightMotor']  = {'channel':2, 'inverted':True, 'type':'CANTalon'}
        #motors['rearLeftMotor']   = {'channel':3, 'inverted':False, 'type':'CANTalon'}
        motors['frontRightMotor'] = {'channel':9, 'inverted':True, 'type':'CANTalon'}
        motors['frontLeftMotor']  = {'channel':10, 'inverted':False, 'type':'CANTalon'}
        motors['rearRightMotor']  = {'channel':11, 'inverted':True, 'type':'CANTalon'}
        motors['rearLeftMotor']   = {'channel':12, 'inverted':False, 'type':'CANTalon'}        
        self.driveMotors = motors
        #add shooter motors to shooter.Motors
        
        
        
class controllerMap():
    def __init__(self):
        movement = {}
        self.movementJoystick = 0
        movement['x'] = 0 #joystick Axis
        movement['y'] = 1
        movement['rotation'] = 2
        self.movement = movement
        #create shooter controls