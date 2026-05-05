from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Rosbridge WebSocket server
        Node(
            package='rosbridge_server',
            executable='rosbridge_websocket',
            name='rosbridge_websocket',
            output='screen',
            parameters=[{'port': 9090}]
        ),

        # rosapi for topic/service introspection
        Node(
            package='rosapi',
            executable='rosapi_node',
            name='rosapi',
            output='screen'
        ),

        # RosClaw agent
        Node(
            package='rosclaw_agent',
            executable='agent',
            name='rosclaw_agent',
            output='screen'
        ),

        # RosClaw discovery node
        Node(
            package='rosclaw_discovery',
            executable='discovery',
            name='rosclaw_discovery',
            output='screen'
        ),
    ])
