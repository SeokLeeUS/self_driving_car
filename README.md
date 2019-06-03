Simulation environment:

-- Python version:
```python
python --version
2.7.12
```
-- Keras version 
```python
python -c "import keras; print(keras.__version__)
2.0.8
```

## Procedure 
- At first, make sure the vehicle follows the path without classification 
- image classification model build up 
  - image collection
  - train/test/verify
  - predict
- external Bosch data set works well with a learning model (taken from behavioral cloning's CNN architecture), but it doesn't predict well with simulation images. 
- shift the gear to collect the traffic signal images from simulation envrironment 
  - need to establish the image saving algorithrm from a topic 
  - need to establish the signal color information form a messaage in order to annotate the image
  - create a seperate code to save the combination image/annotation in csv format
  - when training the model, need to find out if I need to crop out the image. Also, I need to consider to set the input/output size as is. (bosch dataset forces to set the image size as 32x32x3).
  - Also, make sure I may need to have image pre-processing before training/validate/predict(I need to check).  
- data preprocessing- why there's no data preprocessing for bosch dataset?
- I also need to check the classification output is transmitted correctly to the tl_detector.py logic when the tl_classifier function is called. 

Training model files: 
- traffic_identifer_training_00.py
Predict model to check the training model works fine:
- predict_tl.py

Number of training/validation data is 10698. The location of data is xxx

Image reprocessing code (classifier_dataprep_01.ipynb):
```python
# jupyter notebook command 
import sys
sys.executable
import numpy as np

from platform import python_version
print(python_version())

import numpy
numpy.version.version
%run -i save_tl_images.py data/train.yaml data/tl-extract-train
```
tl_images.py is take from [this link](https://github.com/asimonov/Bosch-TL-Dataset)

However, the classification with traffic light in simulation doesn't work well. 

The options which I am considering is, 

a. Take the image from the simulation. The code is, 
```python 
# saving traffic light image from simulation:
        path = os.getcwd()
        directory = os.path.dirname(path)
        image_folder = directory +'/tl_detector/sim_data'
        timestamp = datetime.utcnow().strftime('%Y_%m_%d_%H_%M_%S_%f')[:-3]
        image_filename = os.path.join(image_folder, timestamp)
        print(image_filename)
        cv2.imwrite('{}.jpg'.format(image_filename),image)
```
b. Image classification annotation, there's message from a topic which does tell about the signal color, hence, save along with the annotation. 
```python
from styx_msgs.msg import TrafficLightArray, TrafficLight
t=TrafficLight()
print(t.state)
```
c. Add postfix @ the file name to annotate the signal color:
```python
image_filename = os.path.join(image_folder,timerstamp,'_',t.state)
```
d. drive manually to collect image 

e. generate csv files (1st column: file name, 2nd column, signal color annotation)
```python

```
f. I might need cropping the image to only looking at traffic light from the simulation. 
```python

```
g. Sample an image every other 3 images obtained from the simulation to mitigate the latency issue on the simulation: 
```python

```



yellow	1
red	2
green	3
rest	4


uint8 state

uint8 UNKNOWN=4
uint8 GREEN=2
uint8 YELLOW=1
uint8 RED=0


# Self Driving Car capstone
  - Udacity self driving nano degree #9 (final...)

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

- The scope of project is to write ROS nodes to implement and integrate the various features (packages) of Carla's autonomous driving system. The packages (**c++ package name**) include, 

  1. traffic light detection (**tl_detector**): transmits the location to stop for red light
  2. way point updater (**waypoint_updater**): update target velocity of each way points based on traffic light and obstacle detection data
  3. vehicle controller (**twist_controller**): controls the steering,throttle,and brakes

![project_overview](/selfdriving_final_figure/project_overview.png)

## self driving car nodes:

1.**tl_detector** (traffic light detection)
  - incoming topics:  
    a. /base_waypoints: the complete list of way points which the vehicle will follow      
    b. /image_color: color of traffic light(?)    
    c. /current_pose: the vehicle's current location   

  - outgoing topic:    

    a.  /traffic_waypoint: the locations to stop for red traffic light (index of the waypoint for the nearest upcoming red light's stop line)     
  - things to work on:    

    a. tl_detector.py: traffic light detection       

    b. tl_classfier.py: classfies traffic light      

![tl_detector](/selfdriving_final_figure/tl-detector-ros-graph.png)

2.**waypoint_updater** (update target velocity based on traffic light/obstacle data)

 - incoming topics:  

    a.  /base_waypoints: the complete list of way points which the vehicle will follow. only published once (it makes sense as it won't change all lists throughout driving on the target path) 

    b.  /obstacle_waypoint: ?    

    c.  /traffic_waypoint: topic from tl_detector node    

    d.  /current_pose: the vehicle's current location     

 - outgoing topic:    

    a.  /final_waypoints: the list of waypoints (a fixed number of waypo ahead of the car with target velocities  

![tl_detector](/selfdriving_final_figure/waypoint-updater-ros-graph.png)

3.**twist_controller** (responsible for control the vehicle)    

 - incoming topics:      

   a.  /current_velocity      

   b.  /twist_cmd      

   c.  /vehicle/dbw_enabled      

 - outgoing topics:      

    a.  /vehicle/throttle_cmd    

    b.  /vehicle/steering_cmd    

    c.  /vehicle/brake_cmd    

![twist_controller](/selfdriving_final_figure/dbw-node-ros-graph.png)

4. **classifier**
- Frame work:
  a. step 1 (classification):
     - obtain annotated dataset [Bosch dataset] (https://hci.iwr.uni-heidelberg.de/benchmarks)
     - train the model and predict the traffic signal for testing the data by looking at existing example code:
     [asimonov's CNN for traffic signal identification](https://github.com/asimonov/Bosch-TL-Dataset)
     - create a csv file for data location with annotated traffic signal color
     - look for behavioral cloning code for benchmark [Behavioral_Cloning](https://github.com/SeokLeeUS/behavioral_cloning)
     - then train and predict 
     
  b. step 2 (integration to tl_classifier node):
     - initialization (adding necessary initialization attribute and calling methods from other nodes) 
     - embed classification and transmit the signal color as an output. 
     
     
