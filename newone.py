import cv2
import numpy as np
from sklearn.cluster import KMeans

from PIL import Image

im1 = Image.open(r'/Users/mac/Downloads/OCR-based-Vehicle-Number-plate-Recognition-System-ANPR--master 3/data/images/plate.png')
im1.save(r'/Users/mac/Downloads/OCR-based-Vehicle-Number-plate-Recognition-System-ANPR--master 3/plate.jpg')


def make_histogram(cluster):
    """
    Count the number of pixels in each cluster
    :param: KMeans cluster
    :return: numpy histogram
    """
    numLabels = np.arange(0, len(np.unique(cluster.labels_)) + 1)
    hist, _ = np.histogram(cluster.labels_, bins=numLabels)
    hist = hist.astype('float32')
    hist /= hist.sum()
    return hist


def make_bar(height, width, color):
    """
    Create an image of a given color
    :param: height of the image
    :param: width of the image
    :param: BGR pixel values of the color
    :return: tuple of bar, rgb values, and hsv values
    """
    bar = np.zeros((height, width, 3), np.uint8)
    bar[:] = color
    red, green, blue = int(color[2]), int(color[1]), int(color[0])
    hsv_bar = cv2.cvtColor(bar, cv2.COLOR_BGR2HSV)
    hue, sat, val = hsv_bar[0][0]
    return bar, (red, green, blue), (hue, sat, val)


def sort_hsvs(hsv_list):
    """
    Sort the list of HSV values
    :param hsv_list: List of HSV tuples
    :return: List of indexes, sorted by hue, then saturation, then value
    """
    bars_with_indexes = []
    for index, hsv_val in enumerate(hsv_list):
        bars_with_indexes.append((index, hsv_val[0], hsv_val[1], hsv_val[2]))
    bars_with_indexes.sort(key=lambda elem: (elem[1], elem[2], elem[3]))
    return [item[0] for item in bars_with_indexes]


# START HERE
img = cv2.imread('plate.jpg')
height, width, _ = np.shape(img)

# reshape the image to be a simple list of RGB pixels
image = img.reshape((height * width, 3))

# we'll pick the 5 most common colors
num_clusters = 5
clusters = KMeans(n_clusters=num_clusters)
clusters.fit(image)

# count the dominant colors and put them in "buckets"
histogram = make_histogram(clusters)
# then sort them, most-common first
combined = zip(histogram, clusters.cluster_centers_)
combined = sorted(combined, key=lambda x: x[0], reverse=False)

# finally, we'll output a graphic showing the colors in order
bars = []

hsv_values = []
for index, rows in enumerate(combined):
    bar, rgb, hsv = make_bar(100, 100, rows[1])
    a = rgb
    print(f'Bar {index + 1}')
    print(a)
    
    hsv_values.append(hsv)
    bars.append(bar)

# sort the bars[] list so that we can show the colored boxes sorted
# by their HSV values -- sort by hue, then saturation
sorted_bar_indexes = sort_hsvs(hsv_values)
sorted_bars = [bars[idx] for idx in sorted_bar_indexes]

cv2.imshow('Sorted by HSV values', np.hstack(sorted_bars))
cv2.imshow(f'{num_clusters} Most Common Colors', np.hstack(bars))
cv2.waitKey(0)



TARGET_COLORS = {"Red": (255, 0, 0), "Yellow": (255, 255, 0), "Green": (0, 255, 0), "White": (255,255,255), "Blue": (0,0,255)}

def color_difference (color1, color2):
    return sum([abs(component1-component2) for component1, component2 in zip(color1, color2)])

my_color = (a)

differences = [[color_difference(my_color, target_value), target_name] for target_name, target_value in TARGET_COLORS.items()]
differences.sort()  # sorted by the first element of inner lists
my_color_name = differences[0][1]

print(my_color_name)



my_color_name = str(my_color_name)

with open('readme.txt', 'a') as f:
    f.writelines(my_color_name + "\n" )

# Open the file in read mode
text = open("readme.txt", "r")
  
# Create an empty dictionary
d = dict()
  
# Loop through each line of the file
for line in text:
    # Remove the leading spaces and newline character
    line = line.strip()
  
    # Convert the characters in line to 
    # lowercase to avoid case mismatch
    line = line.lower()
  
    # Split the line into words
    words = line.split(" ")
  
    # Iterate over each word in line
    for word in words:
        # Check if the word is already in dictionary
        if word in d:
            # Increment count of word by 1
            d[word] = d[word] + 1
        else:
            # Add the word to dictionary with count 1
            d[word] = 1
  
# Print the contents of dictionary
for key in list(d.keys()):
    print(key, ":", d[key])

