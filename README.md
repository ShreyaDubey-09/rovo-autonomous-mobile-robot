🤖 Rovo — Autonomous Mobile Robot

Rovo is a ROS 2-based Autonomous Mobile Robot (AMR) simulation that I built to learn and work with different parts of a robotics software stack — from robot modeling and Gazebo simulation to LiDAR, SLAM, localization, TF, RViz, and Nav2 navigation.

The main goal of this project wasn't just to make a robot move. I wanted to understand what is actually happening behind the scenes and learn how to debug the system when things inevitably went wrong.

And there were quite a few things that went wrong. 😅

This project became a hands-on way for me to learn how the different parts of a ROS 2 navigation stack connect together.

📌 Project Overview

Rovo is a differential-drive mobile robot simulated in a warehouse-style environment.

The project uses:

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

With these components working together, Rovo can:

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
🏗️ How the System Fits Together

One of the main things I learned while building Rovo was that the different parts of a ROS 2 robot are closely connected.

The robot model, sensors, odometry, TF, SLAM, localization, and navigation all need to work together for the robot to navigate properly.

At a high level:

Gazebo simulates the robot and its environment.
URDF/Xacro defines the robot's structure and sensors.
LiDAR provides information about the surroundings.
Odometry provides information about the robot's movement.
TF2 keeps track of the relationships between coordinate frames.
SLAM Toolbox uses sensor and odometry data to build a map.
AMCL estimates the robot's position on a saved map.
Nav2 uses the map and robot position to plan and execute navigation goals.
RViz2 helps visualize and debug what is happening.

Simple frame relationship:

map
 │
 ▼
odom
 │
 ▼
base_link

Understanding how these frames and components interact became a major part of debugging Rovo, especially when working with SLAM, AMCL, and Nav2.

🛠️ Tech Stack
Technology	Purpose
ROS 2 Humble	Robot middleware
Gazebo Classic	Physics-based simulation
RViz2	Visualization and debugging
URDF / Xacro	Robot modeling
TF2	Coordinate-frame transformations
SLAM Toolbox	Mapping
AMCL	Localization on a known map
Nav2	Autonomous navigation
Python	ROS 2 launch files and configuration
CMake / ament_cmake	ROS 2 package build system
Linux / Ubuntu	Development environment
🚀 Getting Started
Prerequisites
Ubuntu 22.04
ROS 2 Humble
Gazebo Classic
Python 3
colcon

Make sure ROS 2 Humble is installed and sourced before building the workspace.

1. Clone the Repository
git clone https://github.com/ShreyaDubey-09/rovo-autonomous-mobile-robot.git
cd rovo-autonomous-mobile-robot

Source ROS 2:

source /opt/ros/humble/setup.bash
2. Install Dependencies
sudo apt update

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
colcon build

Then source the workspace:

source install/setup.bash
🌍 Running the Simulation
ros2 launch rovo_gazebo gazebo.launch.py

This starts the Rovo robot inside the configured Gazebo environment.

👁️ Viewing the Robot in RViz
ros2 launch rovo_description display.launch.py

RViz is useful for visualizing:

Robot model
LiDAR data
TF frames
Odometry
Maps
Navigation costmaps
Planned paths
🗺️ Mapping with SLAM
ros2 launch rovo_bringup mapping.launch.py

The robot can then be moved around while SLAM Toolbox builds a map using LiDAR.

Useful commands:

ros2 topic list
ros2 topic echo /scan
ros2 topic echo /map

Save the map:

ros2 run nav2_map_server map_saver_cli -f ~/rovo_map
📍 Localization

After creating a map, Rovo uses AMCL to estimate its position.

Localization depends on:

Saved map
LiDAR data
Odometry
Correct TF tree
Initial pose estimate

In RViz, use 2D Pose Estimate to provide the robot's initial position.

🧭 Autonomous Navigation
ros2 launch rovo_bringup navigation.launch.py

From RViz:

Set the initial pose
Set a navigation goal
Monitor costmaps
Observe the planned path
Watch the robot's response

Main Nav2 configuration:

src/rovo_bringup/config/nav2_params.yaml
🔧 Useful Debugging Commands

A big part of developing Rovo was learning how to debug ROS 2 instead of just restarting everything and hoping it works. 😅

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

This is probably the part that taught me the most.

Rovo didn't work perfectly on the first try. A lot of time went into figuring out why something wasn't working instead of simply writing more code.

1. Robot Partially Below Ground

The robot initially had a problem where parts of the chassis and wheels were positioned incorrectly relative to the ground.

I had to check:

URDF/Xacro origins
Wheel radius
Chassis dimensions
Relative link positions
Gazebo spawn position

This taught me how small geometry and transform errors can affect the entire simulation.

2. RViz Showing "No Map Received"

At one point, /map was being published, but RViz still wasn't displaying the map correctly.

The problem was related to the TF relationship between map and odom.

This taught me that publishing a topic isn't always enough — the coordinate frames also need to be connected correctly.

3. Understanding map → odom → base_link

TF was mostly theory to me before this project.

While debugging SLAM, AMCL and Nav2, I realized how important the TF tree actually is.

map
 │
 ▼
odom
 │
 ▼
base_link

Understanding these relationships became essential for getting localization and navigation working.

4. AMCL Needed an Initial Pose

AMCL couldn't properly publish the robot pose until an initial estimate was provided.

Using 2D Pose Estimate in RViz solved this.

This helped me understand that localization isn't just about running AMCL — it also depends on correct sensor data, TF, odometry and an initial estimate.

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

This showed me that Nav2 is really a pipeline where localization, TF, costmaps, planning, control and robot motion all depend on each other.

7. Gazebo and RViz Performance

Running Gazebo, RViz, SLAM and Nav2 together can be demanding, especially on limited hardware.

I used system monitoring tools such as top to understand what was happening.

This taught me that not every problem is a logic problem — sometimes the system itself is struggling.

8. Cleaning and Organizing the Workspace

As the project grew, there were old files, generated outputs, temporary debugging files and obsolete packages.

I eventually organized the project into:

rovo_bringup
rovo_description
rovo_gazebo

and added generated directories such as build/, install/ and log/ to .gitignore.

This taught me that good project structure matters just as much as getting the code to work.

📊 Current Project Status
Component	Status
ROS 2 workspace	✅
Robot URDF/Xacro	✅
Differential-drive simulation	✅
Gazebo environment	✅
LiDAR simulation	✅
RViz visualization	✅
SLAM mapping	✅
Map generation	✅
AMCL localization	✅
Nav2 integration	✅
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
Improve RViz visualization
Make the navigation stack more robust across different environments
🎯 What This Project Taught Me

The most valuable part of Rovo wasn't just getting a robot to navigate.

It was understanding how the different pieces of a robotics system fit together.

A simplified view of the workflow:

Robot Modeling
      ↓
Gazebo Simulation
      ↓
Sensor Integration
      ↓
TF / Odometry
      ↓
SLAM
      ↓
Localization
      ↓
Nav2
      ↓
Navigation

And probably the most important workflow I learned was debugging:

Check the nodes
      ↓
Check the topics
      ↓
Check the TF
      ↓
Check the logs
      ↓
Isolate the problem
      ↓
Fix it
      ↓
Test again

That debugging process has probably been one of the most useful things I've learned from this project.

👩‍💻 Author

Shreya Dubey

Electronics & Telecommunication Engineering
Robotics & Autonomous Systems Enthusiast

GitHub:
https://github.com/ShreyaDubey-09

📄 License

This project is licensed under the MIT License.

See LICENSE for details.