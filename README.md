🤖 Rovo — Autonomous Mobile Robot

Rovo is a ROS 2-based Autonomous Mobile Robot (AMR) simulation that I built to learn and work with the different parts of a robotics software stack — from robot modeling and Gazebo simulation to LiDAR, SLAM, localization, TF, RViz, and Nav2 navigation.

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

At a high level, Rovo works like this:

Gazebo simulates the robot and its environment.
URDF/Xacro defines the robot's structure and sensors.
LiDAR provides information about the surroundings.
Odometry provides information about the robot's movement.
TF2 keeps track of the relationships between coordinate frames.
SLAM Toolbox uses sensor and odometry data to build a map.
AMCL estimates the robot's position on a saved map.
Nav2 uses the map and robot position to plan and execute navigation goals.
RViz2 helps visualize and debug what is happening.

A simplified view of the main coordinate frames is:

map
 └── odom
      └── base_link

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
📁 Repository Structure
rovo-autonomous-mobile-robot/
│
├── src/
│   │
│   ├── rovo_bringup/
│   │   ├── config/
│   │   │   └── nav2_params.yaml
│   │   ├── launch/
│   │   │   ├── demo.launch.py
│   │   │   ├── mapping.launch.py
│   │   │   ├── navigation.launch.py
│   │   │   └── simulation.launch.py
│   │   ├── maps/
│   │   │   ├── amr_map.pgm
│   │   │   └── amr_map.yaml
│   │   └── rviz/
│   │       └── rovo_nav.rviz
│   │
│   ├── rovo_description/
│   │   ├── launch/
│   │   │   └── display.launch.py
│   │   └── urdf/
│   │       ├── base.xacro
│   │       ├── gazebo.xacro
│   │       ├── materials.xacro
│   │       ├── robot.urdf.xacro
│   │       ├── sensors.xacro
│   │       └── wheels.xacro
│   │
│   └── rovo_gazebo/
│       ├── config/
│       │   └── mapper_params_online_async.yaml
│       ├── launch/
│       │   └── gazebo.launch.py
│       └── worlds/
│           ├── amr_world.world
│           └── warehouse.world
│
├── .gitignore
├── LICENSE
└── README.md
🚀 Getting Started
Prerequisites

The project currently targets:

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

Install the main ROS 2 dependencies:

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

From the repository root:

colcon build

Then source the workspace:

source install/setup.bash
🌍 Running the Simulation

Launch the Gazebo simulation:

ros2 launch rovo_gazebo gazebo.launch.py

This starts the Rovo robot inside the configured Gazebo environment.

👁️ Viewing the Robot in RViz

To visualize the robot model:

ros2 launch rovo_description display.launch.py

RViz is useful for inspecting:

Robot model
LiDAR data
TF frames
Odometry
Maps
Navigation costmaps
Planned paths
🗺️ Mapping with SLAM

Start the simulation and then launch the mapping system:

ros2 launch rovo_bringup mapping.launch.py

The robot can then be moved around the environment while SLAM Toolbox builds a map using LiDAR data.

Some useful commands while mapping:

ros2 topic list

Check LiDAR data:

ros2 topic echo /scan

Check the generated map:

ros2 topic echo /map

Once the map is ready, it can be saved using:

ros2 run nav2_map_server map_saver_cli -f ~/rovo_map
📍 Localization

After creating a map, Rovo uses AMCL (Adaptive Monte Carlo Localization) to estimate its position on that map.

Localization depends on several things working together:

Saved map
LiDAR data
Odometry
Correct TF tree
Initial pose estimate

In RViz, the robot's starting position can be provided using 2D Pose Estimate.

🧭 Autonomous Navigation

With a saved map available, launch Nav2:

ros2 launch rovo_bringup navigation.launch.py

From RViz, you can then:

Set the robot's initial pose
Set a navigation goal
Monitor the costmaps
Observe the planned path
Watch how the robot responds to the goal

The main Nav2 configuration is located at:

src/rovo_bringup/config/nav2_params.yaml
🔧 Useful Debugging Commands

A big part of developing Rovo was learning how to debug ROS 2 instead of just restarting everything and hoping it works.

These are some of the commands that helped the most.

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

This is probably the part of the project that taught me the most.

