import os
import shutil
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
from datetime import datetime
import schedule
import time

# Load thông tin từ file .env
load_dotenv()
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")

# Đường dẫn
SOURCE_DIR = "./Database" # thư mục hiện tại
BACKUP_DIR = "./Database/backup_folder"

# Tạo thư mục backup nếu chưa có
if not os.path.exists(BACKUP_DIR):
    os.makedirs(BACKUP_DIR)

def send_email(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_USER
    msg['To'] = EMAIL_RECEIVER

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(EMAIL_USER, EMAIL_PASSWORD)
            server.send_message(msg)
        print("Email đã gửi thành công.")
    except Exception as e:
        print("Gửi email thất bại:", e)

def backup_database():
    try:
        now = datetime.now().strftime("%Y%m%d_%H%M%S")
        files_backed_up = []

        for file in os.listdir(SOURCE_DIR):
            if file.endswith(".sql") or file.endswith(".sqlite3"):
                src_path = os.path.join(SOURCE_DIR, file)
                dst_file = f"{file}_{now}"
                dst_path = os.path.join(BACKUP_DIR, dst_file)
                shutil.copy2(src_path, dst_path)
                files_backed_up.append(dst_file)

        if files_backed_up:
            subject = "Backup thành công"
            body = f"Các file đã backup:\n" + "\n".join(files_backed_up)
        else:
            subject = "Backup thất bại"
            body = "Không tìm thấy file .sql hoặc .sqlite3 nào để backup."

        send_email(subject, body)
    except Exception as e:
        send_email("Backup thất bại", str(e))

# Đặt lịch backup mỗi ngày lúc 00:00
# schedule.every().day.at("00:00").do(backup_database)
backup_database()

print("Đang chạy tiến trình backup theo lịch...")
while True:
    schedule.run_pending()
    time.sleep(1)
