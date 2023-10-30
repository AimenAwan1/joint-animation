#! /bin/bash

gnome-terminal --tab -- bash -c "rostopic pub /torso_controller/command trajectory_msgs/JointTrajectory '{joint_names:[], points:[]}'; exec bash -i"
gnome-terminal --tab -- bash -c "rostopic pub /right_arm_controller/command trajectory_msgs/JointTrajectory '{joint_names:[], points:[]}'; exec bash -i"
gnome-terminal --tab -- bash -c "rostopic pub /left_arm_controller/command trajectory_msgs/JointTrajectory '{joint_names:[], points:[]}'; exec bash -i"
gnome-terminal --tab -- bash -c "rostopic pub /right_gripper_controller/command trajectory_msgs/JointTrajectory '{joint_names:[], points:[]}'; exec bash -i"
gnome-terminal --tab -- bash -c "rostopic pub /left_gripper_controller/command trajectory_msgs/JointTrajectory '{joint_names:[], points:[]}'; exec bash -i"
gnome-terminal --tab -- bash -c "rostopic pub /right_leg_controller/command trajectory_msgs/JointTrajectory '{joint_names:[], points:[]}'; exec bash -i"
gnome-terminal --tab -- bash -c "rostopic pub /left_leg_controller/command trajectory_msgs/JointTrajectory '{joint_names:[], points:[]}'; exec bash -i"

#gnome-terminal --tab -- "rostopic pub /torso_controller/command trajectory_msgs/JointTrajectory '{joint_names:[], points:[]}'" #; exec bash -i"
#gnome-terminal --tab -- "rostopic pub /right_arm_controller/command trajectory_msgs/JointTrajectory '{joint_names:[], points:[]}'" #; exec bash -i"
#gnome-terminal --tab -- "rostopic pub /left_arm_controller/command trajectory_msgs/JointTrajectory '{joint_names:[], points:[]}'" #; exec bash -i"
#gnome-terminal --tab -- "rostopic pub /right_gripper_controller/command trajectory_msgs/JointTrajectory '{joint_names:[], points:[]}'" #; exec bash -i"
#gnome-terminal --tab -- "rostopic pub /left_gripper_controller/command trajectory_msgs/JointTrajectory '{joint_names:[], points:[]}'" #; exec bash -i"
#gnome-terminal --tab -- "rostopic pub /right_leg_controller/command trajectory_msgs/JointTrajectory '{joint_names:[], points:[]}'" #; exec bash -i"
#gnome-terminal --tab -- "rostopic pub /left_leg_controller/command trajectory_msgs/JointTrajectory '{joint_names:[], points:[]}'" #; exec bash -i"
