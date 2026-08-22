from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction, RegisterEventHandler
from launch.event_handlers import OnProcessStart
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch.substitutions import Command
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue

from ament_index_python.packages import get_package_share_directory

import os


def generate_launch_description():

    world = os.path.join(
        get_package_share_directory('rovo_gazebo'),
        'worlds',
        'amr_world.world'
    )

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('gazebo_ros'),
                'launch',
                'gazebo.launch.py'
            )
        ),
        launch_arguments={
            'world': world
        }.items()
    )

    xacro_file = os.path.join(
        get_package_share_directory('rovo_description'),
        'urdf',
        'robot.urdf.xacro'
    )

    robot_description = ParameterValue(
        Command([
            'xacro',
            ' ',
            xacro_file
        ]),
        value_type=str
    )

    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[
            {
                'robot_description': robot_description,
                'use_sim_time': True
            }
        ],
        output='screen'
    )

    spawn_robot = TimerAction(
        period=5.0,
        actions=[
            Node(
                package='gazebo_ros',
                executable='spawn_entity.py',
                arguments=[
                    '-topic',
                    'robot_description',
                    '-entity',
                    'rovo_robot'
                ],
                output='screen'
            )
        ]
    )

    delayed_spawn = RegisterEventHandler(
        OnProcessStart(
            target_action=robot_state_publisher,
            on_start=[
                spawn_robot
            ]
        )
    )

    return LaunchDescription([
        gazebo,
        robot_state_publisher,
        delayed_spawn
    ])
