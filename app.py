import base64
import streamlit as st

st.set_page_config(
    page_title="Hệ Thống Lời Chào Taxi", page_icon="🚕", layout="centered"
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
  # Giao diện HTML + CSS + Script chống copy & khóa chuột phải
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
                /* Chặn bôi đen (chọn) văn bản trên toàn trang */
                -webkit-user-select: none;
                -moz-user-select: none;
                -ms-user-select: none;
                user-select: none;
            }}
            body {{
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
                background: linear-gradient(rgba(0, 20, 30, 0.75), rgba(0, 20, 30, 0.85)), 
                            url('https://images.unsplash.com/photo-1549399542-7e3f8b79c341?auto=format&fit=crop&w=1200&q=80');
                background-size: cover;
                background-position: center;
                background-attachment: fixed;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                padding: 15px;
            }}
            .card {{
                background: rgba(255, 255, 255, 0.95);
                backdrop-filter: blur(10px);
                width: 100%;
                max-width: 440px;
                padding: 30px 20px;
                border-radius: 24px;
                box-shadow: 0 20px 40px rgba(0, 0, 0, 0.5);
                text-align: center;
            }}
            .taxi-title-box {{
                background: linear-gradient(135deg, #002d3a, #0a9396);
                color: #ffc107;
                padding: 18px;
                border-radius: 16px;
                margin-bottom: 25px;
                box-shadow: 0 6px 15px rgba(0, 0, 0, 0.15);
            }}
            .taxi-title-box h1 {{
                font-size: 32px;
                font-weight: 900;
                letter-spacing: 2px;
                margin-bottom: 4px;
            }}
            .taxi-title-box p {{
                color: #ffffff;
                font-size: 13px;
                font-weight: 500;
                letter-spacing: 1px;
                margin: 0;
            }}
            h2 {{
                color: #002d3a;
                font-size: 20px;
                margin-bottom: 6px;
            }}
            .subtitle {{
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
            .btn-stop {{
                background: linear-gradient(135deg, #f77f00, #fcbf49);
                color: #fff;
            }}
            .btn-stop:hover {{
                opacity: 0.92;
            }}
            .icon {{
                font-size: 22px;
            }}
            
            @media (max-width: 480px) {{
                .card {{
                    padding: 22px 15px;
                }}
                .taxi-title-box h1 {{
                    font-size: 28px;
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
            <div class="taxi-title-box">
                <h1>🚖 TAXI</h1>
                <p>HỆ THỐNG PHÁT ÂM THANH TRÊN XE</p>
            </div>

            <h2>Xin chào tài xế</h2>
            <div class="subtitle">Chạm vào nút tương ứng khi khách lên hoặc xuống xe</div>

            <div class="button-group">
                <button class="btn-welcome" onclick="playAudio('welcomeAudio')">
                    <span class="icon">🚗</span> Lên Xe (Phát Chào Mừng)
                </button>
                
                <button class="btn-farewell" onclick="playAudio('farewellAudio')">
                    <span class="icon">🏁</span> Xuống Xe (Thông Báo Dừng)
                </button>

                <button class="btn-stop" onclick="stopAllAudio()">
                    <span class="icon">⏸️️</span> Tạm Dừng Âm Thanh
                </button>
            </div>
        </div>

        <audio id="welcomeAudio" src="data:audio/mp3;base64,{audio_len_base64}"></audio>
        <audio id="farewellAudio" src="data:audio/mp3;base64,{audio_xuong_base64}"></audio>

        <script>
            // 1. Chặn click chuột phải
            document.addEventListener('contextmenu', function(e) {{
                e.preventDefault();
                alert("Tính năng này đã bị khóa bảo vệ!");
            }});

            // 2. Chặn các phím tắt copy, xem mã nguồn (Ctrl+C, Ctrl+U, F12, Ctrl+Shift+I...)
            document.addEventListener('keydown', function(e) {{
                if (
                    e.keyCode == 123 || // Phím F12
                    (e.ctrlKey && e.shiftKey && (e.keyCode == 73 || e.keyCode == 74)) || // Ctrl+Shift+I / J (DevTools)
                    (e.ctrlKey && e.keyCode == 85) || // Ctrl+U (Xem mã nguồn)
                    (e.ctrlKey && e.keyCode == 67)    // Ctrl+C (Copy)
                ) {{
                    e.preventDefault();
                    return false;
                }}
            }});

            function playAudio(audioId) {{
                stopAllAudio();
                const audio = document.getElementById(audioId);
                audio.play().catch(error => {{
                    alert("Trình duyệt chặn phát tự động, vui lòng chạm thêm lần nữa!");
                }});
            }}

            function stopAllAudio() {{
                document.querySelectorAll('audio').forEach(audio => {{
                    audio.pause();
                    audio.currentTime = 0;
                }});
            }}
        </script>

    </body>
    </html>
    """

  st.components.v1.html(html_code, height=600)
