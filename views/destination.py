import streamlit as st

with open("style.css") as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)

# --- HEAD ---
st.title("Destinasi Wisata Ikonik", anchor=False)
st.write(
    '''
    Jika kamu datang ke Surabaya, tidak lengkap rasanya kalau tidak mengunjungi tempat ini.
    Pasalnya, selain menjadi kota dengan sejarah pahlawan Surabaya juga dikenal sebagai salah satu kota terbesar di Indonesia.
    Pastinya kota ini memiliki banyak tempat wisata yang tidak akan membuatmu bosan mendatanginya.
    '''
)

# --- FIRST ROW ---
column1, column2 = st.columns(2,gap="medium",vertical_alignment="center")

with column1:
    st.image("assets/surabaya-carnival.jpeg")
    st.subheader("Surabaya Carnival", anchor=False)
    st.write(
        '''
        Surabaya Carnival adalah destinasi wisata bernuansa circus, yang terletak di daerah Surabaya selatan.
        '''
    )
with column2:
    st.image("assets/tugu-pahlawan.jpeg")
    st.subheader("Tugu Pahlawan", anchor=False)
    st.write(
        '''
        Salah satu monumen bersejarah yang berada di kota Surabaya yang berada di Surabaya pusat.
        '''
    )

# --- SECOND ROW ---
column3, column4 = st.columns(2, gap="medium", vertical_alignment="center")

with column3:
    st.image("assets/Kebun-Binatang-Surabaya.jpg")
    st.subheader("Kebun Binatan Surabaya", anchor=False)
    st.write(
        '''
        Penangkaran hewan yang berada di kota Surabaya pusat dan terdapat banyak sekali satwa di dalam nya.
        '''
    )

with column4:
    st.image("assets/monumen-kapal-selam.jpg")
    st.subheader("Monumen Kapal Selam", anchor=False)
    st.write(
        '''
        Merupakan tempat wisata yang dimana terdapat bangkai kapal pasopati yang di pernah di gunakan oleh NKRI.
        '''
    )