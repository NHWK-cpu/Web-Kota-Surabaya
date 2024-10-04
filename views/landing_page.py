import streamlit as st

# --- FIRST SECTION ---
st.title("Kota Surabaya", anchor=False)
st.image('assets/landmark1(cropped).jpg', caption='Landmark Surabaya')
st.write(
    '''
    Surabaya, yang didirikan sekitar tahun 1293. 
    Adalah salah satu kota tertua di Indonesia, namanya berasal dari kata "sura" (ikan hiu putih legenda lokal) dan "baya" (buaya), yang melambangkan perjuangan dan keberanian. 
    Kota ini memiliki peran penting dalam sejarah Indonesia, terutama selama pertempuran Surabaya pada tahun 1945, ketika warga melawan pasukan kolonial Belanda dalam perjuangan menuju kemerdekaan. 
    Dengan lokasi strategis di pesisir utara Pulau Jawa, Surabaya kini dikenal sebagai "Kota Pahlawan" dan menjadi pusat perdagangan, industri, dan pendidikan, mencerminkan keberagaman budaya masyarakatnya.
    \ntirto.id 6 November 2023
    '''
)

# --- SECOND SECTION ---
st.subheader("Pahlawan Kota surabaya", anchor=False)

column1, column2 = st.columns(2, gap="small", vertical_alignment="center")
with column1:
    st.image('assets/perang_10_november.jpg', caption='Bung Tomo', width=300)
with column2:
    st.write(
        '''
        Pahlawan Kota Surabaya dikenal terutama melalui pertempuran bersejarah yang terjadi pada 10 November 1945, yang dipimpin oleh tokoh-tokoh seperti Bung Tomo, yang mengobarkan semangat perjuangan rakyat melawan penjajahan Belanda. 
        Dalam pertempuran ini, warga Surabaya menunjukkan keberanian luar biasa, mempertaruhkan nyawa untuk mempertahankan kemerdekaan yang baru diproklamirkan. 
        Momen ini menjadi simbol perlawanan dan semangat nasionalisme, sehingga 10 November diperingati sebagai Hari Pahlawan. 
        Kota Surabaya pun dijuluki "Kota Pahlawan" sebagai penghormatan kepada semua yang berjuang dan mengorbankan hidup mereka demi kemerdekaan Indonesia.
        \nsumber-liputan86 majalah 19. Rabu, 19 September 1999
        '''
    )

# --- THIRD SESSION ---
st.subheader("Letak Geografis Surabaya", anchor=False)
st.image('assets/peta surabaya.jpg', caption='Geografis Kota Surabaya')
st.write(
    '''
    Surabaya adalah ibu kota provinsi Jawa Timur, Indonesia, dan terletak di bagian timur pulau Jawa. 
    Kota ini berada di pesisir utara, menghadap ke Selat Madura, dan merupakan salah satu kota terbesar di Indonesia. 
    Surabaya dikenal sebagai pusat perdagangan, bisnis, dan pendidikan, serta memiliki pelabuhan yang penting untuk aktivitas ekonomi. 
    Letaknya yang strategis menjadikannya sebagai gerbang utama untuk akses ke wilayah timur Indonesia. 
    \nsumber-liputan86,majalah 19, Rabu 19, September 1999
    '''
)