#! /bin/bash

gnome-terminal --tab -- bash "rostopic pub /torso_controller/command trajectory_msgs/JointTrajectory '{joint_names:[], points:[]}'"
gnome-terminal --tab -- bash "rostopic pub /right_arm_controller/command trajectory_msgs/JointTrajectory '{joint_names:[], points:[]}'"
gnome-terminal --tab -- bash "rostopic pub /left_arm_controller/command trajectory_msgs/JointTrajectory '{joint_names:[], points:[]}'"
gnome-terminal --tab -- bash "rostopic pub /right_gripper_controller/command trajectory_msgs/JointTrajectory '{joint_names:[], points:[]}'"
gnome-terminal --tab -- bash "rostopic pub /left_gripper_controller/command trajectory_msgs/JointTrajectory '{joint_names:[], points:[]}'"
gnome-terminal --tab -- bash "rostopic pub /right_leg_controller/command trajectory_msgs/JointTrajectory '{joint_names:[], points:[]}'"
gnome-terminal --tab -- bash "rostopic pub /left_leg_controller/command trajectory_msgs/JointTrajectory '{joint_names:[], points:[]}'"

#gnome-terminal --tab -- "rostopic pub /torso_controller/command trajectory_msgs/JointTrajectory '{joint_names:[], points:[]}'" #; exec bash -i"
#gnome-terminal --tab -- "rostopic pub /right_arm_controller/command trajectory_msgs/JointTrajectory '{joint_names:[], points:[]}'" #; exec bash -i"
#gnome-terminal --tab -- "rostopic pub /left_arm_controller/command trajectory_msgs/JointTrajectory '{joint_names:[], points:[]}'" #; exec bash -i"
#gnome-terminal --tab -- "rostopic pub /right_gripper_controller/command trajectory_msgs/JointTrajectory '{joint_names:[], points:[]}'" #; exec bash -i"
#gnome-terminal --tab -- "rostopic pub /left_gripper_controller/command trajectory_msgs/JointTrajectory '{joint_names:[], points:[]}'" #; exec bash -i"
#gnome-terminal --tab -- "rostopic pub /right_leg_controller/command trajectory_msgs/JointTrajectory '{joint_names:[], points:[]}'" #; exec bash -i"
#gnome-terminal --tab -- "rostopic pub /left_leg_controller/command trajectory_msgs/JointTrajectory '{joint_names:[], points:[]}'" #; exec bash -i"
