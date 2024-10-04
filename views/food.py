import streamlit as st

st.title("Makanan Khas Surabaya")

# --- FOOD 1 ---
st.subheader("Gado-gado", anchor=False)
column1, column2 = st.columns(2,gap="small",vertical_alignment="center")
with column1:
    st.image("assets/gado-gado.jpeg")

with column2:
    st.write("Makanan yang terdiri atas sayur-sayuran, kentang, tempe, tahu, telur rebus, dan lain-lain diberi bumbu sambal kacang dan sebagainya.")

# --- FOOD 2 ---
st.subheader("Tahu tek", anchor=False)
column3, column4 = st.columns(2,gap="small",vertical_alignment="center")
with column3:
    st.write("Salah satu masakan khas Jawa Timur khususnya di Kota Surabaya yang terdiri atas tahu goreng setengah matang dan lontong yang dipotong kecil-kecil dengan alat gunting dan garpu untuk memegang tahu atau lontong, telur, kentang goreng, sedikit taoge, dan irisan ketimun dipotong kecil-panjang (seperti acar), lalu setelah disiram dengan saus kacang dengan campuran petis di atasnya, ditaburkan kerupuk udang yang bentuknya kecil dengan diameter sekitar 3 cm.")

with column4:
    st.image("assets/tahu-tek.jpeg")

# --- FOOD 3 ---
st.subheader("Rawon", anchor=False)
column5, column6 = st.columns(2,gap="small",vertical_alignment="center")
with column5:
    st.image("assets/rawon.jpeg")

with column6:
    st.write("Masakan khas Indonesia yang berasal dari Ponorogo, Jawa Timur, yang berupa sup daging berkuah hitam dengan campuran bumbu khas yang menggunakan kluwek. Makanan ini telah berusia lebih dari 1.000 tahun. Rawon dari Ponorogo menyebar ke penjuru Jawa Timur dan dikenal sebagai masakan khas Jawa Timur.")
