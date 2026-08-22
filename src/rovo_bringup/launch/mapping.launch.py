from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription

from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node

from ament_index_python.packages import get_package_share_directory

import os


def generate_launch_description():


    simulation = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory(
                    'rovo_bringup'
                ),
                'launch',
                'simulation.launch.py'
            )
        )
    )


    slam_params = os.path.join(
        get_package_share_directory(
            'rovo_gazebo'
        ),
        'config',
        'mapper_params_online_async.yaml'
    )


    slam = Node(
        package='slam_toolbox',
        executable='async_slam_toolbox_node',
        output='screen',
        parameters=[
            slam_params,
            {
                'use_sim_time': True
            }
        ]
    )


    rviz_config = os.path.join(
        get_package_share_directory(
            'rovo_bringup'
        ),
        'rviz',
        'rovo_nav.rviz'
    )


    rviz = Node(
        package='rviz2',
        executable='rviz2',
        arguments=[
            '-d',
            rviz_config
        ],
        output='screen'
    )


    return LaunchDescription([

        simulation,

        slam,

        rviz

    ])
