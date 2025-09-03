# generate MJCF file from onshape CAD project

import argparse
import json
import os
from pathlib import Path
import shutil


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Script to generate URDF file from onshape CAD project.",
    )
    parser.add_argument(
        "--config",
        type=str,
        help="Path to the config file.",
        default="./data/robots/berkeley_humanoid/berkeley_humanoid_lite/mjcf/config.json",
    )
    args = parser.parse_args()

    # check if the config file exists
    config_file_path = Path(args.config)
    if not config_file_path.exists():
        raise FileNotFoundError(f"Config file {config_file_path} does not exist!")

    robot_name = json.load(open(config_file_path))["output_filename"]
    mjcf_dir = config_file_path.parent
    robot_dir = mjcf_dir.parent
    scad_dir = robot_dir / "scad"

    # copy all the predefined scad files to the mjcf assets directory
    # for onshape-to-robot to generate custom colliders
    if scad_dir.exists():
        # Create assets directory if it doesn't exist
        assets_dir = mjcf_dir / "assets"
        assets_dir.mkdir(exist_ok=True)

        for file in scad_dir.iterdir():
            shutil.copy(file, assets_dir / file.name)

    # invoke onshape-to-robot to generate the mjcf file
    os.system(f"onshape-to-robot {mjcf_dir}")

    # copy everything under merged/ directory to the assets directory
    if (mjcf_dir / "assets" / "merged").exists():
        shutil.copytree(
            mjcf_dir / "assets" / "merged",
            robot_dir / "meshes",
            dirs_exist_ok=True,
        )

    # delete the assets directory
    shutil.rmtree(mjcf_dir / "assets")

    # modify the mjcf to use the mesh from the parent meshes directory
    with open(mjcf_dir / f"{robot_name}.xml", "r") as file:
        content = file.read()

    content = content.replace("assets/merged/", "../meshes/")

    content = content.replace("</actuator>", """</actuator>

  <sensor>
    <jointpos name="arm_left_shoulder_pitch_pos"  joint="arm_left_shoulder_pitch_joint"/>
    <jointpos name="arm_left_shoulder_roll_pos"   joint="arm_left_shoulder_roll_joint"/>
    <jointpos name="arm_left_shoulder_yaw_pos"    joint="arm_left_shoulder_yaw_joint"/>
    <jointpos name="arm_left_elbow_pitch_pos"     joint="arm_left_elbow_pitch_joint"/>
    <jointpos name="arm_left_elbow_roll_pos"      joint="arm_left_elbow_roll_joint"/>
    <jointpos name="arm_right_shoulder_pitch_pos" joint="arm_right_shoulder_pitch_joint"/>
    <jointpos name="arm_right_shoulder_roll_pos"  joint="arm_right_shoulder_roll_joint"/>
    <jointpos name="arm_right_shoulder_yaw_pos"   joint="arm_right_shoulder_yaw_joint"/>
    <jointpos name="arm_right_elbow_pitch_pos"    joint="arm_right_elbow_pitch_joint"/>
    <jointpos name="arm_right_elbow_roll_pos"     joint="arm_right_elbow_roll_joint"/>
    <jointpos name="leg_left_hip_roll_pos"        joint="leg_left_hip_roll_joint"/>
    <jointpos name="leg_left_hip_yaw_pos"         joint="leg_left_hip_yaw_joint"/>
    <jointpos name="leg_left_hip_pitch_pos"       joint="leg_left_hip_pitch_joint"/>
    <jointpos name="leg_left_knee_pitch_pos"      joint="leg_left_knee_pitch_joint"/>
    <jointpos name="leg_left_ankle_pitch_pos"     joint="leg_left_ankle_pitch_joint"/>
    <jointpos name="leg_left_ankle_roll_pos"      joint="leg_left_ankle_roll_joint"/>
    <jointpos name="leg_right_hip_roll_pos"       joint="leg_right_hip_roll_joint"/>
    <jointpos name="leg_right_hip_yaw_pos"        joint="leg_right_hip_yaw_joint"/>
    <jointpos name="leg_right_hip_pitch_pos"      joint="leg_right_hip_pitch_joint"/>
    <jointpos name="leg_right_knee_pitch_pos"     joint="leg_right_knee_pitch_joint"/>
    <jointpos name="leg_right_ankle_pitch_pos"    joint="leg_right_ankle_pitch_joint"/>
    <jointpos name="leg_right_ankle_roll_pos"     joint="leg_right_ankle_roll_joint"/>

    <jointvel name="arm_left_shoulder_pitch_vel"  joint="arm_left_shoulder_pitch_joint"/>
    <jointvel name="arm_left_shoulder_roll_vel"   joint="arm_left_shoulder_roll_joint"/>
    <jointvel name="arm_left_shoulder_yaw_vel"    joint="arm_left_shoulder_yaw_joint"/>
    <jointvel name="arm_left_elbow_pitch_vel"     joint="arm_left_elbow_pitch_joint"/>
    <jointvel name="arm_left_elbow_roll_vel"      joint="arm_left_elbow_roll_joint"/>
    <jointvel name="arm_right_shoulder_pitch_vel" joint="arm_right_shoulder_pitch_joint"/>
    <jointvel name="arm_right_shoulder_roll_vel"  joint="arm_right_shoulder_roll_joint"/>
    <jointvel name="arm_right_shoulder_yaw_vel"   joint="arm_right_shoulder_yaw_joint"/>
    <jointvel name="arm_right_elbow_pitch_vel"    joint="arm_right_elbow_pitch_joint"/>
    <jointvel name="arm_right_elbow_roll_vel"     joint="arm_right_elbow_roll_joint"/>
    <jointvel name="leg_left_hip_roll_vel"        joint="leg_left_hip_roll_joint"/>
    <jointvel name="leg_left_hip_yaw_vel"         joint="leg_left_hip_yaw_joint"/>
    <jointvel name="leg_left_hip_pitch_vel"       joint="leg_left_hip_pitch_joint"/>
    <jointvel name="leg_left_knee_pitch_vel"      joint="leg_left_knee_pitch_joint"/>
    <jointvel name="leg_left_ankle_pitch_vel"     joint="leg_left_ankle_pitch_joint"/>
    <jointvel name="leg_left_ankle_roll_vel"      joint="leg_left_ankle_roll_joint"/>
    <jointvel name="leg_right_hip_roll_vel"       joint="leg_right_hip_roll_joint"/>
    <jointvel name="leg_right_hip_yaw_vel"        joint="leg_right_hip_yaw_joint"/>
    <jointvel name="leg_right_hip_pitch_vel"      joint="leg_right_hip_pitch_joint"/>
    <jointvel name="leg_right_knee_pitch_vel"     joint="leg_right_knee_pitch_joint"/>
    <jointvel name="leg_right_ankle_pitch_vel"    joint="leg_right_ankle_pitch_joint"/>
    <jointvel name="leg_right_ankle_roll_vel"     joint="leg_right_ankle_roll_joint"/>

    <jointactuatorfrc name="arm_left_shoulder_pitch_torque"   joint="arm_left_shoulder_pitch_joint"/>
    <jointactuatorfrc name="arm_left_shoulder_roll_torque"    joint="arm_left_shoulder_roll_joint"/>
    <jointactuatorfrc name="arm_left_shoulder_yaw_torque"     joint="arm_left_shoulder_yaw_joint"/>
    <jointactuatorfrc name="arm_left_elbow_pitch_torque"      joint="arm_left_elbow_pitch_joint"/>
    <jointactuatorfrc name="arm_left_elbow_roll_torque"       joint="arm_left_elbow_roll_joint"/>
    <jointactuatorfrc name="arm_right_shoulder_pitch_torque"  joint="arm_right_shoulder_pitch_joint"/>
    <jointactuatorfrc name="arm_right_shoulder_roll_torque"   joint="arm_right_shoulder_roll_joint"/>
    <jointactuatorfrc name="arm_right_shoulder_yaw_torque"    joint="arm_right_shoulder_yaw_joint"/>
    <jointactuatorfrc name="arm_right_elbow_pitch_torque"     joint="arm_right_elbow_pitch_joint"/>
    <jointactuatorfrc name="arm_right_elbow_roll_torque"      joint="arm_right_elbow_roll_joint"/>
    <jointactuatorfrc name="leg_left_hip_roll_torque"         joint="leg_left_hip_roll_joint"/>
    <jointactuatorfrc name="leg_left_hip_yaw_torque"          joint="leg_left_hip_yaw_joint"/>
    <jointactuatorfrc name="leg_left_hip_pitch_torque"        joint="leg_left_hip_pitch_joint"/>
    <jointactuatorfrc name="leg_left_knee_pitch_torque"       joint="leg_left_knee_pitch_joint"/>
    <jointactuatorfrc name="leg_left_ankle_pitch_torque"      joint="leg_left_ankle_pitch_joint"/>
    <jointactuatorfrc name="leg_left_ankle_roll_torque"       joint="leg_left_ankle_roll_joint"/>
    <jointactuatorfrc name="leg_right_hip_roll_torque"        joint="leg_right_hip_roll_joint"/>
    <jointactuatorfrc name="leg_right_hip_yaw_torque"         joint="leg_right_hip_yaw_joint"/>
    <jointactuatorfrc name="leg_right_hip_pitch_torque"       joint="leg_right_hip_pitch_joint"/>
    <jointactuatorfrc name="leg_right_knee_pitch_torque"      joint="leg_right_knee_pitch_joint"/>
    <jointactuatorfrc name="leg_right_ankle_pitch_torque"     joint="leg_right_ankle_pitch_joint"/>
    <jointactuatorfrc name="leg_right_ankle_roll_torque"      joint="leg_right_ankle_roll_joint"/>

    <framequat name="imu_quat" objtype="site" objname="imu" />
    <gyro name="imu_gyro" site="imu" />
    <accelerometer name="imu_acc" site="imu" />
    <framepos name="frame_pos" objtype="site" objname="imu" />
    <framelinvel name="frame_vel" objtype="site" objname="imu" />
  </sensor>""")

    with open(mjcf_dir / f"{robot_name}.xml", "w") as file:
        file.write(content)
