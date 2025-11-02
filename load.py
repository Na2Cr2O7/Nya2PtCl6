import sys
import time

def loading_animation():
    loading_chars = ['|', '/', '-', '\\']
    while True:
        for char in loading_chars:
            sys.stdout.write('\r' + char)  # 使用 \r 让光标回到行首
            sys.stdout.flush()  # 刷新输出
            time.sleep(0.1)  # 控制动画速度

try:
    print("加载中，请稍候...")
    loading_animation()
except KeyboardInterrupt:
    print("\r加载停止。")

