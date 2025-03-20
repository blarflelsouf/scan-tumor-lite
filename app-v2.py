import streamlit as st
import requests
import time
import base64
from PIL import Image
from io import BytesIO

# Custom styles for background
st.markdown(
    """
    <style>
        body {
            background-color: #E3F2FD;
        }
        .stButton>button {
            width: 100%;
            padding: 10px;
            font-size: 16px;
        }
        div[data-testid="stFileUploader"] > div:first-child {
            visibility: hidden;
            height: 0px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# Session state initialization
for key in ['import_image_btn', 'image_uploaded', 'diagnostic', 'loading','image_pred_yolo']:
    if key not in st.session_state:
        st.session_state[key] = False

# Configurations
img_allowed_extensions = ["jpg", "jpeg", "png"]
scan_tumor_api_url = "https://scantumor-939517190032.europe-west1.run.app/predict-yolo"
#scan_tumor_api_url = "http://localhost:8000/predict-yolo"


# UI Elements
st.image("images/background_banner.png")
st.markdown("<h1 style='text-align: center;'>SCAN TUMOR</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Smart Scans, Clear Results</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Upload a brain scan to get an AI-powered diagnostic.</p>", unsafe_allow_html=True)

diag_area = st.container()

with diag_area:
    colA_1, colA_2, colA_3 = st.columns(3)
    with colA_2:
        import_image_btn = st.button("Import Brain Scan", type="primary")

    if import_image_btn or st.session_state['import_image_btn']:
        st.session_state['import_image_btn'] = True
        st.session_state['image_pred_yolo']  = False
        st.markdown('''
        <style>
            .stFileUploaderFile {display: none}
        <style>''',
        unsafe_allow_html=True)
        image_uploaded = st.file_uploader(
            "Upload a brain scan image:",
            type=img_allowed_extensions,
            key='brain_img_to_predict',
            label_visibility="collapsed"  # Hide file name
        )

        if image_uploaded or st.session_state['image_uploaded']:
            st.session_state['image_uploaded'] = True
            colB_1, colB_2 = st.columns(2)
            with colB_1:
                image_container = st.empty()
                if st.session_state['image_pred_yolo']:
                    image_container.image(img_pred_yolo)
                else:
                    image_container.image(image_uploaded)
            with colB_2:
                colC_1, colC_2, colC_3 = st.columns([0.25, 0.5, 0.25])
                with colC_2:

                    launch_diag = st.button("Launch Diagnostic")

                if launch_diag:
                    st.session_state['loading'] = True
                    with st.spinner("Processing... Please wait."):
                        time.sleep(2)  # Simulated delay
                        files = {"file": image_uploaded.getvalue()}
                        response = requests.post(scan_tumor_api_url, files=files, timeout=30)
                    st.session_state['loading'] = False

                    if response.status_code == 200:
                        result = response.json()
                        recall_percentage = round(result['recall'] * 100, 2)
                        precision_percentage = round(result['precision'] * 100, 2)

                        st.markdown("---")

                        if result["tumor"]:
                            st.error(f"⚠️ A tumor **{result['tumor_type'].capitalize()}** has been detected")
                            st.markdown(f"*Tumor Recall: {recall_percentage}% (0% no tumor, 100% tumor)*")
                            st.markdown(f"*{result['tumor_type'].capitalize()} Precision: {precision_percentage}%*")
                        else:
                            st.success("✅ No tumor has been detected!")
                            st.markdown(f"*Tumor Recall: {recall_percentage}% (0% no tumor, 100% tumor)*")
                            st.balloons()  # Balloon animation when no tumor detected

                        if "img_pred_yolo" in result:
                            img_64_pred_yolo = result["img_pred_yolo"]
                            img_array_pred_yolo = base64.b64decode(img_64_pred_yolo)
                            img_pred_yolo = Image.open(BytesIO(img_array_pred_yolo))
                            image_container.image(img_pred_yolo)
                            st.session_state['image_pred_yolo'] = True
                    else:
                        st.error(f"Error during diagnostic: {response.text}")
        else:
            colD_1, colD_2, colD_3 = st.columns(3)
            with colD_2:
                st.button("Launch Diagnostic", disabled=True, type="primary")

# Footer Credit
st.markdown("""
    <hr>
    <p style='text-align: center;'>Developed by Scan Tumor Group - version 2.0</p>
    <p style='text-align: center; font-size: 12px; font-style: italic;'>This software is an AI-based tool designed to assist in the detection of brain tumors. \
        It does not constitute a medical diagnosis and does not replace the evaluation of a qualified healthcare professional. \
        The software publisher disclaims any liability for errors, omissions, or technical malfunctions. \
        The user is solely responsible for interpreting the results and making clinical decisions based on them. </p>

""", unsafe_allow_html=True)
