#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# flake8: noqa
#
# Copyright 2023 Herman Ye @Auromix
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Description:
# This launch file is a part of ROS-LLM project developed to control and interact with the turtlesim robot or your own robot.
# The launch file contains a LaunchDescription object which defines the ROS2 nodes to be executed.
# 
# Node test Method:
# ros2 launch llm_bringup chatgpt_with_turtle_robot.launch.py
# ros2 topic pub /llm_state std_msgs/msg/String "data: 'listening'" -1

# Author: Herman Ye @Auromix

from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    return LaunchDescription(
        [
            Node(
                package="llm_model",
                executable="chatgpt",
                name="chatgpt",
                output="screen",
            ),
            Node(
                package="llm_robot",
                executable="turtle_robot",
                name="turtle_robot",
                output="screen",
            ),
            Node(
                package="turtlesim",
                executable="turtlesim_node",
                name="turtlesim_node",
                output="screen",
            ),
        ]
    )
