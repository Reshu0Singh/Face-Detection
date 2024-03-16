
import cv2
face_cap = cv2.CascadeClassifier("C:/Users/reshu/AppData/Local/Programs/Python/Python312/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
video_cap = cv2.VideoCapture(0)
while True:
    ret , video_data = video_cap.read()                  #caputure of data read
    col = cv2.cvtColor(video_data,cv2.COLOR_BGR2GRAY)    #view color ko black and white ke form me show kr rha hai like eyes,ebrow,lips etc capture it
    faces = face_cap.detectMultiScale( 
        col,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30,30),
        flags=cv2.CASCADE_SCALE_IMAGE
     )
    for (x,y,w,h) in faces:     #for loop using for creating a box where x,y codinates and w,h width and height (0,255,0=color)
      cv2.rectangle(video_data,(x,y),(x+w,y+h),(0,255,0),2)         
    cv2.imshow("video_live",video_data)  #imshow ki help se data show hua hai
    if cv2.waitKey(10 ) == ord("a"):   #a button se close hoga crama
        break
video_cap.release()    
        
#import cv2  # module of open  #carama enable keliye ye code
#video_cap = cv2.VideoCapture(0)
#while True:
#    ret , video_data = video_cap.read()
#    cv2.imshow("video_live",video_data)
#    if cv2.waitKey(10 ) == ord("a"):   #a button se close hoga crama
#      break
#video_cap.release()    
    
    
