import wpilib
from wpilib.command.commandgroup import CommandGroup
from wpilib.command.waitcommand import WaitCommand
from commands.moveRobot import MoveRobot

class AutonomousProgram(CommandGroup):
	def __init__(self):
		super().__init__("Autonomous Program")
		self.addSequential(MoveRobot(0.5,0,0,timeoutInSeconds = 1))
		self.addSequential(WaitCommand(timeoutInSeconds = 1))
		self.addSequential(MoveRobot(-0.5,0,0,timeoutInSeconds = 1))
		self.addSequential(WaitCommand(timeoutInSeconds = 1))
		self.addSequential(MoveRobot(0.5,0,1,timeoutInSeconds = 1))