#!/usr/bin/env python

#this code sends reference joint angles to TALOS


#import libraries
import roslib
import rospy
import actionlib
from std_msgs.msg import Float64
import trajectory_msgs.msg
import control_msgs.msg
from trajectory_msgs.msg import JointTrajectoryPoint
from control_msgs.msg import JointTrajectoryAction, JointTrajectoryGoal, FollowJointTrajectoryAction, FollowJointTrajectoryGoal
import multiprocessing
from multiprocessing import Process, Queue
import threading
import queue
from csv import reader
import csv
import numpy as np
import time


#function for reading csv files
def read_csv(file_loc):
    with open(file_loc, 'r') as read_obj:
        i = 0
        angles = [] #change this number according to your csv file size
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        # Iterate over each row in the csv using reader object
        for row in csv_reader:
            # row variable is a list that represents a row in csv
            try:
            	angles.append([float(x) for x in row[:-1]])
            except:
            	print('Error Parsing Line {}'.format(row))
            #print(row)
            i += 1
        print("Read {} lines from csv file {}".format(i,file_loc))
        print("Line 1: {}\nLast Line: {}".format(angles[0],angles[-1]))
    return angles



#class for publishing joint trajectory angles
class Joint:
        def __init__(self, motor_name, joint_name):
            #arm_name should be b_arm or f_arm
            self.name = motor_name
            self.joint_name = joint_name
            self.jta = actionlib.SimpleActionClient('/'+self.name+'_controller/follow_joint_trajectory', FollowJointTrajectoryAction)
            #rospy.loginfo('Waiting for joint trajectory action')
            #self.jta.wait_for_server()
            #rospy.loginfo('Found joint trajectory action!')


        def move_joint(self, start_time, angles, vels, accs):
            goal = FollowJointTrajectoryGoal()
            goal.trajectory.header.stamp = start_time
            char = self.name[0] #either 'f' or 'b'
            #print(len(angles))
            if len(angles[0]) == 6: #legs have 6 joints
                goal.trajectory.joint_names = [self.joint_name+'1_joint', self.joint_name+'2_joint', self.joint_name+'3_joint', self.joint_name+'4_joint', self.joint_name+'5_joint',                   self.joint_name+'6_joint']  
            elif len(angles[0]) == 7: #arms have 7 joints
                goal.trajectory.joint_names = [self.joint_name+'1_joint', self.joint_name+'2_joint', self.joint_name+'3_joint', self.joint_name+'4_joint', self.joint_name+'5_joint', self.joint_name+'6_joint', self.joint_name+'7_joint']
            elif len(angles[0]) == 2: #torso has 2 joints
                goal.trajectory.joint_names = [self.joint_name+'1_joint', self.joint_name+'2_joint']
            elif len(angles[0]) == 1: #gripper has 1 joint
                goal.trajectory.joint_names = [self.joint_name+'left_joint', self.joint_name+'right_joint']	
            else:
                raise Exception ('Dimension')
            mytime = 0
            for point_angles, point_vels, point_accs in zip(angles,vels,accs):
                point = JointTrajectoryPoint()
                point.positions = point_angles
                point.velocities = point_vels
                point.accelerations = point_accs
                point.time_from_start = rospy.Duration(mytime)
                mytime = mytime + 0.01
                goal.trajectory.points.append(point) 
            print("move_joint for joints \"{}\" with angles size {} {}, duration {}s".format(
            	goal.trajectory.joint_names,
            	len(angles),len(angles[0]),
            	mytime))                
            self.jta.send_goal_and_wait(goal)

#define the controllers
la_controller = Joint('left_arm', 'arm_left_')
ra_controller = Joint('right_arm', 'arm_right_')
ll_controller = Joint('left_leg', 'leg_left_')
rl_controller = Joint('right_leg', 'leg_right_')
t_controller = Joint('torso', 'torso_')
lg_controller = Joint('left_gripper', 'gripper_left_')
rg_controller = Joint('right_gripper', 'gripper_right_')


def main():
    #file locations
    right_leg_angles = read_csv('talos_pickplace_jointpos_leg_right.csv')
    left_leg_angles = read_csv('talos_pickplace_jointpos_leg_left.csv')
    right_arm_angles = read_csv('talos_pickplace_jointpos_arm_right.csv')
    left_arm_angles = read_csv('talos_pickplace_jointpos_arm_left.csv')
    torso_angles = read_csv('talos_pickplace_jointpos_torso.csv')
    right_gripper_angles = read_csv('talos_pickplace_jointpos_gripper_right.csv')
    left_gripper_angles = read_csv('talos_pickplace_jointpos_gripper_right.csv')

    #adjust the position of the arms
    print("Adjusting arm configuration")
    start_time = rospy.get_rostime() + rospy.Duration(0.1)
    # TODO: ensure slow execution without jumps
    # TODO: Drive legs and torso to start position
    ra_controller.move_joint(start_time,[[0.000045, -0.149561, -0.000039, -0.100075, -0.000084, 0.000182, 0.00005]], [], []) 
    la_controller.move_joint(start_time,[[0.000033, 0.149549, -0.000092, -0.099945, 0.000041, -0.000121, 0.000177]], [], [])
    rospy.sleep(1.) # wait until motion finished and robot settled down

    print("Adjusting leg configuration")
    start_time = rospy.get_rostime() + rospy.Duration(0.1)
    # TODO: ensure slow execution without jumps
    # TODO: Drive legs and torso to start position
    rl_controller.move_joint(start_time,[[,,,,,,,]], [], []) 
    ll_controller.move_joint(start_time,[[,,,,,,,]], [], [])
    rospy.sleep(1.) # wait until motion finished and robot settled down
    
    raw_input("Press enter to start trajectory")
    start_time = rospy.get_rostime() + rospy.Duration(0.1)
    rl_controller.move_joint(start_time,right_leg_angles,[]*len(right_leg_angles),[]*len(right_leg_angles))
    ll_controller.move_joint(start_time,left_leg_angles,[]*len(left_leg_angles),[]*len(left_leg_angles))
    print("Trajectory uploaded")
    

if __name__ == '__main__':
      rospy.init_node('joint_position_tester')
      main()

