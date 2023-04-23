
import cv2, numpy, os, argparse

DEFAULT_OUTPUT_PATH = "new/"
DEFAULT_CASCADE_INPUT_PATH = '10.1_-_Haarcascade_Frontalface_Alt.xml'
class VideoCapture : 
	def __init__(self):
		self.count = 0 
		self.argobj = Parse()
		self.faceCascade = cv2.CascadeClassifier(self.argobj.input_path)
		self.videoSource = cv2.VideoCapture(0)
		
	def CaptureFrame(self): 
		while True : 
			#Create a unique number for each frame
			frameNumber = "%08d" % (self.count)
			
			#Capture frame by frame 
			ret, frame = self.videoSource.read()
			
			# set screen color to gray, so the haar cascade can easily detect edges and faces
			screenColor = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
			
			#customize how the cascade detects your faces
			faces = self.faceCascade.detectMultiScale(
				screenColor,
				scaleFactor = 1.1,
				minNeighbors = 5,
				minSize = (30,30),
				flags = cv2.CASCADE_SCALE_IMAGE)
				
			#Display the resulting frame
			cv2.imshow("SPYING ON YOU!", frame)
			
			# if the len of face is 0. there have been no faces detected
			
			if len(faces) == 0:
				pass 
			# if the face is detected, face return 1 or more depending n the mou    nt of face detected
			elif len(faces) > 0:
				print("face Detected")
				
				#graph the face and draw the rectangle arount it 
				for (x, y, w, h) in faces:
					cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)
				
				cv2.imwrite(DEFAULT_OUTPUT_PATH + frameNumber + ".png" , frame)
				
			#Increment count so we get a unique name for each frame
			self.count +=1
			
		
			# if 'esc' is hit, the video is closed. we are only going to wait a fraction of second per loop
			#if cv.waitKay(0) == 27:
			#	break
			
			
			#when every thing i done, release the capture adn closed windows

			#self.videoSource.release()
			#cv.waitKay(500)
			#self.destroyAllWindows()
			
			
			
def Parse():
        parser = argparse.ArgumentParser(description='Cascade path fo  face detection')
        parser.add_argument("-i", "--input_path", type=str, default=DEFAULT_CASCADE_INPUT_PATH, help='Cascade input path')
        parser.add_argument("-o", "--output_path", type=str, default=DEFAULT_OUTPUT_PATH, help='Output path for picture taken')			
        args = parser.parse_args()
        return args









				
			
def main():

	if not os.path.exists(DEFAULT_OUTPUT_PATH):
		
		os.makedirs(DEFAULT_OUTPUT_PATH)
		
	faceDetectImplemention = VideoCapture()
		
	#call capture from class to begin face detection
	faceDetectImplemention.CaptureFrame()
		
		

main()
		
		
		
