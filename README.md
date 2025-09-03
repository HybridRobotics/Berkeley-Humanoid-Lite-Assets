# Berkeley Humanoid Lite Assets

This repository contains the assets files and tools necessary for working with the Berkeley Humanoid Lite model. It includes scripts for generating URDF files from Onshape and converting them to MJCF and USD formats to use in multiple simulators.


## Generate description file from Onshape

To export the Onshape design as URDF/MJCF file, we will be using the onshape-to-robot tool.

First, we need to install the necessary system dependencies:

```bash
sudo apt install openscad meshlab
```

Then, run the corresponding export script:

For URDF:

```bash
uv run ./scripts/export_onshape_to_urdf.py --config ./data/robots/berkeley_humanoid/berkeley_humanoid_lite/urdf/config.json
```

For MJCF

```bash
uv run ./scripts/export_onshape_to_mjcf.py --config ./data/robots/berkeley_humanoid/berkeley_humanoid_lite/mjcf/config.json
```

> **Note**
>
> Before running the script, make sure that the robot in the OnShape project is configured correctly, and all joints are at reset position.

The resulting URDF will be generated at `/data/robots/berkeley_humanoid/berkeley_humanoid_lite/urdf/`, MJCF will be generated at `/data/robots/berkeley_humanoid/berkeley_humanoid_lite/mjcf/`, and the STL meshes will be shared under `/data/robots/berkeley_humanoid/berkeley_humanoid_lite/meshes/`.


### Cleaning onshape-to-robot cache

Run the following command to clear the CAD file cache.

```bash
onshape-to-robot-clear-cache
```


## Convert URDF to USD

To generate USD file from URDF file, simply run the following command.

```bash
uv run ./scripts/convert_urdf_to_usd.py ./data/robots/berkeley_humanoid/berkeley_humanoid_lite/urdf/berkeley_humanoid_lite.urdf 
```


## Axis Convention

We follow the ROS [REP-0103](https://www.ros.org/reps/rep-0103.html) standard for the frame and axis convention.

The forward direction of the robot is positive `X` axis, and the left direction is positive `Y` axis. The robot is standing still on a flat surface, with the `Z` axis pointing upwards.

The joint axis are defined to be pointing in the same direction as the robot's reference frame.


## Degree of Freedoms

| Joint ID | Name                           | CAN ID | Range      | Description                                                                                               |
| -------- | ------------------------------ | ------ | ---------- | --------------------------------------------------------------------------------------------------------- |
|  **Left Arm**                           | |        |            |                                                                                                           |
| 0        | arm_left_shoulder_pitch_joint  | 1      | [-90, 45]  | controls the flexion/extension (pitch) motion of the left upper arm. Positive is flexion                  |
| 1        | arm_left_shoulder_roll_joint   | 3      | [0, 90]    | controls the abduction/adduction (yaw) motion of the left upper arm. Positive is adduction                |
| 2        | arm_left_shoulder_yaw_joint    | 5      | [-45, 45]  | controls the rotation (roll) motion of the left upper arm. Positive is lateral rotation                   |
| 3        | arm_left_elbow_pitch_joint     | 7      | [-90, 0]   | controls the flexion/extension (pitch) motion of the left forearm. Positive is extension                  |
| 4        | arm_left_elbow_roll_joint      | 9      | [-45, 45]  | controls the rotation (roll) motion of the left forearm. Positive is lateral rotation                     |
|  **Right Arm**                          | |        |            |                                                                                                           |
| 5        | arm_right_shoulder_pitch_joint | 2      | [-45, 90]  | controls the flexion/extension (pitch) motion of the right upper arm. Positive is extension               |
| 6        | arm_right_shoulder_roll_joint  | 4      | [-90, 0]   | controls the abduction/adduction (yaw) motion of the right upper arm. Positive is abduction               |
| 7        | arm_right_shoulder_yaw_joint   | 6      | [-45, 45]  | controls the rotation (roll) motion of the right upper arm. Positive is medial rotation                   |
| 8        | arm_right_elbow_pitch_joint    | 8      | [-90, 0]   | controls the flexion/extension (pitch) motion of the right forearm. Positive is flexion                   |
| 9        | arm_right_elbow_roll_joint     | 10     | [-45, 45]  | controls the rotation (roll) motion of the right forearm. Positive is medial rotation                     |
|  **Left Leg**                             |        |            |                                                                                                           |
| 10       | leg_left_hip_roll_joint        | 1      | [-10, 90]  | controls the flexion/extension (pitch) motion of the left thigh. Positive is flexion                      |
| 11       | leg_left_hip_yaw_joint         | 3      | [-33.75, 56.25]  | controls the abduction/adduction (yaw) motion of the left thigh. Positive is adduction              |
| 12       | leg_left_hip_pitch_joint       | 5      | [-108.75, 56.25] | controls the rotation (roll) motion of the left thigh. Positive is lateral rotation                 |
| 13       | leg_left_knee_pitch_joint      | 7      | [0, 140]   | controls the flexion/extension (pitch) motion of the left shin. Positive is extension                     |
| 14       | leg_left_ankle_pitch_joint     | 11     | [-45, 45]  | controls the rotation (roll) motion of the left shin. Positive is lateral rotation                        |
| 15       | leg_left_ankle_roll_joint      | 13     | [-15, 15]  | controls the inversion / eversion (roll) motion of the left foot. Positive is eversion                    |
| **Right Leg**                             |        |            |                                                                                                           |
| 16       | leg_right_hip_roll_joint       | 2      | [-90, 10]  | controls the flexion/extension (pitch) motion of the right thigh. Positive is extension                   |
| 17       | leg_right_hip_yaw_joint        | 4      | [-56.25, 33.75]  | controls the abduction/adduction (yaw) motion of the right thigh. Positive is abduction             |
| 18       | leg_right_hip_pitch_joint      | 6      | [-56.25, 108.75] | controls the rotation (roll) motion of the right thigh. Positive is medial rotation                 |
| 19       | leg_right_knee_pitch_joint     | 8      | [0, 140]  | controls the flexion/extension (pitch) motion of the right shin. Positive is flexion                       |
| 20       | leg_right_ankle_pitch_joint    | 12     | [-45, 45]  | controls the rotation (roll) motion of the right shin. Positive is medial rotation                        |
| 21       | leg_right_ankle_roll_joint     | 14     | [-15, 15]  | controls the inversion / eversion (roll) motion of the right foot. Positive is inversion                  |


> **Info**
>
> The descriptions are based from [this reference](https://courses.lumenlearning.com/suny-ap1/chapter/types-of-body-movements/).

