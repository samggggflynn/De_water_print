# Python-openCV发票去印章

`python-openCV`写了一个去除发票红色印章水印的小工具。鼠标拖拽，模拟`inpaint`图像修复的操作去除红色印章。修改HSV颜色值还可以用来去蓝色印章。

## 文档结构

输入图像`input1.png`；处理结果`new_img.jpg`。

## 操作说明

读取待处理图像：

```python
img = cv2.imread("input1.png")  #加载图片
```
鼠标拖拽完成去水印效果：

![](/images/20190901235609.png)

英文输入法下，按`s`保存：

```python
        if cv2.waitKey(0) & 0xFF == ord('s'):
            cv2.imwrite("new_img.jpg", img)
            print("图像已经保存")
```

运行时`Console`控制台输出结果为鼠标点击坐标，`point1`左上角起始点，`point2`右下角终止点，`width`为点击横跨宽幅，`heigh`为横跨高。
