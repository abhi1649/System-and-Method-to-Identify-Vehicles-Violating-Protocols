import cv2

# test image
image = cv2.imread('seg.png')
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(grayImage,100,100)

histogram = cv2.calcHist([edges], [0],
                         None, [256], [0, 256])

# data1 image
image1 = cv2.imread('t2.png')
grayImage1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
edges1 = cv2.Canny(grayImage1,100,100)


histogram1 = cv2.calcHist([edges1], [0],
                          None, [256], [0, 256])

# data2 image
image2 = cv2.imread('seg2.png')
grayImage2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
edges2 = cv2.Canny(grayImage2,100,100)


histogram2 = cv2.calcHist([edges2], [0],
                          None, [256], [0, 256])

c1, c2 = 0, 0

# Euclidean Distace between data1 and test
i = 0
while i < len(histogram) and i < len(histogram1):
    c1 += (histogram[i] - histogram1[i]) ** 2
    i += 1
c1 = c1 ** (1 / 2)

# Euclidean Distace between data2 and test
i = 0
while i < len(histogram) and i < len(histogram2):
    c2 += (histogram[i] - histogram2[i]) ** 2
    i += 1
c2 = c2 ** (1 / 2)

if (c1 < c2):
    print("HOLOGRAM FOUND!!!")
else:
    print("HOLOGRAM NOT FOUND!!!")