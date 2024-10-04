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

# ---WIDGET FUNCTION---
def ig_hafizh():
    st.switch_page('https://www.instagram.com/hafizh_komputer/')
def ig_widiiphone():
    st.switch_page('https://www.instagram.com/widi.iphone/')
def ig_himpti():
    st.switch_page('https://www.instagram.com/hmppti.unesa/')
def ig_himti():
    st.switch_page('https://www.instagram.com/hmpti.unesa/')
def ig_himsi():
    st.switch_page('https://www.instagram.com/hmpsi.unesa/')

# --- SHARED ON ALL PAGES ---
st.logo("assets/LogoSurabaya.png")
st.sidebar.text("Hafizh Ammar Muflih\n24050974055\nPendidikan Teknologi Informasi 2024")
st.sidebar.button("@hafizh_komputer",on_click=ig_hafizh)
st.sidebar.button("@widi.Iphone", on_click=ig_widiiphone)
st.sidebar.button("@hmppti.unesa", on_click=ig_himpti)
st.sidebar.button("@hmpti.unesa", on_click=ig_himti)
st.sidebar.button("@hmpsi.unesa", on_click=ig_himsi)
st.sidebar.text("24050974055@mhs.unesa.ac.id")
st.sidebar.text("Di Dukung @BoloSewu Network & Widi.Iphone")

# --- RUN NAVIGATION ---
pg.run()