cmake_minimum_required(VERSION 2.6)
project(eigenexercise)

SET(CMAKE_BUILD_TYPE "RELEASE") 
ADD_EXECUTABLE(${PROJECT_NAME} src/eigenexercise.cpp)

#include_directories($ENV{EIGEN3_INCLUDE_DIR})
#ADD_EXECUTABLE(eigenLib eigenLib.cpp)
#ADD_EXECUTABLE(eigenState eigenState.cpp)

