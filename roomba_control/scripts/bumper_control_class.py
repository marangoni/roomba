#!/usr/bin/env python

# Classe em python criada para implementação da logica
# de leitura do sensor bumper e movimentação em função
# desta leitura

import rospy
from create_msgs.msg import Bumper
from roomba_control_class import RobotControl  

class BumperControl(RobotControl):
    def __init__(self):
        super(BumperControl, self).__init__()
        self.bumper_pressed = False
        self.bumper_sub = rospy.Subscriber('/bumper', Bumper, self.bumper_callback)

    def bumper_callback(self, msg):
        if msg.is_left_pressed or msg.is_right_pressed:
            rospy.loginfo("Bumper acionado, parando o robô")
            self.bumper_pressed = True
            self.stop_robot()

    def move_and_check_bumper(self):
        rate = rospy.Rate(10)

        while not rospy.is_shutdown():
            if not self.bumper_pressed:
                self.move_straight()
            else:
                rospy.loginfo("Executando manobra após bumper ser acionado")
                rospy.loginfo("Robô andando para trás")
                self.move_straight_time("backward", speed = 0.5, time=2)             
                self.turn(clockwise="clockwise", speed=0.5, time=2)
                  
                self.bumper_pressed = False
            
            rate.sleep()
