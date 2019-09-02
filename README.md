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
2. 进阶：利用 img[0:50,0:50]=img[100:150,100:150] 将图片中间内容拷贝到左上角
3. 挑战：参考文档完成人脸识别

# VSC安装
# GithubDesktop安装

# 20190909练习
1. 复习：利用vsc运行python打开一张图程序
2. 基础：队友在github上传一张图，利用vsc pull 得到图，然后显示
