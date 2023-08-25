import cv2
from time import sleep

## variable for the final generated ascii image
generated = []
rgb = []

## this is the number used to map the brightness of the image to the brightness array
scuffedMap = 0.11372549019
aspectRatio = 0.57101980267

# define an object containing an image
img = cv2.imread('./sidTheSloth.jpg', 0) # 0 as the second argument loads the image as grayscale

# create log object; a scuffed way of creating a log of the program's output
log = open('log.txt', 'w')
output = open('output.txt', 'w')

# resize the image for optimal ascii conversion
resize = cv2.resize(img, (0, 0), fx=.1, fy=.1)
## print the size of the array that is the loaded image
# print(img.shape) # array[:2] prints the first two objects in the array
# print(resize.shape)

'''
if img.shape[0] / img.shape[1] ~= .570 than the aspect ratio is the same and image is valid
'''

# ascii characters ordered from most to least dense (most least brightness)
density = 'Ñ@#W$9876543210?!abc;:+=-,._ '
ytisned = ' _.,-=+:;cba!?01234567$W#@Ñ'

# create a function to loop through all pixels in the image and print the rgb value
def getRGB(image):
    out = ['']
    for i in range(image.shape[0]-1):
        for j in range(image.shape[1]-1):
            out[i] += ' ' + str(image[i, j])
        out.append('')
    for i in range(len(out)):
        out[i] = out[i].split(' ')
        out[i].pop(0)
    log.write(str(out))
    return out

rgb = getRGB(resize)

write = ''

## create the actual ascii art
for i in range(len(rgb)):
    for j in range(len(rgb[i])):
        rgb[i][j] = int(rgb[i][j])
        print(rgb[i][j])

        try:
            rgb[i][j] = ytisned[int(rgb[i][j] * scuffedMap)]
        except:
            pass
        write += str(rgb[i][j])
    write += '\n'

output.write(write)
# for i in range(256):
    # print(int(i * scuffedMap))

cv2.imshow("resized", resize)
cv2.waitKey(0)


# kill all windows
cv2.destroyAllWindows()
