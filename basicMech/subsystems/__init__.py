'''
All subsystems should be imported here and instatniated inside the init method. 
If you want your subsystem accesiable inside commands 
then you must add a variable for it in the general scope.
'''

from .mecanumMove import MechanumMove

move= None

def init():
    global move

    if (mechMoveSubsystem is not None) and (not RobotBase.isSimulation()):
        raise RuntimeError("Subsystems have already been initilized")
        
    mechMoveSubsystem = MechanumMove()
    
