#!/bin/bash

# Split the input CSV file into 7 output files
cut -d ',' -f 1-6,32 talos_pickplace_jointpos.csv > talos_pickplace_jointpos_arm_left.csv
cut -d ',' -f 8-14,32 talos_pickplace_jointpos.csv > talos_pickplace_jointpos_arm_right.csv
cut -d ',' -f 15,32 talos_pickplace_jointpos.csv > talos_pickplace_jointpos_gripper_left.csv
cut -d ',' -f 16,32 talos_pickplace_jointpos.csv > talos_pickplace_jointpos_gripper_right.csv
cut -d ',' -f 19-24,32 talos_pickplace_jointpos.csv > talos_pickplace_jointpos_leg_left.csv
cut -d ',' -f 25-30,32 talos_pickplace_jointpos.csv > talos_pickplace_jointpos_leg_right.csv
cut -d ',' -f 31-32 talos_pickplace_jointpos.csv > talos_pickplace_jointpos_torso.csv

# Add a column of zeros to each output file
#for file in talos_pickplace_jointpos_*.csv; do
   # awk -F, '{$(NF+1)=0;}1' OFS=, "$file" > "$file.tmp" && mv "$file.tmp" "$file"
#done

# Display a message to indicate completion
echo "CSV file successfully split into 7 output files"

