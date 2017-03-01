OMR SHEET EVALUATOR V1.0

This software evaluates an OMR sheet (Bubble sheet) based on the key provided by the user. Currently, it only supports Multiple Choice Questions (only 1 correct answer),
however the code can easily be extended for Multiple Answer Questions too. OSE v1.0 makes extensive use of the OpenCV 3 library. 
Built on Python by Sourav Johar.

Dependencies:
	Numpy
	OpenCV (v2 or v3)
	
	The OpenCV .pyd file is contianed in the Dependencies folder under src. If OpenCV isn't installed on your system, simply copy this .pyd file and paste it under Python>Lib>site-packages
	You'll be able to run this with just these two external libraries.


More details:
	A sample key file has been included in the package. The user given key must strictly follow the same format as the sample key.
	The first line of the key must contain three numbers, separated by commas.
	The first value represents the score awarded for a coorect answer.
	The second, the points deducted for a wrong answer.
	The third, is included in the situation where an override is required. Leave it as 0, if not required.
	The next twenty lines must contain the correct options for the twenty questions.

	
	The location of the OMR sheets to be eavluated is given as the next input. It can be a folder of different OMRs or it can be a folder with a single OMR as well.
	The evaluated OMRs will be stored in a directory called Evaluated Sheets within ApplicationData.

	The software currently only works for the fixed OMR sheet design which comes with the package. (It can be found in OMR Sheet directory in ApplicationData.)
	Support for more OMR designs will be added in the future.


	
