import wpilib


from wpilib.command import TimedCommand

import subsystems


class MoveRobot(TimedCommand):

    def __init__(self, magnitude, direction, rotation, timeoutInSeconds):
        super().__init__('Set Spped %d Direction %d and rotation %d'%
                         (magnitude,direction,rotation)
                         ,timeoutInSeconds)
        self.magnitude = magnitude
        self.direction = direction
        self.rotation = rotation
        self.requires(subsystems.move)


    def initialize(self):
        subsystems.move.setDriveTrain(self.magnitude, self.direction, self.rotation)

    def end(self):
        subsystems.move.disableDriveTrain()


