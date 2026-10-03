import base64
import streamlit as st

st.set_page_config(
    page_title="Hệ Thống Lời Chào Xe Taxi", page_icon="🚕", layout="centered"
)


# Hàm chuyển đổi file âm thanh sang Base64
def get_audio_base64(file_path):
  try:
    with open(file_path, "rb") as f:
      data = f.read()
    return base64.b64encode(data).decode()
  except FileNotFoundError:
    return None


# Lấy dữ liệu mã hóa của 2 file âm thanh
audio_len_base64 = get_audio_base64("lenxe.mp3")
audio_xuong_base64 = get_audio_base64("xuongxe.mp3")

if not audio_len_base64 or not audio_xuong_base64:
  st.error(
      "⚠️ Không tìm thấy file `lenxe.mp3` hoặc `xuongxe.mp3`. Hãy kiểm tra lại"
      " tên file trong thư mục GitHub của bạn!"
  )
else:
  # Giao diện HTML + CSS Responsive & Hình ảnh xe Taxi
  html_code = f"""
    <!DOCTYPE html>
    <html lang="vi">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            * {{
                box-sizing: border-box;
                margin: 0;
                padding: 0;
            }}
            body {{
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
                background-color: #f8f9fa;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                padding: 10px;
            }}
            .card {{
                background: #ffffff;
                width: 100%;
                max-width: 450px;
                padding: 25px 20px;
                border-radius: 20px;
                box-shadow: 0 10px 25px rgba(0, 0, 0, 0.08);
                text-align: center;
            }}
            .car-img-container {{
                width: 100%;
                height: 180px;
                border-radius: 12px;
                overflow: hidden;
                margin-bottom: 20px;
                box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
            }}
            .car-img-container img {{
                width: 100%;
                height: 100%;
                object-fit: cover;
            }}
            h2 {{
                color: #1a1a1a;
                font-size: 22px;
                margin-bottom: 8px;
            }}
            p {{
                color: #666;
                font-size: 14px;
                margin-bottom: 25px;
            }}
            .button-group {{
                display: flex;
                flex-direction: column;
                gap: 15px;
            }}
            button {{
                width: 100%;
                padding: 16px 20px;
                font-size: 18px;
                font-weight: bold;
                color: white;
                border: none;
                border-radius: 12px;
                cursor: pointer;
                transition: all 0.2s ease;
                display: flex;
                align-items: center;
                justify-content: center;
                gap: 10px;
                box-shadow: 0 4px 6px rgba(0,0,0,0.05);
            }}
            button:active {{
                transform: scale(0.97);
            }}
            .btn-welcome {{
                background: linear-gradient(135deg, #28a745, #20c997);
            }}
            .btn-welcome:hover {{
                opacity: 0.9;
            }}
            .btn-farewell {{
                background: linear-gradient(135deg, #007bff, #6610f2);
            }}
            .btn-farewell:hover {{
                opacity: 0.9;
            }}
            
            /* Tối ưu hóa cho màn hình điện thoại nhỏ */
            @media (max-width: 480px) {{
                .card {{
                    padding: 20px 15px;
                }}
                h2 {{
                    font-size: 20px;
                }}
                button {{
                    font-size: 16px;
                    padding: 14px;
                }}
            }}
        </style>
    </head>
    <body>

        <div class="card">
            <!-- Hình ảnh xe Taxi minh họa chuyên nghiệp -->
            <div class="car-img-container">
                <img src="https://images.unsplash.com/photo-1549399542-7e3f8b79c341?auto=format&fit=crop&w=800&q=80" alt="Taxi Car">
            </div>

            <h2>Hệ Thống Lời Chào Tự Động</h2>
            <p>Chọn thao tác bên dưới khi khách lên hoặc xuống xe</p>

            <div class="button-group">
                <!-- Nút Lên Xe -->
                <button class="btn-welcome" onclick="playAudio('welcomeAudio')">
                    🚗 Lên Xe (Phát Chào Mừng)
                </button>
                
                <!-- Nút Xuống Xe -->
                <button class="btn-farewell" onclick="playAudio('farewellAudio')">
                    🚏 Xuống Xe (Thông Báo Dừng)
                </button>
            </div>
        </div>

        <!-- Thẻ Audio ẩn -->
        <audio id="welcomeAudio" src="data:audio/mp3;base64,{audio_len_base64}"></audio>
        <audio id="farewellAudio" src="data:audio/mp3;base64,{audio_xuong_base64}"></audio>

        <script>
            function playAudio(audioId) {{
                document.querySelectorAll('audio').forEach(audio => {{
                    audio.pause();
                    audio.currentTime = 0;
                }});
                
                const audio = document.getElementById(audioId);
                audio.play().catch(error => {{
                    alert("Trình duyệt chặn phát tự động, vui lòng chạm thêm lần nữa!");
                }});
            }}
        </script>

    </body>
    </html>
    """

  # Hiển thị giao diện trên Streamlit với chiều cao thích ứng đẹp mắt
  st.components.v1.html(html_code, height=480)
