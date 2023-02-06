#!/usr/bin/env python3

import roslib; roslib.load_manifest('joint_animation_tutorial')
import rospy, math, time
import pandas as pd

from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

def jointTrajectoryCommand():
	# Initialize the node
	rospy.init_node('joint_control')

	print (rospy.get_rostime().to_sec())
	while rospy.get_rostime().to_sec() == 0.0:
	        time.sleep(0.1)
	        print (rospy.get_rostime().to_sec())

	pos = pd.read_csv('talos_pickplace_jointpos.csv', header=None)

	pub = rospy.Publisher('/joint_trajectory', JointTrajectory, queue_size=10)
	jt = JointTrajectory()

	jt.header.stamp = rospy.Time.now()
	jt.header.frame_id = " "
	jt.joint_names.append("arm_left_1_joint")
	jt.joint_names.append("arm_left_2_joint")
	jt.joint_names.append("arm_left_3_joint")
	jt.joint_names.append("arm_left_4_joint")
	jt.joint_names.append("arm_left_5_joint")
	jt.joint_names.append("arm_left_6_joint")
	jt.joint_names.append("arm_left_7_joint")
	jt.joint_names.append("arm_right_1_joint")
	jt.joint_names.append("arm_right_2_joint")
	jt.joint_names.append("arm_right_3_joint")
	jt.joint_names.append("arm_right_4_joint")
	jt.joint_names.append("arm_right_5_joint")
	jt.joint_names.append("arm_right_6_joint")
	jt.joint_names.append("arm_right_7_joint")
	jt.joint_names.append("gripper_left_joint")
	jt.joint_names.append("gripper_right_joint")
	jt.joint_names.append("head_1_joint")
	jt.joint_names.append("head_2_joint")
	jt.joint_names.append("leg_left_1_joint")
	jt.joint_names.append("leg_left_2_joint")
	jt.joint_names.append("leg_left_3_joint")
	jt.joint_names.append("leg_left_4_joint")
	jt.joint_names.append("leg_left_5_joint")
	jt.joint_names.append("leg_left_6_joint")
	jt.joint_names.append("leg_right_1_joint")
	jt.joint_names.append("leg_right_2_joint")
	jt.joint_names.append("leg_right_3_joint")
	jt.joint_names.append("leg_right_4_joint")
	jt.joint_names.append("leg_right_5_joint")
	jt.joint_names.append("leg_right_6_joint")
	jt.joint_names.append("torso_1_joint")
	jt.joint_names.append("torso_2_joint")
	
	dt = 0.01
	n = 0
	count = 4552
	
	for i in range (count):
   	    p = JointTrajectoryPoint()
   	    p.positions.append(pos._get_value(n,0))
   	    p.positions.append(pos._get_value(n,1))
   	    p.positions.append(pos._get_value(n,2))
   	    p.positions.append(pos._get_value(n,3))
   	    p.positions.append(pos._get_value(n,4))
   	    p.positions.append(pos._get_value(n,5))
   	    p.positions.append(pos._get_value(n,6))
   	    p.positions.append(pos._get_value(n,7))
   	    p.positions.append(pos._get_value(n,8))
   	    p.positions.append(pos._get_value(n,9))
   	    p.positions.append(pos._get_value(n,10))
   	    p.positions.append(pos._get_value(n,11))
   	    p.positions.append(pos._get_value(n,12))
   	    p.positions.append(pos._get_value(n,13))
   	    p.positions.append(pos._get_value(n,14))
   	    p.positions.append(pos._get_value(n,15))
   	    p.positions.append(pos._get_value(n,16))
   	    p.positions.append(pos._get_value(n,17))
   	    p.positions.append(pos._get_value(n,18))
   	    p.positions.append(pos._get_value(n,19))
   	    p.positions.append(pos._get_value(n,20))
   	    p.positions.append(pos._get_value(n,21))
   	    p.positions.append(pos._get_value(n,22))
   	    p.positions.append(pos._get_value(n,23))
   	    p.positions.append(pos._get_value(n,24))
   	    p.positions.append(pos._get_value(n,25))
   	    p.positions.append(pos._get_value(n,26))
   	    p.positions.append(pos._get_value(n,27))
   	    p.positions.append(pos._get_value(n,28))
   	    p.positions.append(pos._get_value(n,29))
   	    p.positions.append(pos._get_value(n,30))
   	    p.positions.append(pos._get_value(n,31))
   	    jt.points.append(p)
   	    #print (n)
   	    n+=1
   	   
   	    
   	    #set duration
   	    jt.points[i].time_from_start = rospy.Duration.from_sec(dt*i)
   	    #rospy.loginfo("test: angles[%d][%f, %f]",n,x1,x2)
	pub.publish(jt)
	rospy.spin()

if __name__ == '__main__':
	try:
		jointTrajectoryCommand()
	except rospy.ROSInterruptException: pass
