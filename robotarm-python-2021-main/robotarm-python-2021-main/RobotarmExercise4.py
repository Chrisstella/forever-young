from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')

# Jouw python instructies zet je vanaf hier:

for A in range(3):
    robotArm.grab()
    for B in range(2):
        robotArm.moveRight()
    robotArm.drop()
    for G in range(2):
        robotArm.moveLeft()

robotArm.moveRight()
robotArm.moveRight()

for O in range(3):
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()
    robotArm.moveRight()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()