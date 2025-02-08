import streamlit as st
import time

def main():
    # Title with bigger text
    st.markdown("<h1 style='font-size: 40px;'>💕 Timi, Will You Be My Valentine? 💕</h1>", unsafe_allow_html=True)
    
    # Image with larger size
    st.image("IMG_3103.jpeg", use_container_width=True)
    
    # Write text with custom size
    st.markdown("<h2 style='font-size: 30px;'>Hey baby, I just wanted to ask you a quick question...</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='font-size: 25px;'>Will you be my Valentine? 🌚💖</h3>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    # Customize buttons with bigger size using custom HTML
    with col1:
        if st.button("Yes! 💘", key="yes_button"):
            st.balloons()
            st.success("Yay! I knew you'd say yes! 😍")
    
    with col2:
        if st.button("No...😡", key="no_button"):
            st.write("Wrong answer..let's try this again uhn 🫠")
            time.sleep(2)
            st.experimental_rerun()

if __name__ == "__main__":
    main()
