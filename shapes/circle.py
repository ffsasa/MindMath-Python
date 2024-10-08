import os
import tempfile  # Sử dụng để tạo file tạm thời
import time  # Để sử dụng timestamp
from manim import *
from utils.firebase_utils import upload_video

def draw_circle_and_upload(radius):
    # Tạo thư mục tạm thời để lưu video
    with tempfile.TemporaryDirectory() as temp_dir:
        # Đặt tên file video với timestamp
        timestamp = int(time.time())  # Lấy timestamp hiện tại
        output_file = os.path.join(temp_dir, f"circle_radius_{radius}_{timestamp}.mp4")
        
        # Cấu hình đầu ra cho Manim để lưu video vào thư mục tạm thời
        config.media_dir = temp_dir
        config.output_file = output_file

        class DrawCircle(Scene):
            def construct(self):
                circle = Circle(radius=radius)
                circle.set_fill(PINK, opacity=0.5)
                self.play(Create(circle))

        try:
            # Tạo video của hình tròn
            scene = DrawCircle()
            scene.render()

            print(f"Đã tạo video cho hình tròn có bán kính {radius} tại {output_file}")
            
            # Upload video lên Google Drive
            link_video = upload_video(output_file)
            print("Đã upload video lên Firebase.")
            return link_video
        except Exception as e:
            print(f"Lỗi khi vẽ và upload video: {str(e)}")
