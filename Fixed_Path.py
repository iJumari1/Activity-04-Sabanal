import cv2 as cv

print("Printing Krazy Yor please wait...")

loc = 'yor.jpg'
image = cv.imread(loc, 1)
cv.imshow("Krazy Yor", image)
cv.waitKey(0)
cv.destroyAllWindows()