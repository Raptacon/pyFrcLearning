from wpilib.command.commandgroup import CommandGroup

from wpilib.command.waitcommand import WaitCommand
from commands.moveRobot import MoveRobot

class AutonomousProgram(CommandGroup):
    '''
    A simple program that spins the motor for two seconds, pauses for a second,
    and then spins it in the opposite direction for two seconds.
    '''

    def __init__(self):
        super().__init__('Autonomous Program')

        self.addSequential(MoveRobot(.5,0,0, timeoutInSeconds=1))
        self.addSequential(WaitCommand(timeout=1))
        self.addSequential(MoveRobot(-.5,0,0, timeoutInSeconds=1))
        self.addSequential(WaitCommand(timeout=1))
        self.addSequential(MoveRobot(.5,0,1.0, timeoutInSeconds=1))

