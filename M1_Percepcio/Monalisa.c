//Libraries
#include <stdio.h>
#include <stdlib.h> 
#include <math.h>
//#include <chplot.h>


#define PI 3.14159265


main()
{
	//Variables
	int Selection;	
	int Selection2;	
	int Distance;
	float MLisaW;
	float MLisaH;
	
	//Pixel and camera parameters
	float Sp= 0.00408; 	
	int Sw= 1288; 		
	int Sh= 728; 		
	float f= 8; 		
	printf ("\n Camera resolution is %dx%d Pixels", Sw, Sh);
	printf ("\n Lense is %f mm \n", f);


	
	//Can calculate pixels of Mona Lisa picture or any other picture with dimensions entered by user	
	printf (" \n Do you want calculate the number of pixels of mona Lisa or other picture?");
	printf (" \n                            Select Your Option:");
	printf (" \n ----------------------------------------------------------------------------");	
	printf (" \n 1: MONA LISA PIXELS");
	printf (" \n 2: OTHER PICTURE PIXELS");
	printf (" \n ----------------------------------------------------------------------------");
	do 
	{		
		printf (" \n Enter Your Selection: ");
		scanf("%d", &Selection);
		if (Selection>=3 || Selection<=0)
		{
			printf (" Selection must be 0 or 1, Try again!");
		}	
	}while((Selection>=3) || (Selection<=0));
	printf (" Your selection is: %d", Selection);

	

	if (Selection==1)
	{
		MLisaW = 0.77;//Mona Lisa Width in meters (Landscape orientation)
		MLisaH = 0.53;//Mona Lisa Height in meters (Landscape orientation)
		printf ("\n Mona Lisa Width: %f Meters. Mola Lisa Heght: %f Meters", MLisaW, MLisaH);
	}
	else
	{
		printf ("\n Insert the Width in meters of the picture: ");		
		scanf("%f", &MLisaW);
		printf ("\n Insert the Height in meters of the picture: ");
		scanf("%f", &MLisaH);
		printf ("\n Your selection is: %f meters of Width and %f meteres of Height", MLisaW, MLisaH);

	}
	
	float Angle_w = (2*(atan (Sp*Sw/(2*f))));
	float Angle_h = (2*(atan (Sp*Sh/(2*f))));
	float Angle_w_Degress = (Angle_w*180)/PI;
	float Angle_h_Degress = (Angle_h*180)/PI;
	printf ("\n Angle W: %f Degress", Angle_w_Degress);
	printf ("\n Angle H: %f Degress", Angle_h_Degress);

	
	//Can calculate pixels at 1 to 10 meters or at a specific distance introduced by user
	printf (" \n Do you want calculate at 1-10 meters or to a Specific distance ?");
	printf (" \n                            Select Your Option:");
	printf (" \n ----------------------------------------------------------------------------");	
	printf (" \n 1: At 1 to 10 meters");
	printf (" \n 2: To a Specific distance");
	printf (" \n ----------------------------------------------------------------------------");
	do 
	{		
		printf (" \n Enter Your Selection: ");
		scanf("%d", &Selection2);
		if (Selection2>=3 || Selection2<=0)
		{
			printf (" Selection must be 1 or 2, Try again!");
		}	
	}while((Selection2>=3) || (Selection2<=0));
	printf (" Your selection is: %d", Selection2);


	if (Selection2==1)
	{
		//Calculate distance at 1-10 meters for bucle
		//array double xx[10], yy[10];		
		for (Distance=1; Distance<11; Distance++)	
		{
			//Total Widh of Image at distance 
			float HipotW = Distance /(cos(Angle_w/2)); 			
    			float W_Image = 2* HipotW * sin(Angle_w/2);	
    			printf ("\n Total wide of image in meters: %f", W_Image);
			
			//Total Height of Image at distance
			float HipotH = Distance /(cos(Angle_h/2)); 		
    			float H_Image = 2* HipotH * sin(Angle_h/2);	
			printf ("\n Total height of image in meters: %f", H_Image);

			//PIXELS OF IMAGE
			float MLisaW_pixels = Sw * (MLisaW/W_Image);	 
    			float MLisaH_pixels = Sh * (MLisaH/H_Image);	
			printf ("\n ----------------------------------------------");
			printf ("\n Mona Lisa width pixels: %f at %d Meteres", MLisaW_pixels,Distance);
			printf ("\n Mona Lisa height pixels: %f at %d Meters", MLisaH_pixels,Distance);
			printf ("\n ----------------------------------------------");
			
			//xx[Distance]=Distance
			//yy[Distance]=MLisaW_pixels
		}
		//plotxy(xx, yy, "WEIGHT PIXELS PLOT", "xlabel", "ylabel");
		
	}
	else
	{
		//Calculate at Specific distance		
		printf ("\n Insert distance in meters:");
		scanf("%d", &Distance);
		printf ("Pixels will be calulated at %d Meters", Distance);
		
		//Total Widh of Image at distance 
		float HipotW = Distance /(cos(Angle_w/2)); 		
    		float W_Image = 2* HipotW * sin(Angle_w/2);	
    		printf ("\n Total wide of image in meters: %f", W_Image);
		
		//Total Height of Image at distance
		float HipotH = Distance /(cos(Angle_h/2)); 		//Get valu of Hipot angle h
    		float H_Image = 2* HipotH * sin(Angle_h/2);	//Obtains Total height of image for current distance in meters
		printf ("\n Total height of image in meters: %f", H_Image);

		//PIXELS OF IMAGE
		float MLisaW_pixels = Sw * (MLisaW/W_Image);	//Obtain Mona Lisa width pixels as proportion of total image 
    		float MLisaH_pixels = Sh * (MLisaH/H_Image);	//Obtain Mona Lisa height pixels as proportion of total image
		printf ("\n ----------------------------------------------");
		printf ("\n Mona Lisa width pixels: %f at %d Meteres", MLisaW_pixels,Distance);
		printf ("\n Mona Lisa height pixels: %f at %d Meters", MLisaH_pixels,Distance);
		printf ("\n ----------------------------------------------");
	
	}
	

	

}


