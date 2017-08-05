## ROS Package for IPython Robot Prototyping workshop at PyCon PL 2017

The package consists msg and srv files and simulator programs for the workshop


### Ordered excercise 


    1. setting_up_and_running_your_first_ROS_Node.ipynb
    2. ROS_concepts_explained_Topic_Service_Parameter.ipynb
    3. Using_IPython_Interactive_Widgets.ipynb
    4. Visualizing_robot_senses.ipynb


### How to install:

_ you will be provided with a virtual machine for the workshop so you don't need to do the fallowing commands before the workshop.

The commands are for those who want to run the ROS from their native environment (for example an [Ubuntu 16.04 computer](http://wiki.ros.org/kinetic/Installation/Ubuntu)) 
 _

First you need to have your ROS basic setup, use 
this tutorial: [http://wiki.ros.org/ROS/Tutorials/InstallingandConfiguringROSEnvironment](http://wiki.ros.org/ROS/Tutorials/InstallingandConfiguringROSEnvironment)

especially you need to have catkin workspace set up. Next commands assume that it is in a standard place (~/catkin_ws)


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
  
  After that, start the IPython notebook in ipython_robot_prototyping directory (~/catkin_ws/src/ipython_robot_prototyping)
  
  
  ```
    cd ~/catkin_ws/src/ipython_robot_prototyping && ipython3 notebook
  ```
  
  IPython notebook should open in your browser. Go to excercises directory and open setting_up_and_running_your_first_ROS_Node.ipynb
  
