#!/usr/bin/env python3
import rospy
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from math import radians
import time

def send_motion(pub, r, wA, wB, duration):
    """
    Send a single joint trajectory point based on motor speeds.
    """
    v_x = r * (wA + wB) / 2
    v_y = r * (wA - wB) / 2

    traj = JointTrajectory()
    traj.joint_names = ['bridge_vertical_joint', 'carriage_horizontal_joint']

    point = JointTrajectoryPoint()
    point.positions = [v_y * duration, v_x * duration]
    point.time_from_start = rospy.Duration(duration)

    traj.points = [point]
    pub.publish(traj)

if __name__ == '__main__':
    rospy.init_node('hbot_motor_speed_loop')
    pub = rospy.Publisher('/gantry_controller/command', JointTrajectory, queue_size=1)
    rate = rospy.Rate(0.5)  # One motion every 2 seconds

    # Pulley radius
    r = 0.05  # meters
    duration = 1.0  # seconds per motion

    # Loop with continuously changing speeds (customize here)
    while not rospy.is_shutdown():
        # Define speeds in degrees/second
        wA_deg = 30  # motor A speed
        wB_deg = 10  # motor B speed

        # You can toggle signs to reverse direction
        wA = radians(wA_deg)
        wB = radians(wB_deg)

        send_motion(pub, r, wA, wB, duration)
        rate.sleep()

