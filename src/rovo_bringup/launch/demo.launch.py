from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription

from launch.launch_description_sources import PythonLaunchDescriptionSource

from ament_index_python.packages import get_package_share_directory

import os


def generate_launch_description():

    bringup_dir = get_package_share_directory(
        'rovo_bringup'
    )

    navigation_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                bringup_dir,
                'launch',
                'navigation.launch.py'
            )
        )
    )


    return LaunchDescription([
        navigation_launch
    ])
