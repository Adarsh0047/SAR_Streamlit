import streamlit as st
from PIL import Image
from streamlit_image_select import image_select
from predict import predict

st.title("SAR Demo")
selected = False
with st.sidebar:
    st.markdown("Upload Image")
    img = st.file_uploader("Upload Image", type=["png", "jpg"])
    image_gallery = st.empty()
    with image_gallery.container():
        img_gall = image_select(label="Examples", images=["hrsid1.jpeg", "hrsid2.jpeg", "hrsid3.jpeg", "ssdd1.jpeg", "ssdd2.jpeg"])


if img is not None:
    selected = True
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("## Original")
        st.image(Image.open(img))
    
    with col2:
        pred_path = predict(img.name)
        if pred_path is not None:
            st.markdown("## Predicted")
            st.image(Image.open(pred_path))
else:
    selected = False
    img = None
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("## Original")
        st.image(Image.open(img_gall))
    
    with col2:
        pred_path = predict(img_gall)
        if pred_path is not None:
            st.markdown("## Predicted")
            st.image(Image.open(pred_path))

