import streamlit as st

# Page 1

st.set_page_config(page_title="Mine", page_icon="😶‍🌫️")
st.title("Film")

st.image('Data/Film.png', caption='Favorite Film')
st.markdown("Film terbaik sepanjang masa")
st.markdown('Nonton Trailer:')
st.markdown("<a href='https://www.youtube.com/watch?v=zSWdZVtXT7E'>INTERSTELLAR</a>.</font>",unsafe_allow_html=True)
st.markdown("<a href='https://youtu.be/bLvqoHBptjg?si=Ac2x8T3Ja8MSbecl'>FORRSET GUMP</a>.</font>",unsafe_allow_html=True)
st.markdown("<a href='https://youtu.be/PsD0NpFSADM?si=TsQE1K7PGEHFlL4m'>500 DAYS OF SUMMER</a>.</font>",unsafe_allow_html=True)

st.title("Playlist")
st.image('Data/lAGU.png', caption='John Mayer')
st.markdown("Playlist <a href='https://open.spotify.com/playlist/3HwtZRMR0HqP5Hcb55pB4f?si=539b8ffbbaa64251'>STOP THIS TRAIN</a>.</font>",unsafe_allow_html=True)

st.title("SEE ALL")
st.markdown("WEB <a href='https://tisian1.odoo.com/playlist'>TisIan</a>.</font>",unsafe_allow_html=True)
st.markdown("Film <a href='https://letterboxd.com/TisIan/'>Letterboxd</a>.</font>",unsafe_allow_html=True)
