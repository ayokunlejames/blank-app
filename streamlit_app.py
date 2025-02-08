import streamlit as st
from PIL import Image

# Load your logo
our_cute_pic = Image.open('IMG_3103.jpeg')

def main():
    st.image(our_cute_pic, use_container_width=5)

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
