import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

# Konfigurasi halaman
st.set_page_config(page_title="Klasifikasi Penyakit Udang Vannamei", layout="wide")

# Load model
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model("Model.keras")
    return model

model = load_model()
class_names = ['ehp', 'imnv', 'sehat']

# Warna dan CSS
PRIMARY_COLOR = "#0077B6"
BLACK = "#000000"
LIGHT_BLUE = "rgba(192, 237, 252, 0.5)"
SIDEBAR_COLOR = "rgba(124, 155, 198, 0.5)"
ELIPS_COLOR_60 = "rgba(41, 172, 253, 0.6)"
ELIPS_COLOR_100 = "#29ACFD"

# Dekorasi CSS
st.markdown(f"""
    <style>
        .elips-container {{
            position: absolute;
            top: -133px;
            right: -117px;
            width: 270px;
            height: 270px;
            background-color: {ELIPS_COLOR_60};
            border-radius: 123%;
        }}
        

        .elips-small {{
            position: absolute;
            top: 46px;
            right: -107px;
            width: 170px;
            height: 170px;
            background-color: {ELIPS_COLOR_100};
            border-radius: 50%;
        }}
        .css-1d391kg {{
            background-color: {SIDEBAR_COLOR};
        }}
        .upload-header {{
            color: {PRIMARY_COLOR};
            font-size: 20px;
            font-weight: bold;
            margin-bottom: 20px;
            text-align: center;
        }}
        .upload-area {{
            border: 2px dashed {PRIMARY_COLOR};
            border-radius: 10px;
            padding: 20px;
            background-color: {LIGHT_BLUE};
            text-align: center;
        }}
        .upload-icon {{
            font-size: 40px;
            color: {PRIMARY_COLOR};
        }}
        .stFileUploader input[type="file"] {{ display: none; }}
        .stFileUploader button {{
            display: block;
            padding: 5px 15px;
            font-size: 16px;
            font-weight: 500;
            text-align: center;
            color: black !important;
            background-color: white;
            border: 1px solid grey !important;
            border-radius: 10px;
            transition: all 0.3s ease;
        }}
        .stFileUploader button:hover {{
            background-color: white !important;
            color: {PRIMARY_COLOR} !important;
            border: 1px solid #018FE8 !important;
        }}
        .stFileUploader button:active {{
            background-color: {PRIMARY_COLOR} !important;
            color: white !important;
            border: 1px solid #015BB5 !important;
        }}
        .stButton > button {{
            display: block;
            margin: 0 auto;
            background-color: white !important;
            color: black !important;
            font-size: 16px;
            font-weight: bold;
            padding: 5px 15px;
            border-radius: 10px;
            border: 1px solid grey !important;
            transition: all 0.3s ease !important;
        }}
        .stButton > button:hover {{
            background-color: white !important;
            color: {PRIMARY_COLOR} !important;
            border: 1px solid #018FE8 !important;
        }}
        .stButton > button:active {{
            background-color: {PRIMARY_COLOR} !important;
            color: white !important;
            border: 1px solid #015BB5 !important;
        }}
        .alert-box {{
            color: #ff4b4b;
            background-color: #fff4f4;
            border: 1px solid #ff4b4b;
            border-radius: 10px;
            padding: 15px;
            text-align: center;
            font-size: 14px;
            max-width: 280px;
            margin: 0 auto;
        }}

        /* --- RESPONSIVE STYLES --- */
        @media (max-width: 768px) {{
            .elips-container {{
                top: -100px;
                right: -90px;
                width: 180px;
                height: 180px;
            }}
            .elips-small {{
                top: 30px;
                right: -80px;
                width: 120px;
                height: 120px;
            }}
            .upload-header {{
                font-size: 18px;
            }}
            .upload-area {{
                padding: 15px;
            }}
            .upload-icon {{
                font-size: 30px;
            }}
            .stFileUploader button,
            .stButton > button {{
                font-size: 14px;
                padding: 5px 10px;
            }}
            .alert-box {{
                font-size: 13px;
                padding: 10px;
                max-width: 90%;
            }}
        }}
    </style>
    <div class="elips-container"></div>
    <div class="elips-small"></div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown(f"""
        <style>
            .sidebar-title {{ margin-top: -30px; }}
            .sidebar-spacing {{ margin-top: 20px; }}
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 class="sidebar-title" style="color:#2196F3;">Tentang Kami</h1>', unsafe_allow_html=True)
    st.write("Shrimpcare hadir untuk membantu Anda mengidentifikasi penyakit udang vannamei dengan cepat, mudah, dan akurat. Dengan dukungan teknologi AI, Anda dapat menganalisis kondisi udang secara instan hanya melalui unggah foto udang dari ponsel atau komputer! 🌊🦐")
    st.markdown("<p style='font-size:16px; font-weight:bold; color:#4DA8DA; margin-top:10px;'>🌱 Cepat diagnosis, selamatkan tambak Anda!</p>", unsafe_allow_html=True)
    st.markdown('<h1 class="sidebar-spacing" style="color:#2196F3;">Tips Pengambilan Gambar!</h1>', unsafe_allow_html=True)
    st.markdown("""
        1. **Jarak Kamera**: Ambil gambar minimal **25 cm** dari kamera, agar detail udang terlihat.
        2. **Pencahayaan**: Pastikan pencahayaan cukup dan hindari bayangan.
        3. **Latar Belakang**: Gunakan latar belakang bersih dan kontras.
    """)

# Logo di tengah
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("Shrimp (2).png", width=250)

# Judul dan deskripsi tetap rata kiri
st.markdown(f"<h2 style='text-align:left; color:{PRIMARY_COLOR};'>Klasifikasi Penyakit Udang Vannamei</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:left;'>Jaga kesehatan tambak Anda dengan diagnosis dini dan pengelolaan yang tepat!</p>", unsafe_allow_html=True)

# Upload area
st.subheader("📤 Unggah Gambar Udang")
uploaded_file = st.file_uploader("Pilih gambar udang Anda🦐!", type=["jpg", "png", "jpeg"])
if uploaded_file:
    st.image(Image.open(uploaded_file), caption="Gambar yang diunggah", use_container_width=True)

if st.session_state.get('button_clicked') and not uploaded_file:
    st.session_state['button_clicked'] = False

if 'button_clicked' not in st.session_state:
    st.session_state['button_clicked'] = False

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("Analisis Gambar"):
        if uploaded_file:
            st.session_state['button_clicked'] = True
        else:
            st.warning("Harap unggah gambar terlebih dahulu.")

if st.session_state['button_clicked']:
    st.write("🔎 Sedang menganalisis gambar, mohon tunggu sebentar...")

    image = Image.open(uploaded_file).convert("RGB")
    img_resized = image.resize((224, 224))
    img_array = np.array(img_resized) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    with st.spinner("🔬 Shrimpcare sedang memproses gambar..."):
        prediction = model.predict(img_array)
        pred_index = np.argmax(prediction)
        predicted_class = class_names[pred_index]
    
    if predicted_class == 'sehat':
        st.success(f"✅ Udang dalam kondisi **{predicted_class.upper()}**")
    else:
        st.error(f"⚠️ Udang terdeteksi terkena penyakit **{predicted_class.upper()}**")