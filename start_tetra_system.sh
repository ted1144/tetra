#!/bin/bash

# Tetra configuration launch
echo "Launching Tetra configuration..."
gnome-terminal -- ros2 launch tetra tetra_configuration.launch.py

# Waiting for Tetra configuration to launch (adjust the sleep time as needed)
sleep 5

# NAVI launch
echo "Launching NAVI..."
gnome-terminal -- ros2 launch tetra_nav2 nav2.launch.py

# TTS server launch
echo "Launching TTS server..."
gnome-terminal -- ros2 launch bmkbot_io bmkbot_io.launch.py

# FlexBE launch
echo "Launching FlexBE..."
gnome-terminal -- ros2 launch flexbe_app flexbe_full.launch.py

# GUI launch
echo "Launching GUI..."
gnome-terminal -- ros2 launch bmkbot_gui bmkbot_gui.launch.py

