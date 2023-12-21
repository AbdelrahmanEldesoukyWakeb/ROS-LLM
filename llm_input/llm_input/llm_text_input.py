#!/usr/bin/env python

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class ChatGpt_Input(Node):
    def __init__(self):
        super().__init__('ChatGpt_Input')
        self.publisher = self.create_publisher(String, 'llm_input_audio_to_text', 10)
        self.timer = self.create_timer(5.0, self.publish_terminal_input)

    def publish_terminal_input(self):
        user_input = input('Enter a message for ChatGpt 3.5 turbo: ')
        msg = String()
        msg.data = user_input
        self.publisher.publish(msg)
        self.get_logger().info(f'Published: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = ChatGpt_Input()
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
