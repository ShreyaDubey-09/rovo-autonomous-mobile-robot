🤖 Rovo — Autonomous Mobile Robot

Rovo is a ROS 2-based Autonomous Mobile Robot (AMR) simulation that I built to explore different parts of a robotics software stack — from robot modeling and Gazebo simulation to LiDAR, SLAM, localization, TF, RViz2, and Nav2 navigation.

The goal of this project wasn't just to make a robot move. I wanted to understand what is actually happening behind the scenes and learn how to systematically debug the system when things don't work as expected.

This project became a hands-on way for me to understand how the different components of a ROS 2 navigation stack work together.

📌 Project Overview

Rovo is a differential-drive mobile robot simulated in a warehouse-style environment.

Technologies Used
ROS 2 Humble
Gazebo Classic
RViz2
URDF / Xacro
LiDAR
SLAM Toolbox
AMCL
Navigation2 (Nav2)
TF2
Differential-drive control
What Rovo Can Do
Spawn the robot in Gazebo
Publish sensor and transform data
Use LiDAR and SLAM to build a map
Localize the robot on a saved map
Use Nav2 to plan navigation paths
Send navigation goals and observe the robot's behavior
 
 
 ✨ Features

🦾 Custom differential-drive AMR model

📐 Modular URDF/Xacro robot description

🛞 Simulated wheel drive

📡 Simulated LiDAR

🌍 Custom Gazebo warehouse environment

🗺️ SLAM-based mapping

📍 AMCL-based localization

🧭 Nav2 navigation

👁️ RViz2 visualization

🔄 TF2 coordinate-frame management

⚙️ Configurable Nav2 parameters

🧩 Modular ROS 2 package structure

🏗️ How the System Works

One of the main things I learned while building Rovo was that the different parts of a ROS 2 robot are closely connected.

The robot model, sensors, odometry, TF, SLAM, localization, and navigation all need to work together for the robot to navigate properly.

Main Components
Gazebo

Simulates the robot, sensors, physics, and warehouse environment.

URDF / Xacro

Defines the robot's physical structure, links, joints, wheels, and sensors.

LiDAR

Provides information about the surrounding environment.

Odometry

Provides information about the robot's movement.

TF2

Maintains the relationships between the robot's coordinate frames.

SLAM Toolbox

Uses LiDAR and odometry data to build a map.

AMCL

Estimates the robot's position on a previously saved map.

Nav2

Handles path planning, control, and autonomous navigation.

RViz2

Provides visualization and debugging of the robot, sensors, TF, maps, costmaps, and navigation paths.

🛠️ Tech Stack
Technology	Purpose

ROS 2 Humble	Robot middleware

Gazebo Classic	Physics-based simulation

RViz2	Visualization and debugging

URDF / Xacro	

Robot modeling

TF2	Coordinate-frame transformations

SLAM Toolbox	Mapping

AMCL	Localization on a known map

Nav2	Autonomous navigation

Python	ROS 2 launch files and configuration

CMake / ament_cmake	ROS 2 package build system

Linux / Ubuntu	Development environment


🚀 Getting Started
Prerequisites

Make sure the following are installed:

Ubuntu 22.04
ROS 2 Humble
Gazebo Classic
Python 3
colcon

Source ROS 2 before building the workspace:

source /opt/ros/humble/setup.bash
1. Clone the Repository
git clone https://github.com/ShreyaDubey-09/rovo-autonomous-mobile-robot.git
cd rovo-autonomous-mobile-robot
2. Install Dependencies

Update the package lists:

sudo apt update

Install the required ROS 2 packages:

sudo apt install \
    ros-humble-xacro \
    ros-humble-robot-state-publisher \
    ros-humble-joint-state-publisher-gui \
    ros-humble-rviz2 \
    ros-humble-gazebo-ros-pkgs \
    ros-humble-slam-toolbox \
    ros-humble-navigation2 \
    ros-humble-nav2-bringup
3. Build the Workspace

Build the ROS 2 workspace:

colcon build

Then source the workspace:

source install/setup.bash
🌍 Running the Simulation

Launch the Gazebo simulation:

ros2 launch rovo_gazebo gazebo.launch.py

This starts the Rovo robot inside the configured Gazebo environment.

👁️ Viewing the Robot in RViz2

Launch the robot visualization:

ros2 launch rovo_description display.launch.py

RViz2 can be used to visualize:

Robot model
LiDAR data
TF frames
Odometry
Maps
Navigation costmaps
Planned paths
🗺️ Mapping with SLAM

Launch SLAM:

ros2 launch rovo_bringup mapping.launch.py

The robot can then be moved around while SLAM Toolbox builds a map using LiDAR and odometry data.

Useful Commands

Check available topics:

ros2 topic list

Inspect LiDAR data:

ros2 topic echo /scan

Inspect the generated map:

ros2 topic echo /map
Save the Map
ros2 run nav2_map_server map_saver_cli -f ~/rovo_map
📍 Localization

After creating a map, Rovo uses AMCL to estimate its position on the saved map.

Localization Depends On
Saved map
LiDAR data
Odometry
Correct TF relationships
Initial pose estimate

In RViz2, use 2D Pose Estimate to provide the robot's initial position.

🧭 Autonomous Navigation

Launch the Nav2 navigation stack:

