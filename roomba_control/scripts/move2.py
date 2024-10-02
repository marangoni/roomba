#!/usr/bin/env python

import rospy
from bumper_control_class import BumperControl  # Importa a classe BumperControl

if __name__ == '__main__':
    try:
        #rospy.init_node('bumper_control_node', anonymous=True)

        # Instancia a classe BumperControl
        bumper_control = BumperControl()

        # Executa o método que controla o movimento e verifica o bumper
        bumper_control.move_and_check_bumper()

    except rospy.ROSInterruptException:
        pass
