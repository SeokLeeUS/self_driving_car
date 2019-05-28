# Self Driving Car capstone
Udacity self driving nano degree #8

## References:
All figures appeared on this readme.md are from Udacity's self driving car nano degree material unless otherwise specified. 
ROS official website: [ros.org](https://www.ros.org/)

## Project overview:

![project_overview](/selfdriving_final_figure/project_overview.png)

## How a robot works: 
perception: how robot sees the world
decision making: command to determine what the next step would be
actuation: make a move 

![ROS_overview](/selfdriving_final_figure/ros.png)

## Node,topics,messages:
ROS (Robot Operating System) governs the interaction (communication) of each nodes. 

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
