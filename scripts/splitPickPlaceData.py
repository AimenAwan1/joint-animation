#!/usr/bin/env python
import pandas as pd

# Load the original CSV file without header
original_df = pd.read_csv("~/robohub/julie/talos_public_ws/src/joint_animation_tutorial/scripts/merged_data.csv", header=None)

# Copy columns 1-7
left_arm_df = original_df.iloc[:, 0:7].copy()
left_arm_df['Row'] = range(1, len(left_arm_df) + 1)
left_arm_df.to_csv("talos_pickplace_jointpos_arm_left.csv", index=False, header=False)

# Copy columns 8-14
right_arm_df = original_df.iloc[:, 7:14].copy()
right_arm_df['Row'] = range(1, len(right_arm_df) + 1)
right_arm_df.to_csv("talos_pickplace_jointpos_arm_right.csv", index=False, header=False)

# Copy column 15
left_gripper_df = original_df.iloc[:, 14].copy().to_frame()
left_gripper_df['Row'] = range(1, len(left_gripper_df) + 1)
left_gripper_df.to_csv("talos_pickplace_jointpos_gripper_left.csv", index=False, header=False)

# Copy column 16
right_gripper_df = original_df.iloc[:, 15].copy().to_frame()
right_gripper_df['Row'] = range(1, len(right_gripper_df) + 1)
right_gripper_df.to_csv("talos_pickplace_jointpos_gripper_right.csv", index=False, header=False)

# Copy columns 19-24
left_leg_df = original_df.iloc[:, 18:24].copy()
left_leg_df['Row'] = range(1, len(left_leg_df) + 1)
left_leg_df.to_csv("talos_pickplace_jointpos_leg_left.csv", index=False, header=False)

# Copy columns 25-30
right_leg_df = original_df.iloc[:, 24:30].copy()
right_leg_df['Row'] = range(1, len(right_leg_df) + 1)
right_leg_df.to_csv("talos_pickplace_jointpos_leg_right.csv", index=False, header=False)

# Copy columns 31-32
torso_df = original_df.iloc[:, 30:32].copy()
torso_df['Row'] = range(1, len(torso_df) + 1)
torso_df.to_csv("talos_pickplace_jointpos_torso.csv", index=False, header=False)


