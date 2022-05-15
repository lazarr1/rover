import calibrateServos
import driveRover
import gyro
import keypad
import ledTest
import motorTest
import pca9685
import rover
import servoTest
import sonarTest



def run():
    rover.init(1)

    #left is index 1
    turnCount = [0,0]

    while(1):
        if(rover.getDistance() > 10):
            rover.forward(20)


        else:
            distance = []

            #distance left is index 1

            pca9685.setServo(5, 575)
            distance.append(rover.getDistance())
            pca9685.setServo(5, 175)
            distance.append(rover.getDistance())
            pca9685.setServo(5, 375)

            if( (distance[0] > distance[1] and turnCount[0] < 2) or turnCount[1] == 2):
                rover.spinRight(20)
                turnCount[1] =0
                turnCount[0] += 1
            elif( (distance[1] > distance[0] and turnCount[1] < 2) or turnCount[0] == 2  ):
                rover.spinLeft(20)
                turnCount[0] = 0
                turnCount[1] += 1 
            

        if(KeyboardInterrupt):
            motorTest.userInputs






if __name__ == '__task1__':

    run()


            
            

