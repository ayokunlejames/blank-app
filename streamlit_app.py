import streamlit as st
import time

def main():
    st.title("💕 Timi, Will You Be My Valentine? 💕")
    
    st.image("IMG_3103.jpeg", use_container_width=True)
    
    st.write("Hey love, I just wanted to ask you something really special...")
    st.write("Will you be my Valentine? 💖")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Yes! 💘"):
            st.balloons()
            st.success("Yay! I knew you'd say yes! 😍")
    
    with col2:
        if st.button("No..."):
            st.write("Wrong answer..let's try this again!")
            time.sleep(2)
            st.experimental_rerun()

if __name__ == "__main__":
    main()
