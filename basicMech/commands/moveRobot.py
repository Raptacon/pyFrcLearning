import wpilib
from wpilib.command import TimedCommand
import subsystems
class MoveRobot(TimedCommand):
	def __init__(self, magnitude, direction, rotation, timeoutInSeconds):
		super().__init__("Set Speed %d Direction %d and rotation %d "%(magnitude, direction, rotation), timeoutInSeconds)
		self.M = magnitude
		self.D = direction
		self.R = rotation
		self.requires(subsystems.move)
		
	def initialize(self):
		subsystems.move.setDriveTrain(self.M, self.D, self.R)
		
	def end(self):
		subsystems.move.disableDriveTrain()