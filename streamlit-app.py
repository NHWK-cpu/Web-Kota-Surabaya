import streamlit as st

# --- PAGE SETUP ---
landing_page = st.Page(
    page="views/landing_page.py",
    title="Profil Kota",
    icon=":material/location_city:",
    default=True,
)

destination = st.Page(
    page="views/destination.py",
    title="Tempat Ikonik",
    icon=":material/explore:",
)

food = st.Page(
    page="views/food.py",
    title="Makanan Khas",
    icon=":material/restaurant:",
)

# ---NAVIGATION SETUP [WITHOUT SECTIONS] ---
pg = st.navigation(pages=[landing_page,destination,food])

# --- SHARED ON ALL PAGES ---
st.logo("assets/LogoSurabaya.png")
st.sidebar.text("Hafizh Ammar Muflih\n24050974055\nPendidikan Teknologi Informasi 2024")
st.sidebar.link_button(label="@hafizh_komputer",url="https://www.instagram.com/hafizh_komputer/")
st.sidebar.link_button(label="@widi.Iphone", url="https://www.instagram.com/widi.iphone/")
st.sidebar.link_button(label="@hmppti.unesa", url="https://www.instagram.com/hmppti.unesa/")
st.sidebar.link_button(label="@hmpti.unesa", url="https://www.instagram.com/hmpti.unesa/")
st.sidebar.link_button(label="@hmpsi.unesa", url="https://www.instagram.com/hmpsi.unesa/")
st.sidebar.text("24050974055@mhs.unesa.ac.id")
st.sidebar.text("Di Dukung @BoloSewu Network & Widi.Iphone")

# --- RUN NAVIGATION ---
pg.run()