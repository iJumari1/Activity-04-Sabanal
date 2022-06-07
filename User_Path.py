import cv2 as cv
import os

while True:

    file = input(" \nEnter File name: ")
    fName = str(file + '.jpg')

    print('You want it colored or Nah? \nPlease press [1] or [2]')

    flag = int(input("[1] Colored  \n[2] Grayscale \nEnter Flag Values: "))

    if flag == 1:
        if os.path.exists(fName):
            image = cv.imread(fName, 1)
            if file == 'anya':
                name = 'Esper Child'
                cv.imshow(name, image)
                cv.waitKey(0)
                cv.destroyAllWindows()
                break

            if file == 'yor':
                name = 'Deadly Assassin'
                cv.imshow(name, image)
                cv.waitKey(0)
                cv.destroyAllWindows()
                break

        else:
            print("File not found...")

    elif flag == 2:
        if os.path.exists(fName):
            image = cv.imread(fName, 0)
            if file == 'anya':
                name = 'Esper Child'
                cv.imshow(name, image)
                cv.waitKey(0)
                cv.destroyAllWindows()
                break

            if file == 'yor':
                name = 'Deadly Assassin'
                cv.imshow(name, image)
                cv.waitKey(0)
                cv.destroyAllWindows()
                break

        else:
            print("File not found...")

    else:
        print("Error Flag...")