Rovo definitely didn't work perfectly on the first try. A lot of time went into figuring out why something wasn't working rather than simply writing more code.

Here are some of the problems I ran into.

1. Robot Was Partially Below the Ground

At one point, the robot spawned with a large part of the chassis and wheels below the Gazebo ground plane.

The problem turned out to be related to the positioning of the robot's links.

I went through:

URDF/Xacro link origins
Wheel radius
Chassis dimensions
Relative positions of the components
Gazebo spawn position

Eventually, the vertical placement of the robot components was corrected.

What I learned

Even a small mistake in URDF geometry or link transforms can make the simulated robot behave completely differently from what you expect.

2. RViz Said "No Map Received"

This was one of those problems where the data technically existed, but RViz still wasn't showing what I expected.

The /map topic was publishing correctly, so I checked the TF relationships.

The issue was that the required relationship between the map and odometry frames wasn't available to RViz.

After fixing the TF connection, the map appeared correctly.

What I learned

In ROS, publishing data is only part of the problem. The system also needs the correct coordinate-frame relationships for different nodes to understand where that data belongs.

3. Understanding map → odom → base_link

Before working on this project, TF was one of the concepts I understood mostly in theory.

While debugging Rovo, I had to actually understand how:

map
 ↓
odom
 ↓
base_link

fits together.

This became especially important when working with SLAM, AMCL, and Nav2.

What I learned

A solid understanding of TF2 is essential when working with ROS 2 navigation.

4. AMCL Needed an Initial Pose

AMCL initially reported that it couldn't publish the robot pose or update the transform.

The localization system had not been given a proper initial estimate of where the robot was on the map.

Using 2D Pose Estimate in RViz allowed the robot's initial pose to be provided.

What I learned

Starting a localization node doesn't automatically mean the robot knows where it is.

The localization system needs the right inputs, TF, and an initial estimate.

5. LiDAR Range Warnings

I also ran into warnings where the configured LiDAR minimum and maximum ranges didn't match the capabilities of the simulated sensor.

I had to compare:

Configured LiDAR range
        vs.
Actual simulated sensor range

and adjust the configuration accordingly.

What I learned

Sensor parameters matter. Even in simulation, the configuration should make sense for the sensor being modeled.

6. Nav2 Didn't Always Like My Goals

Navigation was probably the most interesting part to debug.

Some goals worked, while certain paths — especially more complicated or curved ones — produced planner or controller warnings.

I spent time looking at:

Planner logs
Controller behavior
Costmaps
Goal tolerance
TF
Robot odometry
Simulation timing
What I learned

Nav2 isn't one single algorithm that simply "moves the robot."

It's a pipeline where localization, TF, costmaps, planning, control, and robot motion all have to work together.

7. Gazebo and RViz Performance

Running Gazebo, RViz, SLAM, and Nav2 together became fairly demanding on the system.

I used Linux tools such as:

top

to monitor CPU usage.

This helped me understand whether a problem was actually caused by the robotics stack or by the simulation becoming computationally heavy.

What I learned

Not every robotics problem is a software-logic problem.

Sometimes the computer running the simulation is simply struggling.

8. Cleaning Up the ROS 2 Workspace

The project originally contained a number of old files, generated outputs, temporary debugging files, and obsolete packages.

As the project evolved, I cleaned the workspace and organized it into three main packages:

rovo_bringup
rovo_description
rovo_gazebo

Generated directories such as:

build/
install/
log/

are ignored using .gitignore.

What I learned

Good project structure matters, especially when working with ROS 2.

Keeping robot descriptions, simulation files, launch files, and configuration organized makes the project much easier to understand and maintain.

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

The main areas I'm currently working on are navigation robustness, path behavior, and simulation performance.

🔮 Future Improvements

Some things I would like to improve next:

Improve navigation around curved paths
Tune Nav2 planner and controller parameters
Improve costmap configuration
Optimize Gazebo simulation performance
Improve obstacle avoidance
Add waypoint-based navigation
Test navigation with dynamic obstacles
Improve the overall RViz visualization
Make the navigation stack more robust across different environments
🎯 What This Project Taught Me

The most valuable part of Rovo wasn't just getting a robot to navigate.

It was understanding how the different pieces of a robotics system fit together:

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

More importantly, I learned how to approach robotics problems systematically:

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