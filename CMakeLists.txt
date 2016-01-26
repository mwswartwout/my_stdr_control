cmake_minimum_required(VERSION 2.8.3)
project(my_stdr_control)

find_package(catkin REQUIRED COMPONENTS rospy roslint)

catkin_python_setup()

catkin_package(
    INCLUDE_DIRS ${catkin_INCLUDE_DIRS}
    CATKIN_DEPENDS rospy
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

roslint_python()
