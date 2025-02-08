import streamlit as st
import time

def main():
    # Set background image using CSS
    st.markdown("""
        <style>
            .reportview-container {
                background-image: url("IMG_3103.jpeg");
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                height: 100vh;
            }
            .block-container {
                padding-top: 5rem;
                padding-left: 2rem;
                padding-right: 2rem;
                padding-bottom: 2rem;
            }
            h1, h2, h3, p {
                color: white;
                font-family: 'Helvetica', sans-serif;
            }
        </style>
    """, unsafe_allow_html=True)
    
    # Title with bigger text
    st.markdown("<h1 style='font-size: 40px;'>💕 Timi, Will You Be My Valentine? 💕</h1>", unsafe_allow_html=True)
    
    # Write text with custom size
    st.markdown("<h2 style='font-size: 30px;'>Hey baby, I just wanted to ask you a quick question...</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='font-size: 25px;'>Will you be my Valentine? 🌚💖</h3>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    # Manage the state of the rerun
    if 'rerun_triggered' not in st.session_state:
        st.session_state.rerun_triggered = False

    with col1:
        if st.button("Yes! 💘"):
            st.balloons()
            st.success("Yay! I knew you'd say yes! 😍")
    
    with col2:
        if st.button("No...😡"):
            st.write("Wrong answer..let's try this again uhn 🫠")
            time.sleep(2)
            # Mark the state before rerun
            st.session_state.rerun_triggered = True
            # Rerun the app
            st.experimental_rerun()

    if st.session_state.rerun_triggered:
        st.session_state.rerun_triggered = False  # Reset after rerun

if __name__ == "__main__":
    main()
