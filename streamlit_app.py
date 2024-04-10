import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

st.set_page_config(page_title="Form", page_icon="🫡")
# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

# data
existing_data = conn.read(
    worksheet="Sheet1",
    ttl="10m",
    usecols=[0,1,2,3,4,5]
)
existing_data=existing_data.dropna(how="all")

# sidebar
st.header('Recommendation Form')
st.sidebar.markdown("<font size='2'>View the code <a href='https://github.com/Alanjamlu34/streamlit_data_entry_form'>GitHub</a>.</font>", unsafe_allow_html=True)

# input part
with st.form(key="Rekomendation_Form"):
    film = st.text_input(label="Rekomendasi film/series*")
    jenis = st.selectbox(label="Jenis", options=['Film','Series'], index=None)
    tahun = st.date_input(label="Rilis tahun? Pilih tahunnya saja", value=None, min_value=pd.to_datetime('1980-01-01').date(),max_value=pd.to_datetime('today').date())
    lagu = st.text_input(label="Rekomendasi lagu*")
    playlist = st.text_input(label="Playlist spotify/yt")
    tambahan = st.text_area(label='Tambahan')

    st.markdown('**required*')

    submit_button = st.form_submit_button(label="Kirim")

    # pressed buttonl
    if submit_button:
        if not film or not lagu:
            st.warning("Bagian film dan lagunya tolong diisi yah. hehe")
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
st.sidebar.subheader("Data yang Telah Dikirim:")
st.sidebar.dataframe(existing_data[['Film', 'Song']].tail(4))


# Page 2
st.set_page_config(page_title="Mine", page_icon="😶‍🌫️")
st.image('Streamlit-GSheets/Data/Film.png', caption='Favorite Film')