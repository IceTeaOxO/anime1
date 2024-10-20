from DLTs import crawl_ts_files
from DecodeCBC import decrypt_ts_files
from MergeTsByNumber import merge_ts_files



if __name__ == "__main__":
    base_url = "https://p.jisuts.com:999/hls/497/20241013/2947321"
    output_folder = "關於地球的運動-3"  # 指定下載文件的保存目錄
    key = b"Cn2olk8mEqZyNbDU"  # 16 字節的密鑰
    output_file = output_folder+".mp4"  # 輸出的 MP4 文件名
    
    crawl_ts_files(base_url, output_folder)

    input_directory = output_folder
    output_directory = output_folder
    

    decrypt_ts_files(input_directory, key, output_directory)

    input_folder = output_folder  # 包含 .ts 文件的文件夾
    

    merge_ts_files(input_folder, output_file)