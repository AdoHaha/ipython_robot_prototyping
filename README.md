## ROS Package for IPython Robot Prototyping workshop at PyCon PL 2017

The package consists msg and srv files and simulator programs for the workshop


### The order of exercises 

Excercices are at ipython_robot_prototyping/scripts/excercises

 0. Getting_Started_with_virtual_environment.ipynb -- an installation of virtual machine
 1. Setting_up_and_running_your_first_ROS_Node.ipynb
 2. ROS_concepts_explained_Topic_Service_Parameter.ipynb
 3. Using_IPython_Interactive_Widgets.ipynb
 4. Visualizing_robot_senses.ipynb
 5. Controlling_and_visualizing_the_ESP_bot.ipynb
 6. Tour_of_ROS_tools_with_experiments.ipynb


### How to install:

We have prepared a virtual machine for the workshop,
so you don't need to manually install ROS beforehand.

** However, please install and prepare VirtualBox
 using the instructions from
[Getting Started with virtual environment](https://github.com/AdoHaha/ipython_robot_prototyping/blob/master/scripts/excercises/Getting_Started_with_virtual_environment.ipynb) **.

#### Manual install 

The commands are for those who want to run the ROS from their native environment (for example an [Ubuntu 16.04 computer](http://wiki.ros.org/kinetic/Installation/Ubuntu)) **

First, you need to have your ROS basic setup, use 
this tutorial: [http://wiki.ros.org/ROS/Tutorials/InstallingandConfiguringROSEnvironment](http://wiki.ros.org/ROS/Tutorials/InstallingandConfiguringROSEnvironment)




We will be working using python3 so install also:

```
sudo apt-get install python3-rospy python3-rospkg python3-rosdep

```

To run the "robot simulators" offline install also 


```
sudo apt-get install mpg123
```




You need to have catkin workspace set up. Next commands assume that it is in a standard place (~/catkin_ws)


clone this package to catkin_ws/src

  ```
  cd ~/catkin_ws/src/ & git clone https://github.com/AdoHaha/ipython_robot_prototyping
  ```

run catkin_make in the main catkin_ws directory


  ```
  cd ~/catkin_ws && catkin_make
  ```
  
source the changes


  ```
  source ~/catkin_ws/devel/setup.bash
  ```
 
 We will be using some additional python(3) libraries, you can install them by pip
 
 ```
 pip3 install -r requirements.txt
 ```
 
  
  After that, start the IPython notebook in ipython_robot_prototyping directory (~/catkin_ws/src/ipython_robot_prototyping)
  
  
  ```
    cd ~/catkin_ws/src/ipython_robot_prototyping && ipython3 notebook
  ```
  
  Jupyter notebook should open in your browser. Go to exercises directory and open setting_up_and_running_your_first_ROS_Node.ipynb
  
### Running locally

We have prepared "robot simulators" to use this tutorial without the access of
real robots. To do so you need to run:

```

roslaunch ipython_robot_prototyping simulators.launch 

```

also in your Jupyter notebooks change the ROS MASTER URI to http://localhost:11311

```
%env ROS_MASTER_URI=http://localhost:11311
```
