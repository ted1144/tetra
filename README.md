## port setup

```bash
cd ~/ros2_ws/src/tetra
sudo chmod 777 initenv.sh
sudo ./initenv.sh
```

## Robot Bringup

```bash
ros2 launch tetra tetra_configuration.launch.py
```

## SLAM

```bash
ros2 launch tetra_cartographer cartographer_slam.launch.py
```

## NAVI

```bash
ros2 launch tetra_nav2 nav2.launch.py
```