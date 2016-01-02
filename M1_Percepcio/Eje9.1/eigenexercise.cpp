//# PERCEPTION SYSTEMS EXERCISE 9.1: EIGEN in C++	  |
//#-------------------------------------------------------|
//# TONI GUASCH SERRA		January 2016 	          |
//#-------------------------------------------------------|


//#------------------------------Exercise 1)---------------------------------------------------
#include <iostream>
#include <eigen3/Eigen/Dense> //Main Eigen Library
#include <math.h>

#define pi 3.141592654
 
using namespace std;
using namespace Eigen;

int main()
{

cout << "\n(|-------------------------------|)";
cout << "\n(|Exercise 9.1 Perception Syst.  |)";
cout << "\n(|-------------------------------|)";
cout << "\n(|     TONI GUASCH SERRA         |)";
cout << "\n(|-------------------------------|)";



//Given data by exercise. Robot moving values.
  	//Robot position. x,y coordinates
	Vector2d p0(10.8, -2.7);
	//Sensor position. x,y coordinates
	Vector2d mb(3.1, 1.2);
	//Sensor 
	Vector2d qs(12, 3);
	//Robot position. Orientation angle
	float Theta = 28 * (pi/180);
	//Sensor position. Orientation angle
	float Beta = 41 * (pi/180);

//¿Coordinates of the point of interest with respect to the base frame?
//¿Coordinates of the point of interest with respect to the origin of the trajectory?

//Rotation Matrixes involved:
	Matrix2d R0B;
   	Matrix2d RBS;	
	R0B << cos(Theta), -sin(Theta), sin(Theta), cos(Theta);
    	RBS << cos(Beta), -sin(Beta), sin(Beta), cos(Beta);
//Homogeneous Matrixes from the origin tot the base, and from the base to the sensor:
    	Matrix3d T0B;
    	Matrix3d TBS;	
	T0B << cos(Theta), -sin(Theta), p0[0], sin(Theta), cos(Theta), p0[1], 0 , 0 , 1;
    	TBS << cos(Beta), -sin(Beta), mb[0], sin(Beta), cos(Beta), mb[1], 0 , 0 , 1;

//Print Matrixes
	cout << "\nHomogeneous matrix base to origin:" << endl << T0B << std::endl;
	cout << "\nHomogeneous matrix sensor to base:" << endl << TBS << std::endl;


//CALCULATE 
	//Define aux vector with qs value and a 3rd row with "1"value
	Vector3d qs_aux(qs[0], qs[1], 1);
	//Respect ORIGIN of trajectory =T0B*TBS*qs_aux
	cout << "\nVector q in origin in homogeneous:" << endl << T0B * TBS * qs_aux << endl;
	//Respect base frame=TBS*qs_aux
	cout << "\nVector q in base in homogeneous:\n" << endl << TBS * qs_aux << endl;

}

