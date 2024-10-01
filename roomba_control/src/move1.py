#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def cmd_vel_publisher(cmd, tempo):
    # Inicializa o nó ROS com o nome 'cmd_vel_publisher'
    rospy.init_node('cmd_vel_publisher', anonymous=True)
    
    # Cria um publisher para o tópico /cmd_vel do tipo Twist
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    
    # Define a taxa de publicação para 10 Hz
    rate = rospy.Rate(10)

    # Armazena o tempo de início
    start_time = rospy.get_time()
    
     # Publica a mensagem enquanto o tempo não exceder 2 segundos
    while not rospy.is_shutdown():
        current_time = rospy.get_time()
        
        if current_time - start_time > tempo:
            break  # Sai do loop após 2 segundos

        rospy.loginfo(f"Publicando: linear={cmd.linear.x}, angular={cmd.angular.z}")
        pub.publish(cmd)
        rate.sleep()


if __name__ == '__main__':
    try:
        # Cria uma mensagem Twist
        cmd = Twist()
        cmd.linear.x = 0.1  # Velocidade linear em x (m/s)
        cmd.angular.z = 0.0  # Velocidade angular em z (rad/s)
        cmd_vel_publisher(cmd)


    except rospy.ROSInterruptException:
        pass
