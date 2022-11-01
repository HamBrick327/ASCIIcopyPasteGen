import cv2

# define the video capture 
vid = cv2.VideoCapture(0)

# define an object containing an image
img = cv2.imread('rick-astley.png') # 0 as the second argument loads the image as grayscale

# create log object
log = open('log.txt', 'w')

# print the size of the array that is the loaded image
print(img.shape[:2]) # array[:2] prints the first two objects in the array

# ascii characters ordered from most to least dense (most least brightness)
density = 'Ñ@#W$9876543210?!abc;:+=-,._ '

# show the static image (same as showing video because the imshow in the loop shows each frame of the video)
cv2.imshow("image", img)

# loop through all pixels in the image and print the rgb value

'''
for i in range(img.shape[0]-1):
    for j in range(img.shape[1]-1):
        print(i, j, end='\r')
        log.write(str(i) + ' ' + str(j) + '\n')
'''
for i in range(255):
    print(i*0.10980392156862745098039215686275)


while False:

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