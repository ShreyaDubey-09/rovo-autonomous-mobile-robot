from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():

    bringup_dir = get_package_share_directory(
        'nav2_bringup'
    )

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

    # MAP FILE
    map_file = os.path.join(
        get_package_share_directory('rovo_bringup'),
        'maps',
        'amr_map.yaml'
    )

    # NAV2 PARAMS
    params_file = os.path.join(
        get_package_share_directory(
            'rovo_bringup'
        ),
        'config',
        'nav2_params.yaml'
    )

    # RVIZ
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

    # NAV2
    nav2 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                bringup_dir,
                'launch',
                'bringup_launch.py'
            )
        ),

        launch_arguments={
            'map': map_file,
            'use_sim_time': LaunchConfiguration('use_sim_time'),
            'params_file': params_file
        }.items()
    )

    return LaunchDescription([

        DeclareLaunchArgument(
            'use_sim_time',
            default_value='True'
        ),

        simulation,
        nav2,
        rviz

    ])
