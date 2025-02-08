import streamlit as st

def main():
    # Set background image using CSS
    st.markdown("""
        <style>
            .reportview-container {
                background-image: url("IMG_3103.jpeg");
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                height: 100vh;  # Ensure the background covers the entire viewport
            }
            .block-container {
                padding-top: 5rem;
                padding-left: 2rem;
                padding-right: 2rem;
                padding-bottom: 2rem;
            }
            h1, h2, h3, p {
                color: black;  # Text color to make sure it's visible on the image
                font-family: 'Helvetica', sans-serif;
            }
        </style>
    """, unsafe_allow_html=True)
    
    # Title with bigger text
    st.markdown("<h1 style='font-size: 40px;'>💕 Timi, Will You Be My Valentine? 💕</h1>", unsafe_allow_html=True)
    
    # Write text with custom size
    st.markdown("<h2 style='font-size: 30px;'>Hey baby, I just wanted to ask you a quick question...</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='font-size: 25px;'>Will you be my Valentine? 🌚💖</h3>", unsafe_allow_html=True)

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
