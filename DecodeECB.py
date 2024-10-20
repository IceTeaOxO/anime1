import os
from Crypto.Cipher import AES
import glob

def decrypt_ts_files(input_directory, key, output_directory):
    # 確保輸出目錄存在
    os.makedirs(output_directory, exist_ok=True)

    # 獲取所有 .ts 文件
    ts_files = glob.glob(os.path.join(input_directory, "plist*.ts"))

    # 對每個文件進行解密
    for ts_file in sorted(ts_files):
        with open(ts_file, "rb") as f:
            encrypted_content = f.read()

        # 創建 AES 解密器
        # 注意：這裡假設使用 ECB 模式，如果使用 CBC 模式，需要提供 IV
        cipher = AES.new(key, AES.MODE_ECB)

        # 解密內容
        decrypted_content = cipher.decrypt(encrypted_content)

        # 去除填充
        padding_length = decrypted_content[-1]
        decrypted_content = decrypted_content[:-padding_length]

        # 保存解密後的文件
        output_file = os.path.join(output_directory, os.path.basename(ts_file))
        with open(output_file, "wb") as f:
            f.write(decrypted_content)

        print(f"已解密: {ts_file}")

    print("所有文件已解密完成。")

# 使用示例
input_directory = "關於地球的運動-1"  # 包含加密 .ts 文件的目錄
output_directory = "關於地球的運動--1"  # 解密後文件的保存目錄
key = b"wjptcc9H3HJtkGbu"  # 16 字節的密鑰

decrypt_ts_files(input_directory, key, output_directory)
