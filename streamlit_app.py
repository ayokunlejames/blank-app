import streamlit as st
import time

def main():
    st.markdown(
        f"""
        <style>
            .stApp {{
                background: url('IMG_3103.jpeg') no-repeat center center fixed;
                background-size: cover;
            }}
            .stApp::before {{
                content: """";
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: rgba(0, 0, 0, 0.3); /* Adjust transparency here */
                z-index: -1;
            }}
            h1 {{
                text-align: center;
                font-size: 50px;
                color: white;
            }}
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("""<h1>💕 Timi, Will You Be My Valentine? 💕</h1>""", unsafe_allow_html=True)
    
    st.write("Hey baby, I just wanted to ask you a quick question...")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Yes! 💘"):
            st.balloons()
            st.success("Yay! I knew you'd say yes! 😍")
    
    with col2:
        if st.button("No... 😡"):
            st.write("Wrong answer..let's try this again uhn 🫠")
            time.sleep(2)
            st.experimental_rerun()

if __name__ == "__main__":
    main()
