import cv2

# flag 1  --  load image in color
# flag 0  --  load image in greyscale
# flag -1 --  load images in original format with alpha channel
print("Reading Image")
img = cv2.imread('images/lena.jpg',0)
print(img)
cv2.imshow('Image', img)
press_key = cv2.waitKey(0)
if press_key == 27:
    print("User press esc key, destroy all windows")
    cv2.destroyAllWindows()
elif press_key == ord('s'):
    print("User press s key to save image")
    cv2.imwrite('lena_copy.jpg',img)
    cv2.destroyAllWindows()
print("Close")
