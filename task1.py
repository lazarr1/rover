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


    while(1):
        if(rover.getDistance() > 5):
            rover.forward(20)
        else:


            distance = []


            pca9685.setServo(5, 575)
            distance.append(rover.getDistance())
            pca9685.setServo(5, 175)
            distance.append(rover.getDistance())
            pca9685.setServo(5, 375)

            if(distance[0] > distance[1] and distance[0] > 5):
                rover.spinRight(20)
            else:
                rover.spinLeft(20)

        if(KeyboardInterrupt):
            motorTest.userInputs






if __name__ == '__task1__':

    run()


            
            

