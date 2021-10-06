from RobotArm import RobotArm

robotArm = RobotArm('exercise 8')

# Jouw python instructies zet je vanaf hier:

robotArm.moveRight()
for A in range(7):
    robotArm.grab()

    for X in range(9):
        robotArm.moveRight()
    robotArm.drop()
    for Y in range(8):
        robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()