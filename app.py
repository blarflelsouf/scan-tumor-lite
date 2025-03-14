import streamlit as st

import requests

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

# Initialization of a session_state as streamlit resets the whole page every time user interacts with it
if 'import_image_btn' not in st.session_state:
    st.session_state['import_image_btn'] = False

if 'image_uploaded' not in st.session_state:
    st.session_state['image_uploaded'] = False

if 'tmp_mock_count' not in st.session_state: #Mock to display a result until API call is ready
    st.session_state['tmp_mock_count'] = 0

if 'diagnostic' not in st.session_state:
    st.session_state['diagnostic'] = False

img_allowed_extensions = ["jpg", "jpeg", "png"]

import_image_btn = st.button("Import brains scan",type="primary")
if import_image_btn or st.session_state['import_image_btn']:
    st.session_state['import_image_btn'] = True
    image_uploaded = st.file_uploader(label="In order to provide a diagnostic, our trained IA needs a scanner image of the brain.",
                    type=img_allowed_extensions,
                    accept_multiple_files=False,
                    key='brain_img_to_predict',
                    help=None, #tooltip à creuser
                    on_change=None, #callback à creuser
                    disabled=False,
                    label_visibility="visible")
    if image_uploaded is not None or st.session_state['image_uploaded']:
        st.session_state['image_uploaded'] = True
        st.image(image_uploaded,caption="Brain scan uploaded with success")
        #st.markdown("Image downloaded with success")
        launch_diag = st.button("Launch diagnostic")
        if launch_diag:
            st.session_state['tmp_mock_count'] +=1
            if st.session_state['tmp_mock_count'] // 2 == 0:
                st.markdown("No tumor detected")
            else:
                st.markdown("A tumor has been detected")
    else:
        launch_diag_disabled = st.button("Launch diagnostic",disabled=True,type="primary")


# st.title("Off center :(")
# col1, col2, col3 = st.beta_columns([1,1,1])
# col2.title("Centered! :)")
# col2.image(img, use_column_width=True)
