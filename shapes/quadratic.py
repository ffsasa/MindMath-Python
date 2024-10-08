import os
import tempfile  # Sử dụng để tạo file tạm thời
import time  # Để sử dụng timestamp
from manim import *
from utils.firebase_utils import upload_video

def draw_parabola_and_upload(a, b, c):
    # Tạo thư mục tạm thời để lưu video
    with tempfile.TemporaryDirectory() as temp_dir:
        # Đặt tên file video với timestamp
        timestamp = int(time.time())  # Lấy timestamp hiện tại
        output_file = os.path.join(temp_dir, f"parabola_a{a}_b{b}_c{c}_{timestamp}.mp4")
        
        # Cấu hình đầu ra cho Manim để lưu video vào thư mục tạm thời
        config.media_dir = temp_dir
        config.output_file = output_file

        class DrawParabola(Scene):
            def construct(self):
                # Định nghĩa hàm số bậc 2: y = ax^2 + bx + c
                quadratic_function = lambda x: a*x**2 + b*x + c
                
                # Tạo trục x, y với phạm vi và màu sắc
                axes = Axes(
                    x_range=[-10, 10],  # Đặt phạm vi của trục x
                    y_range=[-10, 10],  # Đặt phạm vi của trục y
                    axis_config={"color": BLUE}
                )
                
                # Vẽ đồ thị của hàm số y = ax^2 + bx + c
                graph = axes.plot(quadratic_function, color=YELLOW)
                
                # Thêm các thành phần đồ thị vào scene
                # Bước 1: Vẽ trục trước
                self.play(Create(axes, run_time=3))  # Vẽ trục chậm lại trong 3 giây
                
                # Bước 2: Vẽ đồ thị hàm số từ từ
                self.play(Create(graph, run_time=4))  # Vẽ đồ thị chậm lại trong 4 giây
                self.wait(1)  # Dừng lại 2 giây để xem kết quả

        try:
            # Tạo video của đồ thị Parabol
            scene = DrawParabola()
            scene.render()

            print(f"Đã tạo video cho đồ thị y = {a}x^2 + {b}x + {c} tại {output_file}")
            
            # Upload video lên Google Drive
            link_video = upload_video(output_file)
            print("Đã upload video lên Firebase.")
            return link_video
        except Exception as e:
            print(f"Lỗi khi vẽ và upload video: {str(e)}")
