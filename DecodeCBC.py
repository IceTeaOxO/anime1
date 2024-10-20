import os
from Crypto.Cipher import AES
import glob

def decrypt_ts_files(input_directory, key, output_directory):
    os.makedirs(output_directory, exist_ok=True)
    ts_files = glob.glob(os.path.join(input_directory, "plist*.ts"))

    for ts_file in sorted(ts_files):
        with open(ts_file, "rb") as f:
            encrypted_content = f.read()

        # 假設使用 CBC 模式，IV 為 16 個零字節
        iv = b'\x00' * 16
        cipher = AES.new(key, AES.MODE_CBC, iv)

        # 解密內容
        decrypted_content = b''
        for i in range(0, len(encrypted_content), 16):
            chunk = encrypted_content[i:i+16]
            if len(chunk) == 16:
                decrypted_chunk = cipher.decrypt(chunk)
                decrypted_content += decrypted_chunk

        # 保存解密後的文件
        output_file = os.path.join(output_directory, os.path.basename(ts_file))
        with open(output_file, "wb") as f:
            f.write(decrypted_content)

        print(f"已解密: {ts_file}")

    print("所有文件已解密完成。")

# 使用示例
# input_directory = "關於地球的運動-1"
# output_directory = "關於地球的運動--1"
# key = b"wjptcc9H3HJtkGbu"  # 16 字節的密鑰

# decrypt_ts_files(input_directory, key, output_directory)
