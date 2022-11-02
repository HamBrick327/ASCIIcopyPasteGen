import cv2

# define the video capture 
vid = cv2.VideoCapture(0)

while True:

    # capture video frame by frame
    frame = vid.read()[1] # vid.read()[1] only reads the array of the single frame, there is another attribute that comes before it in the video
    print(frame)

    # display captured video
    cv2.imshow("frame", frame) # frame object is updated every recursion; doesn't make new window, only updates existing window

    # q set at close keybind
    if cv2.waitKey(1) & 0xFF == ord('q'): ## if statement doesn't like 'and'; must use '&'
        break

# release video capture object
vid.release()
# kill all windows
cv2.destroyAllWindows()