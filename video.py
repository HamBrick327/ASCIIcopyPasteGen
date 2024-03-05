import cv2

# define the video capture 
vid = cv2.VideoCapture(0)
firstFrame = vid.read()[1]


for i in range(500):

    # capture video frame by frame
    frame = vid.read()[1] # vid.read()[1] only reads the array of the single frame, there is another attribute that comes before it in the video
    #print(frame)

    # capures the third frame of the video capture
    if i == 3:
        thirdFrame = vid.read()[1]


    # display captured video
    cv2.imshow("frame", frame) # frame object is updated every recursion; doesn't make new window, only updates existing window
    cv2.imshow("first frame", firstFrame) ## hopefully the fist frame of the video capture
    try:
        cv2.imshow("third frame", thirdFrame) ## displays the third frame of the video capture
    except:
        print("there is no third frame in ba sing se")

    # q set at close keybind
    if cv2.waitKey(1) & 0xFF == ord('q'): ## if statement doesn't like 'and'; must use '&'
        break ## this if statement is required apparently

# release video capture object
vid.release()
# kill all windows
cv2.destroyAllWindows()