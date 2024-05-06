import os
import ctypes

# 打印当前PATH环境变量
print("当前PATH环境变量：", os.environ['PATH'])

try:
    # 尝试加载shm.dll
    dll_path = r'C:\Users\22128\AppData\Roaming\Python\Python312\site-packages\torch\lib\shm.dll'  # 请修改为shm.dll实际的路径
    ctypes.CDLL(dll_path)
    print("加载 shm.dll 成功")
except Exception as e:
    print("加载 shm.dll 失败:", e)

# 再次打印PATH环境变量，看是否有变化
print("更新后的PATH环境变量：", os.environ['PATH'])