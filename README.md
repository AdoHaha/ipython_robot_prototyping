## ROS Package for IPython Robot Prototyping workshop at PyCon PL 2017

The package consists msg and srv files and simulator programs for the workshop


### How to install:

First you need to have your ROS basic setup, use 
this tutorial: [http://wiki.ros.org/ROS/Tutorials/InstallingandConfiguringROSEnvironment](http://wiki.ros.org/ROS/Tutorials/InstallingandConfiguringROSEnvironment)

especially you need to have catkin workspace set up. Next commands assume that it is in a standard place (~/catkin_ws)


clone this package to catkin_ws/src

  ```
  cd ~/catkin_ws/src/ & git clone https://github.com/AdoHaha/ipython_robot_prototyping
  ```

run catkin_make in the main catkin_ws directory


  ```
  cd ~/catkin_ws & catkin_make
  ```
  
source the changes


  ```
  source ~/catkin_ws/devel/setup.bash
  ```
  
  After that, start the Ipython notebook in ipython_robot_prototyping directory (~/catkin_ws/src/ipython_robot_prototyping)
  
  
  ```
    cd ~/catkin_ws/src/ipython_robot_prototyping & ipython3 notebook
  ```
