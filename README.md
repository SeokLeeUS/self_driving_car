# Self Driving Car capstone
- Udacity self driving nano degree #8

## References:
- All figures appeared on this readme.md are from Udacity's self driving car nano degree material unless otherwise specified. 
- ROS official website: [ros.org](https://www.ros.org/)

## How a robot works: 
- Perception: how robot sees the world
- Decision making: command to determine what the next step would be
- Actuation: make a move 

![ROS_overview](/selfdriving_final_figure/ros.png)

## nomenclature (Node,topics,messages,package):
- ROS (Robot Operating System) governs the interaction (communication) of each nodes. 

![ROS_Nodes](/selfdriving_final_figure/nodes.png)

- Topic: 
like CAN (Controlled Area Network) bus to arrange standardized method to communicate information between nodes. 
- Publish: 
A Node sends out information (message) to the recipient. "sending" is called as publish. 
- Subscribe: 
The recipient receives the information (message), "receiving" is called as subscribe. 
![ROS_pub_sub](/selfdriving_final_figure/pub_sub_architecture.png)
- Messages: 
There are quite a bit of predefined messages which represents the prevailing robotic application. For instance, Camera sends out (publish) "image" message. Wheel encoder publishes "rotation" message. 
![ROS_message](/selfdriving_final_figure/ROS_message.png)
- Compute Graph: 
Visualization message transportation through topic between nodes (similar with [stateflow](https://www.mathworks.com/products/stateflow.html), [structured analysis](https://en.wikipedia.org/wiki/Structured_analysis))
![compute_graph](/selfdriving_final_figure/compute_graph.png)
- Package: according to [ROSwiki](http://wiki.ros.org/ROS/Concepts), an element of ROS which can build and release. It may contains node(s), ROS dependent library, dataset, configuration files or anything else that is usefully organized together. 

## Project overview:

- The scope of project is to write ROS nodes to implement and integrate the various features (packages) of Carla's autonomous driving system. The packages (**package name**) include, 

1. traffic light detection (**tl_detector**): transmits the location to stop for red light
2. way point updater (**waypoint_updater**): update target velocity of each way points based on traffic light and obstacle detection data
3. vehicle controller (**twist_controller**): controls the steering,throttle,and brakes

![project_overview](/selfdriving_final_figure/project_overview.png)

## self driving car nodes:

1.**tl_detector** (traffic light detection)
- incoming topics:

a. /base_waypoints: the complete list of way points which the vehicle will follow.  

b. /image_color: color of traffic light(?)  

c.  /current_pose: the vehicle's current location   
- outgoing topic:
a.  /traffic_waypoint: the locations to stop for red traffic light  
- things to work on:
a. tl_detector.py: traffic light detection   
b. tl_classfier.py: classfies traffic light  

![tl_detector](/selfdriving_final_figure/tl-detector-ros-graph.png)

2. **waypoint_updater** (update target velocity based on traffic light/obstacle data)
- incoming topics:
a.  /base_waypoints: the complete list of way points which the vehicle will follow.   
b.  /obstacle_waypoint: ?  
c.  /traffic_waypoint: topic from tl_detector node  
d.  /current_pose: the vehicle's current location   
- outgoing topic:
a.  /final_waypoints: the list of waypoints ahead of the car with target velocities  

![tl_detector](/selfdriving_final_figure/waypoint-updater-ros-graph.png)

3.**twist_controller** (responsible for control the vehicle)
-incoming topics:
a.  /current_velocity  
b.  /twist_cmd  
c.  /vehicle/dbw_enabled  
- outgoing topics:
a.  /vehicle/throttle_cmd  
b.  /vehicle/steering_cmd  
c.  /vehicle/brake_cmd  

![twist_controller](/selfdriving_final_figure/dbw-node-ros-graph.png)
