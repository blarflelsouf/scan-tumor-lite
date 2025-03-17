import streamlit as st

import requests

# Initialization of a session_state as streamlit resets the whole page every time user interacts with it
if 'import_image_btn' not in st.session_state:
    st.session_state['import_image_btn'] = False

if 'image_uploaded' not in st.session_state:
    st.session_state['image_uploaded'] = False

if 'tmp_mock_count' not in st.session_state: #Mock to display a result until API call is ready
    st.session_state['tmp_mock_count'] = 0

if 'diagnostic' not in st.session_state:
    st.session_state['diagnostic'] = False

# Initialization of variables
img_allowed_extensions = ["jpg", "jpeg", "png"]
scan_tumor_api_url = "http://localhost:8000/predict"

# Some nice banner
st.image("data/background_banner.png")

# Nice product title
TITLE_HTML = '<h1>ML & DL BRAIN TUMOR</h1>'
st.markdown(TITLE_HTML, unsafe_allow_html=True)

# Catchy sub-title
SUBTITLE_HTML = '<h3>Smart Scans, Clear Results</h3>'
st.markdown(SUBTITLE_HTML, unsafe_allow_html=True)

# A little text to explain the product
HOW_IT_WORKS_HTML = '<p>We provide a trained IA to help brain tumor detections.\
    Please submit a brain scanner image to get the IA diagnostic.</h2>'
st.markdown(HOW_IT_WORKS_HTML, unsafe_allow_html=True)

diag_area = st.container()

with diag_area:
    # Display a centered button with a 3 columns trick
    colA_1, colA_2, colA_3 = st.columns(3)
    with colA_2:
        # Scan image upload & diagnostic request
        import_image_btn = st.button("Import brains scan",type="primary")
    if import_image_btn or st.session_state['import_image_btn']:
        st.session_state['import_image_btn'] = True

        # User can upload image from its directory
        image_uploaded = st.file_uploader(label="In order to provide a diagnostic, our trained IA needs a scanner image of the brain.",
                        type=img_allowed_extensions,
                        accept_multiple_files=False,
                        key='brain_img_to_predict',
                        help=None, #tooltip à creuser
                        on_change=None, #callback à creuser
                        disabled=False,
                        label_visibility="visible")

        # Scan image is displayed to user
        if image_uploaded is not None or st.session_state['image_uploaded']:
            st.session_state['image_uploaded'] = True
            colB_1, colB_2 = st.columns(2, border = True, vertical_alignment = "top")
            with colB_1:
                img = st.image(image_uploaded,caption=None)

            with colB_2:
                # User can launch a diagnostic once image is uploaded
                colC_1, colC_2, colC_3 = st.columns([0.25,0.5,0.25])
                with colC_2:
                    launch_diag = st.button("Launch diagnostic")
                if launch_diag:
                    files = {"file": image_uploaded.getvalue()} #To read image as a Byte file
                    response = requests.post(scan_tumor_api_url,files= files) # nota : we could push many images :)
                    if response.status_code == 200:
                        result = response.json()
                        if result["tumor"]:
                            st.error(f"⚠️A tumor **{result['tumor_type']}** has been detected")
                            st.markdown(f"*Tumor recall: {result['recall']}*")
                            st.markdown(f"*{result['tumor_type']} precision: {result['precision']}*")
                        else:
                            st.success(f"✅No tumor has been detected")
                            st.markdown(f"$*Tumor recall: {result['recall']}*")
                    else:
                        st.error(f"An error occurred during the diagnostic: {response.text}")
        else:
            # Display disabled diagnostic button while image is not uploaded
            colD_1, colD_2, colD_3 = st.columns(3)
            with colD_2:
                launch_diag_disabled = st.button("Launch diagnostic",disabled=True,type="primary")
