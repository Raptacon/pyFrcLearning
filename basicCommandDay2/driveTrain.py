import wpilib
from wpilib import RobotDrive

driveTrain = None 

def init(driveMotors): 
	global driveTrain
	driveTrain = wpilib.RobotDrive(**driveMotors)
	driveTrain.setExpiration(0.2)
	driveTrain.setSafetyEnabled(False)