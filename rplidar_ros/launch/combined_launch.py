#!/usr/bin/env python3

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import LogInfo
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.actions import LifecycleNode


def generate_launch_description():
    # Lidar 1
    channel_type_1 =  LaunchConfiguration('channel_type_1', default='serial')
    serial_port_1 = LaunchConfiguration('serial_port_1', default='/dev/ttyUSB0')
    serial_baudrate_1 = LaunchConfiguration('serial_baudrate_1', default='256000')
    frame_id_1 = LaunchConfiguration('frame_id_1', default='lidar_link')
    inverted_1 = LaunchConfiguration('inverted_1', default='false')
    angle_compensate_1 = LaunchConfiguration('angle_compensate_1', default='true')
    scan_mode_1 = LaunchConfiguration('scan_mode_1', default='Sensitivity')

    # Lidar 2
    serial_port_2 = LaunchConfiguration('serial_port_2', default='/dev/tetra/lidar')
    serial_baudrate_2 = LaunchConfiguration('serial_baudrate_2', default='256000')
    frame_id_2 = LaunchConfiguration('frame_id_2', default='lidar_link')
    inverted_2 = LaunchConfiguration('inverted_2', default='false')
    angle_compensate_2 = LaunchConfiguration('angle_compensate_2', default='true')
    scan_mode_2 = LaunchConfiguration('scan_mode_2', default='Sensitivity')

    return LaunchDescription([

        # Lidar 1 arguments
        DeclareLaunchArgument(
            'channel_type_1',
            default_value=channel_type_1,
            description='Specifying channel type of lidar 1'),
        DeclareLaunchArgument(
            'serial_port_1',
            default_value=serial_port_1,
            description='Specifying usb port of lidar 1'),
        DeclareLaunchArgument(
            'serial_baudrate_1',
            default_value=serial_baudrate_1,
            description='Specifying usb port baudrate of lidar 1'),
        DeclareLaunchArgument(
            'frame_id_1',
            default_value=frame_id_1,
            description='Specifying frame_id of lidar 1'),
        DeclareLaunchArgument(
            'inverted_1',
            default_value=inverted_1,
            description='Specifying whether or not to invert scan data of lidar 1'),
        DeclareLaunchArgument(
            'angle_compensate_1',
            default_value=angle_compensate_1,
            description='Specifying whether or not to enable angle_compensate of scan data of lidar 1'),
        DeclareLaunchArgument(
            'scan_mode_1',
            default_value=scan_mode_1,
            description='Specifying scan mode of lidar 1'),

        # Lidar 2 arguments
        DeclareLaunchArgument(
            'serial_port_2',
            default_value=serial_port_2,
            description='Specifying usb port of lidar 2'),
        DeclareLaunchArgument(
            'serial_baudrate_2',
            default_value=serial_baudrate_2,
            description='Specifying usb port baudrate of lidar 2'),
        DeclareLaunchArgument(
            'frame_id_2',
            default_value=frame_id_2,
            description='Specifying frame_id of lidar 2'),
        DeclareLaunchArgument(
            'inverted_2',
            default_value=inverted_2,
            description='Specifying whether or not to invert scan data of lidar 2'),
        DeclareLaunchArgument(
            'angle_compensate_2',
            default_value=angle_compensate_2,
            description='Specifying whether or not to enable angle_compensate of scan data of lidar 2'),
        DeclareLaunchArgument(
            'scan_mode_2',
            default_value=scan_mode_2,
            description='Specifying scan mode of lidar 2'),

        # Lidar 1 node
        Node(
            package='rplidar_ros',
            executable='rplidar_node',
            name='rplidar_node',
            namespace='lidar_1',
            parameters=[{
                'channel_type': channel_type_1,
                'serial_port': serial_port_1,
                'serial_baudrate': serial_baudrate_1,
                'frame_id': frame_id_1,
                'inverted': inverted_1,
                'angle_compensate': angle_compensate_1
            }],
            output='screen'),

        # Lidar 2 node
        Node(
            package='ydlidar_ros2_driver',
            executable='ydlidar_ros2_driver_node',
            name='ydlidar_ros2_driver_node',
            namespace='lidar_2',
            parameters=[{
                'params_file': os.path.join(
                    get_package_share_directory('ydlidar_ros2_driver'), 'params', 'ydlidar.yaml'),
                'port': serial_port_2,
                'serial_baudrate': serial_baudrate_2,
                'frame_id': frame_id_2,
                'inverted': inverted_2,
                'angle_compensate': angle_compensate_2,
                'scan_mode': scan_mode_2
            }],
            output='screen'),

    ])
