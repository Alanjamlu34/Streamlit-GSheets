import streamlit as st
import csv

# Membuat dictionary untuk menyimpan input dengan kunci q1, q2, q3
user_input = {}

st.title('Rekomendasi Aplikasi')

# Meminta input film/series
film_series = st.text_input('1. Rekomendasi film/series?')
user_input['q1'] = film_series

# Meminta input tempat menonton
where_to_watch = st.text_input('2. Where to watch?')
user_input['q2'] = where_to_watch

# Meminta input lagu/playlist
song_playlist = st.text_input('3. Rekomendasi lagu/playlist')
user_input['q3'] = song_playlist

# Menyimpan input ke file CSV ketika tombol 'Simpan' ditekan
if st.button('Simpan'):
    # Menulis input ke file CSV
    with open("data.csv", mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        # Menulis header jika file baru dibuat atau kosong
        if f.tell() == 0:
            writer.writerow(user_input.keys())
        writer.writerow(user_input.values())
    
    st.success('Input berhasil disimpan ke dalam file data.csv dengan nama kolom q1, q2, dan q3!')

# Menampilkan input yang telah disimpan
st.write('Input yang Anda masukkan:')
for key, value in user_input.items():
    st.write(f"{key}: {value}")