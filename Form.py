import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

st.set_page_config(page_title="Form", page_icon="🥳")
st.header('Recommendation Form (FILM/SERIES)')
st.caption(':red[Isi aja. Data yang ngisi gk bakal disimpan]')
# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

# data
existing_data = conn.read(
    worksheet="Sheet1",
    ttl="20m",
    usecols=[0,1,2,3,4,5]
)
existing_data=existing_data.dropna(how="all")

# input part
with st.form(key="Rekomendation_Form"):
    film = st.text_input(label="Rekomendasi film/series*")
    jenis = st.selectbox(label="Jenis",
                         options=['Film','Series'],
                         index=None)
    tahun = st.date_input(label="Rilis tahun? Pilih tahunnya saja",
                          value=None, min_value=pd.to_datetime('1980-01-01').date(),
                          max_value=pd.to_datetime('today').date())
    lagu = st.text_input(label="Rekomendasi lagu*")
    playlist = st.text_input(label="Playlist spotify/yt")
    st.caption(':red[Link/Nama playlistnya kalau ada]')
    tambahan = st.text_area(label='Tambahan APAPUN')

    st.markdown('**required*')

    submit_button = st.form_submit_button(label="Kirim")

    # pressed buttonl
    if submit_button:
        if not film and not lagu:
            st.warning("Bagian film dan lagunya tolong diisi yah. hehe", icon="⚠️")
            st.stop()
        if not film :
            st.warning("Bagian filmnya tolong diisi yah. hehe", icon="⚠️")
            st.stop()
        if not lagu:
            st.warning("Bagian lagunya tolong diisi yah. hehe", icon="⚠️")
            st.stop()
        elif existing_data['Film'].astype(str).str.contains(film).any():
            st.warning('Film ini sudah pernah diisi. Ada film lain?')
            st.stop()
        elif existing_data['Song'].astype(str).str.contains(lagu).any():
            st.warning('Lagu ini sudah pernah diisi. Ada lagu lain?')
            st.stop()
        else:
            Rek_data= pd.DataFrame(
                [
                    {
                        "Film": film,
                        'Jenis':jenis,
                        'Tahun' : tahun,
                        'Song': lagu,                    
                        'Playlist': playlist,
                        'else': tambahan


                    }
                ]
            )
            # add the new data to Rek_data
            updated_df = pd.concat([existing_data, Rek_data], ignore_index=True)
            
            # Update Google sheets
            conn.update(worksheet='Sheet1', data=updated_df)
            st.success("SUKSESS... Makasih", icon='😎')


# SIDEBAR
st.link_button('Buka page', 'https://rekomendasigess.streamlit.app/Mine')
st.sidebar.subheader("3 Rekomendasi terakhir:")
st.sidebar.dataframe(existing_data[['Film', 'Song']].tail(3))
st.sidebar.warning('Tabel butuh waktu untuk update 🙂\n sekitar 5 menit')

st.sidebar.markdown("<font size='2'>View the code <a href='https://github.com/Alanjamlu34/Streamlit-GSheets.git'>GitHub</a>.</font>",unsafe_allow_html=True)

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
