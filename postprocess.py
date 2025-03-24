import argparse


def postprocess_urdf(name):
    urdf_path = f"data/urdf/{name}.urdf"
    with open(urdf_path, "r") as f:
        content = f.read()

    # update URDF mesh directory
    content = content.replace("package://", "./")

    with open(urdf_path, "w") as f:
        f.write(content)
    
    print("Postprocessing URDF complete")


def postprocess_mjcf(name):
    mjcf_path = f"data/mjcf/{name}.xml"
    with open(mjcf_path, "r") as f:
        content = f.read()

    sensor_content = """
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
  </sensor>
"""
    content = content.replace("<equality/>", sensor_content+"<equality/>")

    with open(mjcf_path, "w") as f:
        f.write(content)
    
    print("Postprocessing MJCF complete")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", type=str, default="urdf")
    parser.add_argument("--name", type=str, default="berkeley-humanoid-lite")
    args = parser.parse_args()

    if args.mode == "urdf":
        postprocess_urdf(args.name)
    elif args.mode == "mjcf":
        postprocess_mjcf(args.name)
    else:
        raise ValueError("Invalid mode: {0}".format(args.mode))
