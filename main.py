import cv2
import sys

from numpy import shape

## variable for the final generated ascii image
generated = []
rgb = []

## this is the number used to map the brightness of the image to the brightness array
scuffedMap = 0.11372549019

## initialize img
img = None

# define an object containing an image
try:
    img = cv2.imread(sys.argv[1], 0)
except:
    img = cv2.imread(
        "./rick-astley.png", 0
    )  # 0 as the second argument loads the image as grayscale

# create log object; a scuffed way of creating a log of the program's output
log = open("log.txt", "w")
output = open("output.txt", "w")

# resize the image for optimal ascii conversion
## pretent img has vaules now
resize = cv2.resize(
    img, (int(img.shape[1] * 0.1), int(img.shape[0] * 0.1)), fx=0.1, fy=0.1
)
## print the size of the array that is the loaded image

"""
if img.shape[0] / img.shape[1] ~= .570 than the aspect ratio is the same and image is valid
"""

# ascii characters ordered from most to least dense (most least brightness)
density = "Ñ@#W$9876543210?!abc;:+=-,._ "
ytisned = " _.,-=+:;cba!?01234567$W#@Ñ"


# create a function to loop through all pixels in the image and print the rgb value
def getRGB(image):
    out = [""]
    for i in range(image.shape[0] - 1):
        for j in range(image.shape[1] - 1):
            out[i] += " " + str(image[i, j])
        out.append("")
    for i in range(len(out)):
        out[i] = out[i].split(" ")
        out[i].pop(0)
    log.write(str(out))
    return out


rgb = getRGB(resize)

write = ""

## create the actual ascii art
for i in range(len(rgb)):
    for j in range(len(rgb[i])):
        rgb[i][j] = int(rgb[i][j])

        try:
            ## I hate all of this code
            rgb[i][j] = density[int(rgb[i][j] * scuffedMap)]
        except:
            pass
        write += str(rgb[i][j])
    write += "\n"

output.write(write)

cv2.imshow("resized", resize)
cv2.waitKey(0)

## clean up opened files
log.close()
output.close()

# kill all windows
cv2.destroyAllWindows()
