# В зображеннях saturn2.gif та saturn3.gif подавити імпульсний шум.
# Описати алгоритм подавлення шуму та програмно реалізувати його,
# надіслати до 12:00 01.04.2021  код програми та її результати
# (код програми, початкове та відповідно оброблене зображення).
# Висилати файл в PDF форматі.




import numpy
from PIL import Image


def MedianFilter(data, f_size):
    # Temp array
    temp = []
    # Index
    ind = f_size // 2

    # Result array
    result = []
    result = numpy.zeros((len(data),len(data[0])))
    for i in range(len(data)):
        for j in range(len(data[0])):
            for z in range(f_size):
                if i + z - ind < 0 or i + z - ind > len(data) - 1:
                    for c in range(f_size):
                        temp.append(0)
                else:
                    if j + z - ind < 0 or j + ind > len(data[0]) - 1:
                        temp.append(0)
                    else:
                        for k in range(f_size):
                            temp.append(data[i + z - ind][j + k - ind])

            # Sorting
            temp.sort()
            result[i][j] = temp[len(temp) // 2]
            temp = []

    return result


def main():
    # get gif file
    img = Image.open("Saturn2.gif").convert("L")
    arr = numpy.array(img)

    # Filter
    removed_noise = MedianFilter(arr, 3)


    # Show
    img = Image.fromarray(removed_noise)
    img.save("Saturn2DONE.gif")


main()
































# import numpy as np
# import cv2 as cv
# from matplotlib import pyplot as plt
#
# img = cv.imread('Saturn2.png')
#
# dst = cv.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)
# plt.subplot(121),plt.imshow(img)
# plt.subplot(122),plt.imshow(dst)
#
# plt.show()