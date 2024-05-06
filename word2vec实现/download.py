import subprocess
import time

def install_package():
    try:
        # 尝试执行 pip 安装命令，加上 `--user` 参数
        subprocess.check_call(['pip3', 'install', 'torch', 'torchvision', 'torchaudio',
                               '--index-url', 'https://download.pytorch.org/whl/cu118', '--user'])
        print("安装成功！")
        return True
    except subprocess.CalledProcessError:
        # 处理安装失败
        print("安装失败，稍后重试...")
        return False

# 循环直到安装成功
while not install_package():
    time.sleep(60)  # 等待 60 秒后重试