import streamlit as st
from PIL import Image
from app.extractor import extract_marksheet_logic  # your function

st.set_page_config(page_title="Marksheet Extractor", layout="centered")

st.title("📄 Marksheet Extractor")
st.write("Upload a marksheet image to extract details")

uploaded_file = st.file_uploader(
    "Upload marksheet image",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Marksheet", use_column_width=True)

    if st.button("Extract"):
        with st.spinner("Extracting data..."):
            result = extract_marksheet_logic(image)
        st.success("Extraction complete")
        st.json(result)