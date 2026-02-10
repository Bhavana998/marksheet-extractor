import streamlit as st
import requests
from PIL import Image
import io

# -------- Page Config --------
st.set_page_config(
    page_title="Marksheet Extractor",
    page_icon="📄",
    layout="centered"
)

# -------- Backend URL --------
BACKEND_URL = "https://marksheet-extractor-ludc.onrender.com/docs"

# -------- UI --------
st.title("📄 Marksheet Extractor")
st.subheader("Upload a marksheet image to extract details")

uploaded_file = st.file_uploader(
    "Upload marksheet image",
    type=["png", "jpg", "jpeg"]
)

# -------- Preview --------
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Marksheet", use_container_width=True)

    if st.button("🚀 Extract Details"):
        with st.spinner("Sending image to backend..."):

            # Convert image to bytes
            img_bytes = io.BytesIO()
            image.save(img_bytes, format=image.format)
            img_bytes.seek(0)

            files = {
                "file": (uploaded_file.name, img_bytes, uploaded_file.type)
            }

            response = requests.post(BACKEND_URL, files=files)

        if response.status_code == 200:
            st.success("✅ Extraction completed")
            st.json(response.json()["data"])
        else:
            st.error("❌ Failed to extract marksheet")
            st.write(response.text)
