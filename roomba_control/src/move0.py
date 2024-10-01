#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from roomba_control_class import RobotControl

if __name__ == '__main__':
    
    roomba = RobotControl() # Cria a instância aqui
     
    
    try:
        roomba.move_straight_time("forward", 0.15, 2)
        roomba.turn("clockwise",0.25,2)
        #roomba.rotate(90)
        roomba.move_straight_time("forward", 0.15, 2)
        #roomba.rotate(90)
        roomba.turn("clockwise",0.25,3)
        roomba.move_straight_time("forward", 0.15, 2)
        roomba.rotate(90)
        roomba.move_straight_time("forward", 0.15, 2)
        roomba.rotate(90)


    except rospy.ROSInterruptException:
        pass
