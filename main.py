import cv2

image = cv2.imread('ok.jpg', cv2.IMREAD_UNCHANGED)

scale_percent = 50

new_width = int(image.shape[1] * scale_percent / 100)
new_height = int(image.shape[0] * scale_percent / 100)

new_size = (new_width, new_height)

output = cv2.resize(image, new_size)

cv2.imwrite('new_img.png', output)

cv2.waitKey(0)