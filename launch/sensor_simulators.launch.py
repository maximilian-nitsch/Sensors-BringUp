"""@license BSD-3 https://opensource.org/licenses/BSD-3-Clause
Copyright (c) 2024, Institute of Automatic Control - RWTH Aachen University
Maximilian Nitsch (m.nitsch@irt.rwth-aachen.de)
All rights reserved.
"""
import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    # Get the path to the launch files you want to include
    imu_sim_launch_file = os.path.join(
        get_package_share_directory('imu_simulator_package'),
        'launch', 'imu_simulator.launch.py'
    )
    mag_sim_launch_file = os.path.join(
        get_package_share_directory('mag_simulator_package'),
        'launch', 'mag_simulator.launch.py'
    )
    usbl_sim_launch_file = os.path.join(
        get_package_share_directory('usbl_simulator_package'),
        'launch', 'usbl_simulator.launch.py'
    )
    dvl_sim_launch_file = os.path.join(
        get_package_share_directory('dvl_simulator_package'),
        'launch', 'dvl_simulator.launch.py'
    )
    dpth_sim_launch_file = os.path.join(
        get_package_share_directory('dpth_sensor_simulator_package'),
        'launch', 'dpth_sensor_simulator.launch.py'
    )

    # Create IncludeLaunchDescription actions to include the launch files
    include_imu_simulator_package_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(imu_sim_launch_file)
    )
    include_mag_simulator_package_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(mag_sim_launch_file)
    )

    include_usbl_simulator_package_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(usbl_sim_launch_file)
    )

    include_dvl_simulator_package_launch = IncludeLaunchDescription( 
        PythonLaunchDescriptionSource(dvl_sim_launch_file)
    )

    include_dpth_simulator_package_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(dpth_sim_launch_file)
    )

    # Create the main launch description
    ld = LaunchDescription()

    # Add the IncludeLaunchDescription actions to the launch description
    ld.add_action(include_imu_simulator_package_launch)
    ld.add_action(include_mag_simulator_package_launch)
    ld.add_action(include_usbl_simulator_package_launch)
    ld.add_action(include_dvl_simulator_package_launch)
    ld.add_action(include_dpth_simulator_package_launch)

    return ld
