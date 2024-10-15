import os

# settings.py
GOOGLE_DRIVE_API_CREDENTIALS = os.path.join(os.path.dirname(__file__), 'credentials.json')  # Đường dẫn tới tệp JSON của API credentials
GOOGLE_DRIVE_FOLDER_ID = '1ndpGD4nG6cAmUPZreEy36TpV2NJ4Q8e4'  # ID của thư mục trên Google Drive
FIREBASE_CREDENTIALS = os.path.join(os.path.dirname(__file__), 'mindmath-firebase.json')  # Đường dẫn tới tệp JSON của API credentials
STORAGE_BUCKET_ID = 'mindmath-56a26.appspot.com' # Storage bucket trên firebase

REDIS_POST = 19901
REDIS_HOST = 'redis-19901.c56.east-us.azure.redns.redis-cloud.com'
REDIS_PASSWORD = 'ExqMLLIww8XVYKaN5GP8zHNEcdtkpx56'
REDIS_CHANEL_SUB = 'Channel1'
REDIS_CHANEL_PUB = 'Channel2'