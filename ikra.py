import streamlit as st
import time

st.set_page_config(page_title="İyi ki Doğdun!", page_icon="🎂", layout="centered")

# CSS ile arka plan ve tipografi düzenlemesi
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .title {
        font-size: 40px;
        text-align: center;
        font-weight: bold;
        color: #ff4b4b;
        margin-bottom: 20px;
    }
    .msg-box {
        background-color: #262730;
        padding: 25px;
        border-radius: 15px;
        border-left: 5px solid #ff4b4b;
        font-size: 18px;
        line-height: 1.6;
        color: #f0f2f6;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>🎂 İyi ki Doğdun! 🎉</div>", unsafe_allow_html=True)

# İnteraktif kutlama akışı
if "step" not in st.session_state:
    st.session_state.step = 1

if st.session_state.step == 1:
    st.write("### Sana özel küçük bir sürpriz hazırlandı...")
    if st.button("🎁 Hediyeni Aç"):
        st.session_state.step = 2
        st.rerun()

elif st.session_state.step == 2:
    st.balloons()  # Ekranda uçuşan balonlar
    
    st.markdown("""
    <div class='msg-box'>
        <b>Sevgili Arkadaşım,</b><br><br>
        Yeni yaşında tüm güzelliklerin, mutluluğun ve hedeflerinin gerçeğe dönüşmesini dilerim. 
        Birlikte güldüğümüz, dertleştiğimiz ve güzel anılar biriktirdiğimiz nice harika yaşların olsun!<br><br>
        <i>— İyi ki varsın!</i>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    if st.button("✨ Pastayı Üfle"):
        st.session_state.step = 3
        st.rerun()

elif st.session_state.step == 3:
    st.snow()  # Konfeti/kar efekti
    st.success("Dileğin kabul olsun! 🕯️✨")
    st.write("### 🍰 Yeni yaşın sana neşe, başarı ve huzur getirsin!")
    