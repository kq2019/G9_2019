# G9_2019
G9 2019 

# 检查自己的Python版本

确保是3.6版本

## 设置pip安装源为国内

安装步骤：  

在你的电脑的c:\user(或者用户)\你电脑的用户名\，这个目录下创建个命名为“pip”的文件夹（如：C:\Users\gmn\pip），在该文件夹下创建一个命名为“pip.ini”的文件，在该文件中写入以下内容：  

[global]  
index-url=https://mirrors.aliyun.com/pypi/simple/  
[install]    
trusted-host=https://mirrors.aliyun.com/pypi/simple/    
disable-pip-version-check = true    
timeout = 6000  

# OpenCV 安装
打开cmd  或 powershell  
pip install opencv-python

# 20190902练习

1. 基本：用OpenCV打开一张图，显示出来  
2. 进阶：利用 img[0:50,0:50]=img[100:150,100:150] 将图片中间内容拷贝到左上角。利用双重循环拷贝到3x3九宫格里
3. 挑战：参考文档完成人脸识别

# VSC安装
# GithubDesktop安装

# 20190909练习：棋盘制作
1.复习：利用idle运行python打开一张图程序
2.基础：画一个矩形
3.进阶：画3x3个矩形
4.挑战：9个矩形都要有不同颜色，线宽，实心空心

# 20190916练习:利用循环制作棋盘

讲解：vsc配置本地路径  
![](https://github.com/kq2019/G9_2019/blob/master/vscfix_01.JPG)  
![](https://github.com/kq2019/G9_2019/blob/master/vscfix_02.JPG)  
  
1. 复习：for 循环打印九宫格格子坐标  (0,0)  (0,1) (0,2) (1,0) .......
2. 基础：利用for循环制作左右两个棋盘
3. 进阶：棋盘格子里面统一画圆
4. 挑战：棋盘格子里统一同时画圆和X

https://gartic.io/055ZrLec

# 20190916练习：利用二维列表表示棋盘
讲解：列表与二维列表
打开idle
a=[0,1,2]
b=[10,11,12]
c=[0,1,2]
chessboard=[a,b,c]
print(chessboard)
二维列表初始化
chessboard=[[0,1,0],[0,2,0],[1,0,0]]
1.复习：双重循环画九宫格里面带圆
2.基础：双重循环画空心圆和实心圆，第一行绿色空心，第二行绿色实心，第三行红色空心
3.进阶：根据chessboard内容画绿色空心（1），绿色实心（2），不画（0）
4.挑战：利用input函数修改特定位置的棋子，比如 0，1，2 表示第0行第1列的棋子为绿色实心。



