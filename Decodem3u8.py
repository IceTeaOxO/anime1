import requests
import m3u8
from Crypto.Cipher import AES
import os

def download_and_decrypt_hls(m3u8_url, key_url):
    # 下載 m3u8 文件
    m3u8_response = requests.get(m3u8_url)
    playlist = m3u8.loads(m3u8_response.text)

    # 下載密鑰
    key_response = requests.get(key_url)
    key = key_response.content

    # 創建輸出目錄
    os.makedirs("output", exist_ok=True)

    # 下載並解密每個片段
    for i, segment in enumerate(playlist.segments):
        # 下載加密的片段
        encrypted_content = requests.get(segment.uri).content

        # 創建 AES 解密器
        iv = bytes.fromhex(segment.init_vector[2:]) if segment.init_vector else b'\0' * 16
        cipher = AES.new(key, AES.MODE_CBC, iv)

        # 解密內容
        decrypted_content = cipher.decrypt(encrypted_content)

        # 去除填充
        padding_length = decrypted_content[-1]
        decrypted_content = decrypted_content[:-padding_length]

        # 保存解密後的片段
        with open(f"output/segment_{i}.ts", "wb") as f:
            f.write(decrypted_content)

    print("所有片段已下載並解密完成。")

# 使用示例
m3u8_url = "https://p.jisuts.com:999/hls/497/20241006/2931223/plist0.m3u8"
key_url = "https://vv.jisuzyv.com/play/1aM4gjGe/enc.key"
download_and_decrypt_hls(m3u8_url, key_url)
