from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            namespace="eyes_disp_system_node", 
            package='eyes_disp_system_node',
            executable='eyes_disp_system_node',
            output='screen',
            parameters=[{"port_name": '/dev/ttyACM0'}, {"bps_speed": 115200}]
        )
    ])