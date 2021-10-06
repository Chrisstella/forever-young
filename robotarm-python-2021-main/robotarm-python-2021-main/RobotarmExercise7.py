from RobotArm import RobotArm
robotArm = RobotArm('exercise 7')


for A in range(5):
    for Y in range(6):
        robotArm.moveRight()
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
    for Z in range(2):
        robotArm.moveRight()

robotArm.wait()