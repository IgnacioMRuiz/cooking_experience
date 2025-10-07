import streamlit as st
from pathlib import Path

# --- PAGE CONFIG ---
st.set_page_config(page_title="Cooking Studio Experiences", page_icon="🍳", layout="wide")

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

# --- STYLES ---
st.markdown(
    """
    <style>
        .navbar {
            display: flex;
            justify-content: center;
            background-color: #fff3e6;
            padding: 0.7rem 0;
            border-radius: 8px;
            margin-bottom: 1.5rem;
        }
        .navbar a {
            color: #3b3b3b;
            text-decoration: none;
            margin: 0 1.5rem;
            font-weight: 500;
            font-size: 1rem;
        }
        .navbar a:hover { color: #f2a154; }
        .footer {
            text-align: center;
            font-size: 0.85rem;
            color: #777;
            padding: 1.2rem 0 0.6rem 0;
            margin-top: 3rem;
            border-top: 1px solid #eee;
        }
        .tag {
            background-color: #ffcccb;
            color: #b30000;
            padding: 2px 8px;
            border-radius: 5px;
            font-size: 0.8rem;
            font-weight: bold;
            margin-left: 8px;
        }
        .tag-open {
            background-color: #c9f5d9;
            color: #008000;
        }
    </style>
    <div class="navbar">
        <a href="#">Workshops</a>
        <a href="#">Gift Cards</a>
        <a href="#">About us</a>
        <a href="#">Contact</a>
    </div>
    """,
    unsafe_allow_html=True
)

# --- MAIN PAGE ---
st.title("🍳 Cooking Studio Experiences")
st.subheader("Discover Our Upcoming Culinary Workshops")

st.markdown(
    """
    At **Cooking Studio Experiences**, we believe that distance should never stop people from sharing a meal together.  
    These online sessions are more than just cooking classes — they’re small shared moments where two people in different places create the same dish, talk, and laugh as if they were in the same kitchen.  
    Each experience is designed to make ordinary mornings or nights feel special — a warm ritual, a connection built through flavor, timing, and presence.  
    Once you reserve your spot, all that’s left is to gather the ingredients, start the call, and let the moment unfold — one recipe, two kitchens, and a shared memory that feels closer than miles apart.
    """
)

# --- LOCAL IMAGE PATHS ---
base_dir = Path(__file__).parent
img_pancakes = base_dir / "pancakes.jpg"
img_pasta = base_dir / "pasta.jpg"
img_sushi = base_dir / "sushi.jpg"
img_dessert = base_dir / "dessert.jpg"

# --- ACTIVITIES GRID ---
col1, col2 = st.columns(2)

with col1:
    if img_pancakes.exists():
        st.image(str(img_pancakes), use_container_width=True)
    st.markdown("### 🥞 Pancake Breakfast")
    st.markdown("Cozy brunch session — **Saturday, 9:00–10:30 AM (Online Class)**.")
    st.markdown("Fluffy pancakes with berries, syrup, and a touch of creativity.")
    if st.button("Reserve this class", key="btn_pancakes"):
        st.switch_page("pages/1_Breakfast_Pancakes.py")

with col2:
    if img_pasta.exists():
        st.image(str(img_pasta), use_container_width=True)
    st.markdown("### 🍝 Italian Pasta Night <span class='tag'>FULLY BOOKED</span>", unsafe_allow_html=True)
    st.markdown("Fresh handmade pasta workshop — **Thursday, 19:00–20:30 PM (Online Class)**.")
    st.markdown("Learn to make authentic tagliatelle, creamy sauces, and rustic Italian flavors.")
    st.button("Reserve this class", disabled=True, key="btn_pasta")

col3, col4 = st.columns(2)

with col3:
    if img_sushi.exists():
        st.image(str(img_sushi), use_container_width=True)
    st.markdown("### 🍣 Sushi Workshop <span class='tag'>FULLY BOOKED</span>", unsafe_allow_html=True)
    st.markdown("Japanese sushi experience — **Friday, 18:30–20:00 PM (Online Class)**.")
    st.markdown("Roll, slice, and plate authentic maki and nigiri with expert guidance.")
    st.button("Reserve this class", disabled=True, key="btn_sushi")

with col4:
    if img_dessert.exists():
        st.image(str(img_dessert), use_container_width=True)
    st.markdown("### 🍰 French Desserts <span class='tag'>FULLY BOOKED</span>", unsafe_allow_html=True)
    st.markdown("Elegant pâtisserie session — **Sunday, 16:00–17:30 PM (Online Class)**.")
    st.markdown("Create delicate tarts and crème brûlée, exploring classic French techniques.")
    st.button("Reserve this class", disabled=True, key="btn_dessert")

# --- FOOTER ---
st.markdown(
    """
    <div class="footer">
        © 2025 Cooking Studio Experiences — All rights reserved.<br>
        Designed for culinary enthusiasts around the world 🌍
    </div>
    """,
    unsafe_allow_html=True
)

# py -m streamlit run app.py