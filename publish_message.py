import redis
from config import settings


# Kết nối đến Redis
r = redis.Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_POST,
    password=settings.REDIS_PASSWORD,  # Thay bằng Primary Access Key của bạn
)

# Tên kênh mới
channel_name = settings.REDIS_CHANEL_SUB

# Gửi thông điệp đến kênh mới
r.publish(channel_name, '1;Quadratic;-1,4,-3;123123')