import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to SARInspector! 👋")

st.write("## Problem Statement")
st.write("To propose a sandwich model to detect small objects within SAR images by performing comprehensive research analysis, observing the intuition and the shortfalls of the existing methods to optimize the performance through the Feature Refinement Module.")

st.write("## Solution")
st.markdown("After extensive research and study, we determined that `tood_r50_fpn_1x_SSDD` to perform the best. This application leverages the model for small image detection.")

st.write("## Application Architecture")
st.image(Image.open("sar_dark.jpeg"))

st.sidebar.success("Select a demo above.")