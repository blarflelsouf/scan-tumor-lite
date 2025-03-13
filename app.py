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

# # A little text to explain the product
# HOW_IT_WORKS_HTML = '<p>We provide a trained IA to help brain tumor detections.\
#     Please submit a brain scanner image to get the IA diagnostic.</h2>'
# st.markdown(HOW_IT_WORKS_HTML, unsafe_allow_html=True)


img_allowed_extensions = ["jpg", "jpeg", "png"]
tmp_mock =0

brain_image = st.file_uploader(label="We provide a trained IA to help brain tumor detections.\
                                Please submit a brain scanner image to get the IA diagnostic.",
                type=img_allowed_extensions,
                accept_multiple_files=False,
                key='brain_img_to_predict',
                help=None, #tooltip à creuser
                on_change=None, #callback à creuser
                disabled=False,
                label_visibility="visible")
if brain_image is not None:
    st.image(brain_image)
    if st.button("Launch diagnostic"):
        tmp_mock +=1
        if tmp.mock

brain_image=st.image("data/brain-logo.png")
st.write(type(brain_image))

# st.title("Off center :(")
# col1, col2, col3 = st.beta_columns([1,1,1])
# col2.title("Centered! :)")
# col2.image(img, use_column_width=True)
