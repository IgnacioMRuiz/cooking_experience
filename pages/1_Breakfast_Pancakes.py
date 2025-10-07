import streamlit as st
import time
from pathlib import Path
import random, string

# --- PAGE CONFIG ---
st.set_page_config(page_title="Pancake Breakfast — Cooking Studio", page_icon="🥞", layout="centered")

# --- HIDE SIDEBAR ---
st.markdown(
    """
    <style>
        [data-testid="stSidebar"] {display: none;}
        [data-testid="stAppViewContainer"] {margin-left: 0;}
    </style>
    """,
    unsafe_allow_html=True
)

# --- HEADER ---
st.title("🥞 Pancake Breakfast — Saturday, 9:00–10:30 AM")
st.markdown(
    """
    Join us for our most popular live online class: **Fluffy Pancakes with Fresh Berries**.  
    This isn’t just about breakfast — it’s about slowing down, sharing a quiet moment, and creating something simple and beautiful together.  
    You’ll learn the art of the perfect batter, the gentle rhythm of flipping each pancake, and how to build your own mix of toppings, from golden syrup to fresh fruit.  
    Every step is designed to feel natural and connected — two kitchens following the same scent, two people laughing over the same recipe, even if miles apart.  
    Perfect for couples, friends, or anyone who believes that love and food taste better when shared.
    """
)

# --- IMAGE ---
image_path = Path(__file__).parent.parent / "pancakes.jpg"
if image_path.exists():
    st.image(str(image_path), use_container_width=True)
else:
    st.warning("Image not found. Make sure 'pancakes.jpg' is in the main folder.")

st.markdown("---")

# --- FORM SECTION ---
st.subheader("Reserve your spot")

# Step 1: user data outside form for interactivity
name = st.text_input("Your name")
accompanied = st.radio("Will you be accompanied?", ["No", "Yes"])

companion = ""
if accompanied == "Yes":
    companion = st.text_input("Companion's name")

# Step 2: form only for confirmation
with st.form("booking_form"):
    slot = st.selectbox("Select your time slot", ["09:00", "09:30", "10:00", "10:30"])
    confirm = st.form_submit_button("Confirm booking")

# --- AFTER SUBMIT ---
if confirm:
    with st.spinner("Processing your booking..."):
        time.sleep(1.5)

    booking_id = "".join(random.choices(string.ascii_uppercase + string.digits, k=6))
    st.success(f"✅ Slot booked successfully for {name or 'you'} at {slot}.")
    st.write(f"Your Booking ID: **{booking_id}**")

    if accompanied == "Yes" and companion:
        st.info(f"Reservation for two confirmed: {name} and {companion}.")

    st.markdown("---")
    st.markdown("### Download your ticket")

    try:
        with open(Path(__file__).parent.parent / "invitation.pdf", "rb") as f:
            st.download_button(
                label="🎟️ Get your ticket",
                data=f,
                file_name=f"Ticket_{booking_id}.pdf",
                mime="application/pdf"
            )
    except FileNotFoundError:
        st.warning("Ticket not available yet. Please check back later.")

# --- BACK BUTTON ---
st.markdown("---")
if st.button("⬅️ Back to homepage"):
    st.switch_page("app.py")
