import sys
import os

from shapes import quadratic
# Thêm đường dẫn gốc vào sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.redis_subscribe import RedisSubscribe  # Class Listener để kết nối Redis
from scripts.redis_publish import RedisPublish  # Class Listener để kết nối Redis
from shapes import circle, quadratic  # Hàm vẽ và upload đã được định nghĩa
from config import settings


def main():
    # Khởi tạo listener để kết nối đến Redis
    subscribe = RedisSubscribe(
        host=settings.REDIS_HOST,
        port=settings.REDIS_POST,
        password=settings.REDIS_PASSWORD,  # Thay bằng khóa truy cập của bạn
    )

    publish = RedisPublish(
        host=settings.REDIS_HOST,
        port=settings.REDIS_POST,
        password=settings.REDIS_PASSWORD
    )
    # Lắng nghe và nhận tin nhắn
    while True:
        message = subscribe.subscribe(settings.REDIS_CHANEL_SUB)  # Phương thức listen() sẽ trả về chuỗi message
        print(f"Tin nhắn nhận được: {message}")

        # Tách tin nhắn thành các phần tử
        parts = message.split(";")
        switch_case = parts[1]

        # Kiểm tra từng trường hợp của switch case
        if switch_case == "Minimum and Maximum":
            try:
                # Phần tử thứ hai là bán kính của hình tròn
                radius = float(parts[2])
                print(f"Case 1: Vẽ hình tròn với bán kính {radius}")

                # Tạo video và upload lên Google Drive
                link_video = circle.draw_circle_and_upload(radius)
                messagereturn = parts[0] + ',' + parts[3] + ',' + link_video
                publish.publish(settings.REDIS_CHANEL_PUB, messagereturn)

            except Exception as e:
                print(f"Lỗi khi xử lý case 1: {str(e)}")
        elif switch_case == "Quadratic":
            try:
                # Phần tử thứ hai là tham số của phương trình
                parameter = parts[2]
                print(f"Case 2: Vẽ đồ thị hàm số với các tham số {parameter}")

                parameters = parameter.split(",")
                a = float(parameters[0])
                b = float(parameters[1])
                c = float(parameters[2])
                # Tạo video và upload lên Google Drive
                link_video = quadratic.draw_parabola_and_upload(a,b,c)
                messagereturn = parts[0] + ',' + parts[3] + ',' + link_video
                publish.publish(settings.REDIS_CHANEL_PUB, messagereturn)

            except Exception as e:
                print(f"Lỗi khi xử lý case 2: {str(e)}")

        else: 
            print(f"Không có hành động cho switch case {switch_case}")


if __name__ == "__main__":
    main()
