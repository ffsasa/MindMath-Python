import os
import time
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from config import settings

def upload_to_google_drive(file_path, mime_type):
    # Xác thực với Google Drive
    creds = service_account.Credentials.from_service_account_file(
        settings.GOOGLE_DRIVE_API_CREDENTIALS, scopes=['https://www.googleapis.com/auth/drive.file']
    )
    service = build('drive', 'v3', credentials=creds)

    file_metadata = {
        'name': os.path.basename(file_path),
        'parents': [settings.GOOGLE_DRIVE_FOLDER_ID]  # Sử dụng ID thư mục từ settings.py
    }
    media = MediaFileUpload(file_path, mimetype=mime_type)

    # Tải file lên Google Drive
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    file_id = file.get('id')
    print(f"Đã tải lên file tới Google Drive với ID: {file.get('id')}")

    # Tạo liên kết đến file đã upload
    video_link = f"https://drive.google.com/file/d/{file_id}/view"
    return video_link  # Trả về liên kết
