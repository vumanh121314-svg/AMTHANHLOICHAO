import base64
import streamlit as st

st.set_page_config(
    page_title="Phát Âm Thanh Lên/Xuống Xe", page_icon="🚗", layout="centered"
)

st.title("🚗 Hệ Thống Phát Âm Thanh Trên Xe")
st.write(
    "Nhấn vào nút tương ứng để phát file âm thanh chào mừng hoặc thông báo xuống xe."
)


# Hàm chuyển đổi file âm thanh sang Base64 để nhúng vào HTML (giúp chạy mượt trên web)
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
      " tên file trong thư mục!"
  )
else:
  # Giao diện HTML kết hợp JavaScript để phát âm thanh khi bấm nút
  html_code = f"""
    <!DOCTYPE html>
    <html lang="vi">
    <head>
        <meta charset="UTF-8">
        <style>
            .container {{
                display: flex;
                flex-direction: column;
                gap: 20px;
                margin-top: 20px;
            }}
            button {{
                width: 100%;
                padding: 18px 20px;
                font-size: 20px;
                font-weight: bold;
                color: white;
                border: none;
                border-radius: 10px;
                cursor: pointer;
                transition: 0.2s;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            }}
            button:active {{
                transform: scale(0.98);
            }}
            .btn-welcome {{
                background-color: #28a745;
            }}
            .btn-welcome:hover {{
                background-color: #218838;
            }}
            .btn-farewell {{
                background-color: #007bff;
            }}
            .btn-farewell:hover {{
                background-color: #0056b3;
            }}
        </style>
    </head>
    <body>

        <div class="container">
            <!-- Nút Lên Xe -->
            <button class="btn-welcome" onclick="playAudio('welcomeAudio')">🚗 Lên Xe (Phát Âm Thanh)</button>
            
            <!-- Nút Xuống Xe -->
            <button class="btn-farewell" onclick="playAudio('farewellAudio')">🚏 Xuống Xe (Phát Âm Thanh)</button>
        </div>

        <!-- Thẻ Audio ẩn chứa dữ liệu gốc -->
        <audio id="welcomeAudio" src="data:audio/mp3;base64,{audio_len_base64}"></audio>
        <audio id="farewellAudio" src="data:audio/mp3;base64,{audio_xuong_base64}"></audio>

        <script>
            function playAudio(audioId) {{
                // Dừng tất cả các âm thanh đang phát (nếu có)
                document.querySelectorAll('audio').forEach(audio => {{
                    audio.pause();
                    audio.currentTime = 0;
                }});
                
                // Phát âm thanh của nút được chọn
                const audio = document.getElementById(audioId);
                audio.play().catch(error => {{
                    alert("Trình duyệt chặn phát tự động, vui lòng bấm lại lần nữa!");
                }});
            }}
        </script>

    </body>
    </html>
    """

  # Hiển thị giao diện lên Streamlit
  st.components.v1.html(html_code, height=220)
