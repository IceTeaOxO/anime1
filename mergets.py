import os
import subprocess

def merge_ts_files(input_folder, output_file):
    # 獲取所有 .ts 文件並按名稱排序
    ts_files = sorted([f for f in os.listdir(input_folder) if f.endswith('.ts')])
    
    if not ts_files:
        print("沒有找到 .ts 文件")
        return

    print(f"找到 {len(ts_files)} 個 .ts 文件")

    # 準備 FFmpeg 命令
    ffmpeg_command = ['ffmpeg']
    
    # 為每個 ts 文件添加輸入
    for ts_file in ts_files:
        ffmpeg_command.extend(['-i', os.path.join(input_folder, ts_file)])
    
    # 添加合併和輸出參數
    ffmpeg_command.extend([
        '-filter_complex', f'concat=n={len(ts_files)}:v=1:a=1[outv][outa]',
        '-map', '[outv]',
        '-map', '[outa]',
        output_file
    ])

    print("開始執行 FFmpeg 命令")
    print(f"FFmpeg 命令: {' '.join(ffmpeg_command)}")

    try:
        result = subprocess.run(ffmpeg_command, check=True, text=True, capture_output=True)
        print(f"FFmpeg 輸出: {result.stdout}")
        print(f"所有 .ts 文件已成功合併為 {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"FFmpeg 執行錯誤: {e}")
        print(f"FFmpeg 標準輸出: {e.stdout}")
        print(f"FFmpeg 錯誤輸出: {e.stderr}")

# 使用示例
input_folder = "關於地球的運動--1"  # 包含 .ts 文件的文件夾
output_file = "merged_video.mp4"  # 輸出的 MP4 文件名

merge_ts_files(input_folder, output_file)
