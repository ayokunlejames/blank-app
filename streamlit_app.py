import streamlit as st
from PIL import Image
import io
import base64

def main():
    # Load and encode the image in base64 (for local images)
    image_path = "IMG_3103.jpeg"  # Ensure this is the correct path to your image
    try:
        image = Image.open(image_path)
    except FileNotFoundError:
        st.error("Image file not found. Please check the file path.")
        return

    # Convert image to base64
    img_bytes = io.BytesIO()
    image.save(img_bytes, format="JPEG")
    img_base64 = base64.b64encode(img_bytes.getvalue()).decode("utf-8")

    # Set background image using CSS with base64 encoded image
    st.markdown(f"""
        <style>
            .reportview-container {{
                background-color: white;
                background-image: url("data:image/jpeg;base64,{img_base64}");
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                background-attachment: fixed;  # Keeps the image fixed during scrolling
                height: 100vh;  # Ensure the background covers the entire viewport
            }}
            .block-container {{
                padding-top: 5rem;
                padding-left: 2rem;
                padding-right: 2rem;
                padding-bottom: 2rem;
            }}
            h1, h2, h3, p {{
                color: black;  # Text color to make sure it's visible on the image
                font-family: 'Helvetica', sans-serif;
            }}
        </style>
    """, unsafe_allow_html=True)


    
    # Title with bigger text
   # st.markdown("<h1 style='font-size: 40px;'>💕 Timi, Will You Be My Valentine? 💕</h1>", unsafe_allow_html=True)
    
    # Write text with custom size
    st.markdown("<h2 style='font-size: 30px;'>Timi baby, I just wanted to ask you a quick question...</h2>", unsafe_allow_html=True)
    st.write("Will you be my Valentine? 🌚💖")

    # Display buttons and handle logic as before
    col1, col2 = st.columns(2)
    
    if 'response' not in st.session_state:
        st.session_state.response = None

    with col1:
        if st.button("Yes! 💘"):
            st.session_state.response = "Yes"
            st.balloons()
            st.success("Yay! I knew you'd say yes! 😍")
    
    with col2:
        if st.button("No...😡"):
            st.session_state.response = "No"
            st.write("Wrong answer..let's try this again uhn 🫠")


if __name__ == "__main__":
    main()
