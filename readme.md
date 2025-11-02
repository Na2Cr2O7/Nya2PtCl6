![alt text](image.png)
# Nya2PtCl6 - 米游社AI机器人
它是基于Selenium网页自动化+Minimind AI +Minimind-V 的米游社自动化机器人。
目前包含回复功能,私信功能
发帖功能已经屏蔽，可以自行在`begin.py`打开


## 使用 
 - 打开account.txt文件，输入你的米游社账号和密码
```
账号（邮箱）
密码
```
 - 需要下载两个python环境
`1`.[Python 3.11.8](https://www.python.org/ftp/python/3.11.8/python-3.11.8-amd64.exe)
`2`.[WinPython 3.13](https://github.com/winpython/winpython/releases/download/17.2.20250920final/WinPython64-3.14.0.1dot.zip)

 - 配置StartTorchPython.cmd为你的WinPython安装路径
```
"python\python.exe" %*
```
 - 安装依赖包
对`1` :
```cmd
python -m pip install -r req1.txt
```
对`2` :
```cmd
StartTorchPython.cmd -m pip install -r req2.txt
```
 - 下载模型
下载[https://www.modelscope.cn/models/gongjy/MiniMind2-PyTorch/file/view/master/full_sft_512.pth?status=2](https://www.modelscope.cn/models/gongjy/MiniMind2-PyTorch/file/view/master/full_sft_512.pth?status=2)到.\out中`full_sft_512.pth`
下载`clip-vit-base-patch16`到.`.\VisionModel\vision_model`中
由于Minimind-V的模型扩展名有误，下载
[https://wwrk.lanzoub.com/b0kojkqch](https://wwrk.lanzoub.com/b0kojkqch)
密码:727h
到.\VisionModel中并解压

安装chrome
安装ollama

- 运行
AnswerUtil7.cmd 启动ai模型
Launch.cmd 启动网页自动化
startImageVisionUtil.cmd 启动图像识别

 - 私信功能
请在手机模拟器上安装好米游社app并登录
将手机模拟器的快捷方式改成`emulator.lnk`放到根目录下
下载[`platform-tools`](https://developer.android.google.cn/tools/releases/platform-tools?hl=zh-cn)解压到根目录下


## 开源协议
Minimind和Minimind-V在MIT协议下开源，Nya2PtCl6在the Unlicense协议下开源。

    