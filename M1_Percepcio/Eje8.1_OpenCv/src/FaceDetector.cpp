//FACE DETECTION CODE USING OPENCV	|
//TONI GUASCH SERRA			|
//--------------------------------------|
//FOLLOWED DOC:
// http://docs.opencv.org/2.4/doc/tutorials/objdetect/cascade_classifier/cascade_classifier.html
// http://docs.opencv.org/2.4/modules/gpu/doc/object_detection.html
// http://docs.opencv.org/2.4/modules/highgui/doc/reading_and_writing_images_and_video.html#videocapture
//------------------------------------------------------------------------------------------------

//Libraries 
#include "cv.h"
#include <stdio.h>
#include <stdlib.h> 
#include <math.h>
#include "highgui.h"
#include <iostream>
#include <cstdlib>

//Variables and Functions
int Selection;	
using namespace cv;
using namespace std;
void detectAndDisplay(Mat frame);
void function1();
void function2();


//Set source of video:
const string filename = "/home/toni/Documents/GIT/Face_Detection/Face_Detection/src/video.mpeg";
//Set Classifier XML source:
String face_cascade_name = "/home/toni/Documents/GIT/Face_Detection/Face_Detection/src/haarcascade_frontalface_default.xml";
CascadeClassifier face_cascade;


//--------------------------------------------------------------------------------------------------------------//
//MAIN FUNCTION													//
//--------------------------------------------------------------------------------------------------------------//
int main() 
{
do
{

	printf ("\n |--------------FACE DETECTION PROGRAM---------------------|");
	printf ("\n | Program to detect and track the center point of a face  |");
	printf ("\n |---------------------------------------------------------|");
	printf ("\n | Select a source of video:                               |");
	printf ("\n |---------------------------------------------------------|");
	printf ("\n |1. Webcam Video Source                                   |"); 
	printf ("\n |2. .Avi file from your HDD                               |");
	printf ("\n |---------------------------------------------------------|");

	printf ("\n | Please enter your selection:");
	scanf("%d", &Selection);
	if (Selection>=3 || Selection<=0)
		{
			printf (" \n Selection must be 1 or 2, Try again!");
		}

}while((Selection>=3) || (Selection<=0));

if (Selection=2)
{
	printf ("\n function 2");	
	function2();
}else
	printf ("\n function 1");	
	function1();

}



//--------------------------------------------------------------------------------------------------------------//
//Function-2: From Video File 											//
//--------------------------------------------------------------------------------------------------------------//
void function2()
{
	Mat frame;
//Load the cascade
	if( !face_cascade.load(face_cascade_name)){ printf("--(!)Error loading\n"); return; };// -1; };

//Read the video file
	VideoCapture capture(filename);
    if( !capture.isOpened())	throw "Error reading video file";
	while(true) {
		//Get a frame		
		capture >> frame;
	
		//Apply the classifier to the frame
		if( !frame.empty())detectAndDisplay(frame);
	
		else {
			cout << "No captured frame -- Break!" << endl;
			break;		
		}
		
		int c = waitKey(10);
		if( (char)c == 'c' ) break;
	}
return;

}


//--------------------------------------------------------------------------------------------------------------//
//Function DETECT and DISPLAY --> .AVI VIDEO FILE								//
//--------------------------------------------------------------------------------------------------------------//
void detectAndDisplay(Mat frame) 
{
	vector<Rect> faces;
	Mat frame_gray;
	
	//Convert frame to grayscale 
	cvtColor( frame, frame_gray, CV_BGR2GRAY );
	equalizeHist( frame_gray, frame_gray );

	//Detect Faces
	face_cascade.detectMultiScale(frame_gray, faces, 1.3, 4, 0|CV_HAAR_SCALE_IMAGE, Size(30, 30));

	for( int i = 0; i < faces.size(); i++) 
		{
			//center
			Point center( faces[i].x + faces[i].width*0.5, faces[i].y + faces[i].height*0.5 );
			//Draw circle in detected phase with center
			 ellipse( frame, center, Size( faces[i].width*0.5, faces[i].height*0.5), 0, 0, 360, Scalar( 0, 0, 255 ), 4, 8, 0 );

		}
	imshow("Face_detector", frame);
	return;
}


//--------------------------------------------------------------------------------------------------------------//
//Function-1: From Webcam Video Source										//
//--------------------------------------------------------------------------------------------------------------//
void function1()
{


	return;

}


	

