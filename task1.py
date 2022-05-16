import rover
import sys
import tty
import termios





rover.init(1)

#left is index 1



while(1):
    if(rover.getDistance() > 10):
        rover.forward(20)
    else:
        turnCount = [0,0]
        distance = []

        #distance left is index 1

        rover.setServo(5, 575)
        distance[0] = (rover.getDistance())
        rover.setServo(5, 175)
        distance[1] = (rover.getDistance())
        rover.setServo(5, 375)

        if( (distance[0] > distance[1] and turnCount[0] < 2) or turnCount[1] == 2):
            rover.turnForward(20, 50)
            turnCount[1] =0
            turnCount[0] += 1
        elif( (distance[1] > distance[0] and turnCount[1] < 2) or turnCount[0] == 2 ):
            rover.spinRight(50,20)
            turnCount[0] = 0
            turnCount[1] += 1 
        

    if(KeyboardInterrupt):
        manual()

def manual():
    while True:
        key = readkey()
        if key == ' ':
            degrees = 0
            rover.setServo(servo, degrees)
            print ('Servo ', servo, ': Centre',sep='')

        if key == 'x' or key == '.':
            rover.stopServos()
            print ('Servo ', servo, ': Stop',sep='')

        elif key == 'w' or ord(key) == 16:
            servo += 1
            servo %= 16
            print ('Servo ', servo, ': Selected',sep='')

        elif key == 'z' or ord(key) == 17:
            servo -= 1
            servo %= 16
            print ('Servo ', servo, ': Selected',sep='')

        elif key == 'a' or ord(key) == 19:
            degrees -= 5
            if (degrees < -90):
                degrees = -90
            rover.setServo(servo, degrees)
            print ('Servo ', servo, ': Value:', degrees, sep='')

        elif key == 's' or ord(key) == 18:
            degrees += 5
            if (degrees > 90):
                degrees = 90
            rover.setServo(servo, degrees)
            print ('Servo ', servo, ': Value:', degrees, sep='')
        elif key == 'e' :
            return

        elif ord(key) == 3:
            break

def readchar():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    if ch == '0x03':
        raise KeyboardInterrupt
    return ch

def readkey(getchar_fn=None):
    getchar = getchar_fn or readchar
    c1 = getchar()
    if ord(c1) != 0x1b:
        return c1
    c2 = getchar()
    if ord(c2) != 0x5b:
        return c1
    c3 = getchar()
    return chr(0x10 + ord(c3) - 65)  # 16=Up, 17=Down, 18=Right, 19=Left arrows

            
            

