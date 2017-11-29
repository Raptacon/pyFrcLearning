'''
All subsystems should be imported here and 
instatniated inide the init method.
If you want your subsystem accessiable inside commands
then you must add a variable for it in the global scope.
'''

from .mecanumMove import MechenumMove
 
 
mechMoveSubsystem = None

def init():
    global mechMoveSubsystem

    if (mechMoveSubsystem is not None) and (not RobotBase.isSimulation()):
        raise RuntimeError("Susbsystems have already \
                           been iitilized")

    mechMoveSubsystem = MechenumMove()


