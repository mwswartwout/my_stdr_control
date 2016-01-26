#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

rospy.init_node('my_stdr_commander')

twist_commander = rospy.Publisher('robot0/cmd_vel', Twist, queue_size=1)

sample_dt = 0.01
speed = 1
yaw_rate = 0.5
time_3_sec = 3
loop_timer = rospy.Rate(1 / sample_dt)
timer = 0

twist_cmd = Twist()
twist_cmd.linear.x = 0
twist_cmd.linear.y = 0
twist_cmd.linear.z = 0
twist_cmd.angular.x = 0
twist_cmd.angular.y = 0
twist_cmd.angular.z = 0

for i in range(0, 10):
    twist_commander.publish(twist_cmd)
    loop_timer.sleep()

# Forward 1
twist_cmd.linear.x = speed  # command to move forward
while timer < time_3_sec:
    twist_commander.publish(twist_cmd)
    timer += sample_dt
    loop_timer.sleep()

# Left 1
twist_cmd.linear.x = 0  # stop moving forward
twist_cmd.angular.z = yaw_rate  # and start spinning (left) in place
timer = 0  # reset the timer
while timer < time_3_sec:
    twist_commander.publish(twist_cmd)
    timer += sample_dt
    loop_timer.sleep()

# Forward 2
twist_cmd.angular.z = 0  # and stop spinning in place
twist_cmd.linear.x = speed  # and move forward again
timer = 0  # reset the timer
while timer < time_3_sec:
    twist_commander.publish(twist_cmd)
    timer += sample_dt
    loop_timer.sleep()

# Right 2
twist_cmd.linear.x = 0  # stop moving forward
twist_cmd.angular.z = yaw_rate * -1  # and start spinning (right) in place
timer = 0  # reset the timer
while timer < time_3_sec:
    twist_commander.publish(twist_cmd)
    timer += sample_dt
    loop_timer.sleep()

# Forward 3
twist_cmd.angular.z = 0  # and stop spinning in place
twist_cmd.linear.x = speed  # and move forward again
timer = 0  # reset the timer
while timer < time_3_sec + .5:
    twist_commander.publish(twist_cmd)
    timer += sample_dt
    loop_timer.sleep()

# Left 3
twist_cmd.linear.x = 0  # stop moving forward
twist_cmd.angular.z = yaw_rate  # and start spinning (left) in place
timer = 0  # reset the timer
while timer < time_3_sec:
    twist_commander.publish(twist_cmd)
    timer += sample_dt
    loop_timer.sleep()

# Forward 4
twist_cmd.angular.z = 0  # and stop spinning in place
twist_cmd.linear.x = speed  # and move forward again
timer = 0  # reset the timer
while timer < time_3_sec - .8:
    twist_commander.publish(twist_cmd)
    timer += sample_dt
    loop_timer.sleep()

# Left 4
twist_cmd.linear.x = 0  # stop moving forward
twist_cmd.angular.z = yaw_rate  # and start spinning (left) in place
timer = 0  # reset the timer
while timer < time_3_sec + .2:
    twist_commander.publish(twist_cmd)
    timer += sample_dt
    loop_timer.sleep()

# Forward 5
twist_cmd.angular.z = 0  # and stop spinning in place
twist_cmd.linear.x = speed  # and move forward again
timer = 0  # reset the timer
while timer < time_3_sec + 3:
    twist_commander.publish(twist_cmd)
    timer += sample_dt
    loop_timer.sleep()

# Right 5
twist_cmd.linear.x = 0  # stop moving forward
twist_cmd.angular.z = yaw_rate * -1  # and start spinning (right) in place
timer = 0  # reset the timer
while timer < time_3_sec:
    twist_commander.publish(twist_cmd)
    timer += sample_dt
    loop_timer.sleep()

# Forward 6
twist_cmd.angular.z = 0  # and stop spinning in place
twist_cmd.linear.x = speed  # and move forward again
timer = 0  # reset the timer
while timer < time_3_sec - 1:
    twist_commander.publish(twist_cmd)
    timer += sample_dt
    loop_timer.sleep()

# Left 6
twist_cmd.linear.x = 0  # stop moving forward
twist_cmd.angular.z = yaw_rate  # and start spinning (left) in place
timer = 0  # reset the timer
while timer < time_3_sec:
    twist_commander.publish(twist_cmd)
    timer += sample_dt
    loop_timer.sleep()

# Forward 7
twist_cmd.angular.z = 0  # and stop spinning in place
twist_cmd.linear.x = speed  # and move forward again
timer = 0  # reset the timer
while timer < time_3_sec - 2.5:
    twist_commander.publish(twist_cmd)
    timer += sample_dt
    loop_timer.sleep()

# Right 7
twist_cmd.linear.x = 0  # stop moving forward
twist_cmd.angular.z = yaw_rate * -1  # and start spinning (right) in place
timer = 0  # reset the timer
while timer < time_3_sec + .1:
    twist_commander.publish(twist_cmd)
    timer += sample_dt
    loop_timer.sleep()

# Forward 8
twist_cmd.angular.z = 0  # and stop spinning in place
twist_cmd.linear.x = speed  # and move forward again
timer = 0  # reset the timer
while timer < time_3_sec + 1:
    twist_commander.publish(twist_cmd)
    timer += sample_dt
    loop_timer.sleep()

# Halt motion
twist_cmd.angular.z = 0
twist_cmd.linear.x = 0
for i in range(0, 10):
    twist_commander.publish(twist_cmd)
    loop_timer.sleep()

# Now we are done
