import cv2

img = cv2.imread('images/lena.jpg', 0)

# print(img)

cv2.imshow('lenaProcess', img)

while True:

    key = cv2.waitKey(0) & 0xFF

    if key == ord('q'):
        cv2.destroyAllWindows()
        break
    elif key == ord('s'):
        cv2.imwrite('imagesProcess/lenaProcess.png', img)
        cv2.destroyAllWindows()
        break
    else:
        print(chr(key))




