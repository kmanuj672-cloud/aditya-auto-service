import streamlit as st
import os

# Page configuration (Mobile View Design)
st.set_page_config(page_title="Aditya Auto Service", page_icon="🛠️", layout="centered")

# Custom CSS for Clean Premium Look
st.markdown("""
    <style>
    .main { background-color: #111111; color: white; }
    .stButton>button { width: 100%; border-radius: 12px; font-weight: bold; height: 45px; }
    .watermark { text-align: center; color: #888888; font-size: 13px; margin-top: 50px; font-weight: bold; border-top: 1px solid #333; padding-top: 15px; }
    .shop-title { text-align: center; color: #FF9900; font-size: 28px; font-weight: bold; margin-bottom: 0px; }
    .shop-address { text-align: center; color: #BBBBBB; font-size: 14px; margin-top: 5px; margin-bottom: 20px; }
    </style>
""", unsafe_allow_html=True)

# 1. TOP SHOP PHOTO (Aapki asli dukan ki photo load hogi)
photo_loaded = False
for ext in [".jpg", ".jpeg", ".png", ".JPG", ".JPEG"]:
    if os.path.exists(f"dukan{ext}"):
        st.image(f"dukan{ext}", caption="आदित्य ऑटो सर्विस - बिजनौर", use_container_width=True)
        photo_loaded = True
        break

if not photo_loaded:
    st.warning("⚠️ Dukan ki photo 'dukan' naam se GitHub par nahi mili! Kripya photo upload karein.")

# 2. SHOP NAME & ADDRESS
st.markdown("<div class='shop-title'>आदित्य ऑटो सर्विस</div>", unsafe_allow_html=True)
st.markdown("<div class='shop-address'>📍 मुरादाबाद रोड, सुल्तानपुर, निकट-लक्ष्य कॉलेज (बिजनौर)</div>", unsafe_allow_html=True)

# 3. OWNER & MECHANIC INFO CARD
with st.container(border=True):
    st.markdown("### 👤 प्रो०: Aditya Kumar")
    st.markdown("🔧 **मिस्त्री:** Nitish Kumar")
    st.markdown("📞 **मोबाइल:** 9027033257")
    
    # Direct Call Button
    st.link_button("📞 CALL MECHANIC NOW", "tel:+919027033257")

# 4. EMERGENCY & LOCATION BUTTONS
st.markdown("### 🗺️ Emergency Roadside Help")
col1, col2 = st.columns(2)
with col1:
    st.link_button("📍 Shop Google Map", "https://maps.app.goo.gl/jWfmm4VcqCZSaH3R9")
with col2:
    whatsapp_msg = "https://wa.me/919027033257?text=Bhai%20meri%20bike%20rasta%20me%20kharab%20ho%20gayi%20hai.%20Ye%20meri%20location%20hai,%20jaldi%20aao!"
    st.link_button("📲 Share My Location", whatsapp_msg)

# 5. SPARE PARTS HINDI PRICE LIST
st.markdown("---")
st.markdown("### ⚡ पार्ट्स और सर्विस रेट लिस्ट (Price List)")

parts = [
    {"name": "स्पार्क प्लग (Spark Plug)", "price": "₹80"},
    {"name": "पंचर सुधार (Tyre Puncture)", "price": "₹50"},
    {"name": "इंजन ऑयल (Engine Oil)", "price": "₹350 / ₹400 / ₹450"},
    {"name": "क्लच वायर (Clutch Wire)", "price": "₹80"},
    {"name": "इमरजेंसी पेट्रोल (Petrol 250ml)", "price": "₹30"},
    {"name": "बाइक सर्विस चार्ज (Service Charge)", "price": "₹150"}
]

# Grid Layout for Parts
p_col1, p_col2 = st.columns(2)
for i, part in enumerate(parts):
    current_col = p_col1 if i % 2 == 0 else p_col2
    with current_col:
        with st.container(border=True):
            st.markdown(f"**{part['name']}**")
            st.markdown(f"<h4 style='color: #00FF00; margin:0px;'>{part['price']}</h4>", unsafe_allow_html=True)

# Watermark
st.markdown("<div class='watermark'>🛠️ Developed by Manuj Kumar</div>", unsafe_allow_html=True)