ros2 launch rovo_bringup navigation.launch.py
From RViz2
Set the initial pose.
Set a navigation goal.
Monitor the costmaps.
Observe the planned path.
Monitor the robot's response.
Main Nav2 Configuration
src/rovo_bringup/config/nav2_params.yaml
🔧 Useful Debugging Commands

A major part of developing Rovo was learning how to debug ROS 2 systematically instead of repeatedly restarting the simulation.

Check Active Nodes
ros2 node list
Check Available Topics
ros2 topic list
Inspect a Topic
ros2 topic echo /scan
Check Topic Publishing Rate
ros2 topic hz /scan
Inspect the TF Tree
ros2 run tf2_tools view_frames
Check a Specific Transform
ros2 run tf2_ros tf2_echo map odom
Visualize Node Connections
rqt_graph
Monitor System Resources
top

🧩 Debugging Journey & Things I Learned

This was one of the most valuable parts of building Rovo.

The project didn't work perfectly on the first try. A significant amount of time went into identifying why something wasn't working instead of simply writing more code.

1. Robot Partially Below Ground

The robot initially had a problem where parts of the chassis and wheels were positioned incorrectly relative to the ground.

I had to check:

URDF/Xacro origins
Wheel radius
Chassis dimensions
Relative link positions
Gazebo spawn position

This taught me how small geometry and transform errors can affect the entire simulation.

2. RViz2 Showing "No Map Received"

At one point, /map was being published, but RViz2 still wasn't displaying the map correctly.

The problem was related to the TF relationship between map and odom.

This taught me that publishing a topic isn't always enough — the coordinate frames also need to be connected correctly.

3. Understanding TF

TF was mostly theoretical to me before this project.

While debugging SLAM, AMCL, and Nav2, I realized how important coordinate-frame relationships are for a mobile robot.

The important frames I worked with included:

map
odom
base_link

Understanding these relationships became essential for getting localization and navigation working.

4. AMCL Needed an Initial Pose

AMCL couldn't properly publish the robot pose until an initial estimate was provided.

Using 2D Pose Estimate in RViz2 solved this.

This helped me understand that localization isn't just about running AMCL — it also depends on correct sensor data, TF, odometry, and an initial estimate.

5. LiDAR Range Warnings

I encountered warnings where the configured LiDAR limits didn't match the simulated sensor's actual range.

I had to compare the sensor configuration with the actual Gazebo LiDAR parameters.

This taught me that sensor configuration matters just as much as the rest of the navigation stack.

6. Nav2 Didn't Always Like Every Goal

Some navigation goals worked while more complex or curved paths produced planner/controller warnings.

I investigated:

Planner logs
Controller behavior
Costmaps
Goal tolerance
TF
Odometry
Simulation timing

This showed me that Nav2 is a pipeline where localization, TF, costmaps, planning, control, and robot motion all depend on each other.

7. Gazebo and RViz2 Performance

Running Gazebo, RViz2, SLAM, and Nav2 together can be demanding.

I used system monitoring tools such as top to understand what was happening.

This taught me that not every problem is a logic problem — sometimes the system itself is struggling.

8. Cleaning and Organizing the Workspace

As the project grew, there were old files, generated outputs, temporary debugging files, and obsolete packages.

I eventually organized the project into three main ROS 2 packages:

rovo_bringup
rovo_description
rovo_gazebo

I also added generated directories such as build/, install/, and log/ to .gitignore.

This taught me that good project structure matters just as much as getting the code to work.

📊 Current Project Status

Component	Status

ROS 2 workspace	✅ Complete

Robot URDF/Xacro	✅ Complete


Differential-drive simulation	✅ Complete

Gazebo environment	✅ Complete

LiDAR simulation	✅ Complete

RViz2 visualization	✅ Complete

SLAM mapping	✅ Complete

Map generation	✅ Complete

AMCL localization	✅ Complete

Nav2 integration	✅ Complete

Autonomous navigation	🟡 Under development

Current Work

Navigation robustness

Path behavior

Simulation performance

🔮 Future Improvements

Improve navigation around curved paths
Tune Nav2 planner/controller parameters
Improve costmap configuration
Optimize Gazebo simulation performance
Improve obstacle avoidance
Add waypoint-based navigation
Test dynamic obstacles
Improve RViz2 visualization
Make the navigation stack more robust across different environments
🎯 What This Project Taught Me

The most valuable part of Rovo wasn't just getting a robot to navigate.

It was understanding how the different pieces of a robotics system fit together.

Through this project, I gained hands-on experience with:

ROS 2 node and topic communication
Robot modeling with URDF/Xacro
Gazebo simulation
LiDAR integration
SLAM and map generation
AMCL localization
TF2
Nav2 navigation
RViz2 visualization
ROS 2 debugging and troubleshooting

The biggest lesson was learning how to debug a robotics system systematically.

Instead of repeatedly restarting the simulation, I learned to:

Check the nodes
Check the topics
Check the TF tree
Check the logs
Isolate the problem
Fix the issue
Test again

That debugging process has probably been one of the most useful things I've learned from this project.

👩‍💻 Author

Shreya Dubey

Electronics & Telecommunication Engineering
Robotics & Autonomous Systems Enthusiast

GitHub: ShreyaDubey-09

📄 License

This project is licensed under the MIT License.

See LICENSE for details.
