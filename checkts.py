import os
import subprocess

def check_ts_file(file_path):
    try:
        result = subprocess.run(
            ['ffprobe', '-v', 'error', '-show_entries', 'stream=codec_type', '-of', 'default=noprint_wrappers=1:nokey=1', file_path],
            capture_output=True,
            text=True
        )
        if 'video' in result.stdout or 'audio' in result.stdout:
            return True
        else:
            return False
    except subprocess.CalledProcessError:
        return False

def check_all_ts_files(folder_path):
    ts_files = [f for f in os.listdir(folder_path) if f.endswith('.ts')]
    
    for ts_file in ts_files:
        file_path = os.path.join(folder_path, ts_file)
        if check_ts_file(file_path):
            print(f"{ts_file} 可以被播放")
        else:
            print(f"{ts_file} 可能有問題，無法播放")

# 使用示例
# folder_path = "關於地球的運動--1"  # 包含 .ts 文件的文件夾
# check_all_ts_files(folder_path)
