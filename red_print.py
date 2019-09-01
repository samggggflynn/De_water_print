import cv2
import numpy as np


def draw_rectangle_r(event, x, y, flags, param):
    global ix, iy

    if event==cv2.EVENT_LBUTTONDOWN:
        ix, iy = x, y
        print("point1:=", x, y)
        # i+=1

    elif event==cv2.EVENT_LBUTTONUP:
        print("point2:=", x, y)
        print("width=",x-ix)
        print("height=", y - iy)

        roi_area = img[iy:y,ix:x]

        hsv_image = cv2.cvtColor(roi_area, cv2.COLOR_BGR2HSV)
        high_range = np.array([180, 255, 255])
        low_range = np.array([156, 43, 46])
        high_range1 = np.array([10, 255, 255])
        low_range1 = np.array([0, 43, 46])
        th = cv2.inRange(hsv_image, low_range, high_range)
        th1 = cv2.inRange(hsv_image, low_range1, high_range1)

        dst = cv2.inpaint(roi_area, th + th1, 3, cv2.INPAINT_TELEA)
        # cv2.imshow('dst', dst)

        img[iy:y, ix:x]= dst
        # cv2.imshow("image", img)
        cv2.imwrite("new_img.jpg", img)
        # while(1):
        cv2.imshow("image",img)
        if cv2.waitKey(0) & 0xFF == ord('s'):
            cv2.imwrite("new_img.jpg", img)
            print("图像已经保存")


if __name__ == '__main__':

    img = cv2.imread("input1.png")  #加载图片

    cv2.namedWindow('image')
    cv2.setMouseCallback('image', draw_rectangle_r)

    cv2.imshow('image', img)
    # if cv2.waitKey(20) & 0xFF == ord('y'):
    #     cv2.imshow('image',)
    #     break
    # if cv2.waitKey(20) & 0xFF == ord('q'):
    #     break
    cv2.waitKey(0)
    cv2.destroyAllWindows()
