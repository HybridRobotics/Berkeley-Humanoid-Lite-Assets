# Copyright (c) 2025, The Berkeley Humanoid Lite Project Developers.

import os

import isaaclab.sim as sim_utils
from isaaclab.actuators import ImplicitActuatorCfg
from isaaclab.assets.articulation import ArticulationCfg

ISAACLAB_ASSET_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "data"))


AIR_HUMANOID_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAACLAB_ASSET_DIR}/usd/air_humanoid.usd",
        activate_contact_sensors=True,
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            disable_gravity=False,
            retain_accelerations=False,
            linear_damping=0.0,
            angular_damping=0.0,
            max_linear_velocity=1000.0,
            max_angular_velocity=1000.0,
            max_depenetration_velocity=1.0,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=False, solver_position_iteration_count=8, solver_velocity_iteration_count=4
        ),
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.6),
        joint_pos={
            "arm_left_shoulder_pitch_joint": 0.0,
            "arm_left_shoulder_roll_joint": 0.0,
            "arm_left_shoulder_yaw_joint": 0.0,
            "arm_left_elbow_pitch_joint": 0.0,
            "arm_left_wrist_yaw_joint": 0.0,
            "arm_right_shoulder_pitch_joint": 0.0,
            "arm_right_shoulder_roll_joint": 0.0,
            "arm_right_shoulder_yaw_joint": 0.0,
            "arm_right_elbow_pitch_joint": 0.0,
            "arm_right_wrist_yaw_joint": 0.0,
            "leg_left_hip_roll_joint": 0.0,
            "leg_left_hip_yaw_joint": 0.0,
            "leg_left_hip_pitch_joint": 0.0,
            "leg_left_knee_pitch_joint": 0.0,
            "leg_left_ankle_yaw_joint": 0.0,
            "leg_left_ankle_pitch_joint": 0.0,
            "leg_left_ankle_roll_joint": 0.0,
            "leg_right_hip_roll_joint": 0.0,
            "leg_right_hip_yaw_joint": 0.0,
            "leg_right_hip_pitch_joint": 0.0,
            "leg_right_knee_pitch_joint": 0.0,
            "leg_right_ankle_yaw_joint": 0.0,
            "leg_right_ankle_pitch_joint": 0.0,
            "leg_right_ankle_roll_joint": 0.0,
            "neck_yaw_joint": 0.0,
            "waist_yaw_joint": 0.0,
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=0.9,
    actuators={
        "arms": ImplicitActuatorCfg(
            joint_names_expr=[
                "arm_.*_shoulder_.*_joint",
                "arm_.*_elbow_.*_joint",
                "arm_.*_wrist_.*_joint",
            ],
            effort_limit=14,
            velocity_limit=27.0,
            stiffness=40,
            damping=2,
            armature=0.002,
        ),
        "legs": ImplicitActuatorCfg(
            joint_names_expr=[
                "leg_.*_hip_.*_joint",
                "leg_.*_knee_.*_joint",
            ],
            effort_limit=17,
            velocity_limit=28.0,
            stiffness=40,
            damping=2,
            armature=0.007,
        ),
        "ankles": ImplicitActuatorCfg(
            joint_names_expr=[
                "leg_.*_ankle_.*_joint",
            ],
            effort_limit=14,
            velocity_limit=27.0,
            stiffness=40,
            damping=2,
            armature=0.002,
        ),
        "neck": ImplicitActuatorCfg(
            joint_names_expr=[
                "neck_.*_joint",
            ],
            effort_limit=14,
            velocity_limit=27.0,
            stiffness=40,
            damping=2,
            armature=0.002,
        ),
        "waist": ImplicitActuatorCfg(
            joint_names_expr=[
                "waist_.*_joint",
            ],
            effort_limit=14,
            velocity_limit=27.0,
            stiffness=40,
            damping=2,
            armature=0.002,
        ),
    },
)
"""Configuration for the Air Humanoid robot."""


AIR_HUMANOID_JOINTS = [name for name in AIR_HUMANOID_CFG.init_state.joint_pos.keys()]