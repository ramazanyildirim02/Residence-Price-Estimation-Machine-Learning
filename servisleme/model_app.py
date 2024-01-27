import streamlit as st
import numpy as np 
import joblib
from predict_cost import predict 

# Arayüz

st.markdown("## Residence Fiyat Tahmini")
st.write("-----------------------------------")


bedroom_count = st.number_input("Yatak odası sayısı")
bathroom_count = st.number_input("Banyo sayısı")
m2 = st.number_input("Kaç metrekare?")
floor = st.number_input("Kaçıncı kat?")
location_lat = st.number_input("Latitude (40-42 arasında bir değer girin)")
location_lng = st.number_input("Longitude (28-30 arasında bir değer girin)")
events = st.number_input("Etkinlik izni (Evet ise 1, hayır ise 0)")
smoke = st.number_input("Sigara izni (Evet ise 1, hayır ise 0)")
pets = st.number_input("Evcil hayvan izni (Evet ise 1, hayır ise 0)")

st.markdown("###### İlçe (Hangi ilçede istiyorsanız onu 1 yapın ve diğer ilçelere dokunmayın)")

atasehir = st.number_input("Ataşehir")
beykoz = st.number_input("Beykoz")
beyoglu = st.number_input("Beyoğlu")
besiktas = st.number_input("Beşiktaş")
eyup = st.number_input("Eyüp")
gokturk = st.number_input("Göktürk-Kemerburgaz")
kadikoy = st.number_input("Kadıköy")
kartal = st.number_input("Kartal")
kagıthane = st.number_input("Kağıthane")
maltepe = st.number_input("Maltepe")
sariyer = st.number_input("Sarıyer")
cekmekoy = st.number_input("Çekmeköy")
umraniye = st.number_input("Ümraniye")
uskudar = st.number_input("Üsküdar")
sisli = st.number_input("Şişli")

# Tahmin butonu

if st.button("Ev fiyatı tahmin et"):
    fiyat = predict(np.array([[bedroom_count,bathroom_count,m2,floor,location_lat,
    location_lng,events,smoke,pets,atasehir,beykoz,beyoglu,besiktas,eyup,gokturk,
    kadikoy,kartal,kagıthane,maltepe,sariyer,cekmekoy,umraniye,uskudar,sisli]]))

    st.text(fiyat[0])




