import base64
import streamlit as st

st.set_page_config(
    page_title="Hệ Thống Lời Chào Taxi Xanh SM", page_icon="🚙", layout="centered"
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
  # Giao diện HTML + CSS phong cách Xanh SM đặc trưng
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
                /* Background chuẩn màu xanh ngọc đặc trưng của Xanh SM */
                background: linear-gradient(135deg, #002d3a, #005f73, #0a9396);
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                padding: 15px;
            }}
            .card {{
                background: #ffffff;
                width: 100%;
                max-width: 440px;
                padding: 25px 20px;
                border-radius: 24px;
                box-shadow: 0 15px 35px rgba(0, 0, 0, 0.35);
                text-align: center;
            }}
            .taxi-banner {{
                position: relative;
                width: 100%;
                height: 170px;
                border-radius: 16px;
                overflow: hidden;
                margin-bottom: 20px;
                box-shadow: 0 6px 15px rgba(0, 0, 0, 0.15);
            }}
            .taxi-banner img {{
                width: 100%;
                height: 100%;
                object-fit: cover;
            }}
            .taxi-badge {{
                position: absolute;
                bottom: 10px;
                left: 50%;
                transform: translateX(-50%);
                background: rgba(0, 45, 58, 0.85);
                color: #00f5d4;
                padding: 6px 16px;
                border-radius: 20px;
                font-size: 13px;
                font-weight: bold;
                letter-spacing: 0.5px;
                backdrop-filter: blur(5px);
                border: 1px solid rgba(0, 245, 212, 0.3);
            }}
            h2 {{
                color: #002d3a;
                font-size: 22px;
                margin-bottom: 6px;
            }}
            p {{
                color: #666;
                font-size: 14px;
                margin-bottom: 22px;
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
                border-radius: 14px;
                cursor: pointer;
                transition: all 0.2s ease;
                display: flex;
                align-items: center;
                justify-content: center;
                gap: 12px;
                box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            }}
            button:active {{
                transform: scale(0.97);
            }}
            .btn-welcome {{
                background: linear-gradient(135deg, #009688, #00b4d8);
            }}
            .btn-welcome:hover {{
                opacity: 0.92;
            }}
            .btn-farewell {{
                background: linear-gradient(135deg, #d90429, #ef233c);
            }}
            .btn-farewell:hover {{
                opacity: 0.92;
            }}
            .icon {{
                font-size: 22px;
            }}
            
            /* Responsive cho điện thoại nhỏ */
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
            <!-- Hình ảnh minh họa xe điện chuyên nghiệp -->
            <div class="taxi-banner">
                <img src="https://images.unsplash.com/photo-1563720223185-11003d516935?auto=format&fit=crop&w=800&q=80" alt="Taxi Xanh SM">
                <div class="taxi-badge">🚙 TAXI XANH SM</div>
            </div>

            <h2>Hệ Thống Lời Chào Tự Động</h2>
            <p>Chạm vào nút tương ứng khi khách lên hoặc xuống xe</p>

            <div class="button-group">
                <!-- Nút Lên Xe -->
                <button class="btn-welcome" onclick="playAudio('welcomeAudio')">
                    <span class="icon">🚗</span> Lên Xe (Phát Chào Mừng)
                </button>
                
                <!-- Nút Xuống Xe -->
                <button class="btn-farewell" onclick="playAudio('farewellAudio')">
                    <span class="icon">🏁</span> Xuống Xe (Thông Báo Dừng)
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

  # Hiển thị giao diện lên Streamlit
  st.components.v1.html(html_code, height=500)
