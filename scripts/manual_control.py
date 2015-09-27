#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy

def callback(data):
	twist = Twist()
	twist.linear.y = data.axis[1]
	twist.linear.x = data.axis[0]
	if data.buttons[0]:
		twist.linear.z = -1
	elif data.buttons[1]:
		twist.linear.z = 1
	pub.publish(twist)

def start():
    global pub
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 10)
    # subscribed to joystick inputs on topic "joy"
    rospy.Subscriber("joy", Joy, callback)
    # starts the node
    rospy.init_node('manual_control')
    rospy.spin()

if __name__ == '__main__':
    try:
        start()
    except rospy.ROSInterruptException:
        pass
