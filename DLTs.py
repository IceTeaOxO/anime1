import requests
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

def download_file(url, output_folder):
    response = requests.get(url)
    if response.status_code == 200:
        filename = url.split('/')[-1]
        filepath = os.path.join(output_folder, filename)
        with open(filepath, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded: {filename}")
        time.sleep(0.1)  # 避免過於頻繁的請求
        return True
    else:
        print(f"Failed to download {url}. Status code: {response.status_code}")
        return False

def crawl_ts_files(base_url, output_folder, start=0, end=9999):
    os.makedirs(output_folder, exist_ok=True)

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = []
        for i in range(start, end + 1):
            url = f"{base_url}/plist{i}.ts"
            future = executor.submit(download_file, url, output_folder)
            futures.append(future)

        for future in as_completed(futures):
            if not future.result():
                print("Encountered a non-200 status code. Stopping the download.")
                executor.shutdown(wait=False, cancel_futures=True)
                break


# if __name__ == "__main__":
#     base_url = "https://p.jisuts.com:999/hls/497/20241006/2931223"
#     output_folder = "關於地球的運動-1"  # 指定下載文件的保存目錄
    
#     crawl_ts_files(base_url, output_folder)