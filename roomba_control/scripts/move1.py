#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from roomba_control_class import RobotControl

if __name__ == '__main__':
    
    try:
        
        
        # Crie uma instância da classe RobotControl
        roomba = RobotControl()
        
        # Mantenha o nó ativo
        rospy.spin()


    except rospy.ROSInterruptException:
        pass
