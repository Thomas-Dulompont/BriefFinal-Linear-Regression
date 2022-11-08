import streamlit as st
import pickle

# Importation de l'algo
pickle_in = open('modelRid.pkl', 'rb')
model = pickle.load(pickle_in)

# Titre & Sous-titre
st.title("Calulateur Immobilier")
st.text('Entrez les informations de votre bien pour calculer son prix !')

col1, col2 = st.columns(2)

with col1:
    chambres = st.selectbox(
        'Nombre de chambres',
        (range(1, 50))
    )
    m2_habitable = st.number_input("M2 Habitable", key="m2_habitable")
    m2_total = st.number_input("M2 Total", key="m2_total")

    etages = st.selectbox(
        "Nombre d'étages",
        (range(0, 5))
    )
    vue = st.selectbox(
        "Vue (0 mauvaise, 4 bonne",
        (range(0, 5))
    )
    vue_mer = st.checkbox("Vue sur la mer")
    salle_eau = st.slider("Nombre salle de bain", max_value=8.0, min_value=0.0, step=0.25)
with col2:
    condition = st.selectbox(
        "Condition",
        (range(1, 6))
    )
    grade = st.selectbox(
        "Grade",
        (range(1, 14))
    )
    m2_cave = st.number_input("M2 Cave", key="m2_cave")
    annee_construction = st.number_input("Année Construction", key="annee_construction", min_value=1900)
    annee_renovation = st.number_input("Année Renovation (vide si jamais renovée)", key="annee_renovation", min_value=0)

    cp = (98001,98002,98003,98004,98005,98006,98007,98008,98010,98011,98014,98019,98022,98023,98024,98027,98028,98029,98030,98031,98032,98033,98034,98038,98039,98040,98042,98045,98052,98053,98055,98056,98058,98059,98065,98070,98072,98074,98075,98077,98092,98102,98103,98105,98106,98107,98108,98109,98112,98115,98116,98117,98118,98119,98122,98125,98126,98133,98136,98144,98146,98148,98155,98166,98168,98177,98178,98188,98198,98199)

    code_postal = st.selectbox(
        "Code Postal",
        (98001,98002,98003,98004,98005,98006,98007,98008,98010,98011,98014,98019,98022,98023,98024,98027,98028,98029,98030,98031,98032,98033,98034,98038,98039,98040,98042,98045,98052,98053,98055,98056,98058,98059,98065,98070,98072,98074,98075,98077,98092,98102,98103,98105,98106,98107,98108,98109,98112,98115,98116,98117,98118,98119,98122,98125,98126,98133,98136,98144,98146,98148,98155,98166,98168,98177,98178,98188,98198,98199)
    )

if vue:
    vue = 1
else:
    vue = 0
if vue_mer:
    vue_mer = 1
else:
    vue_mer = 0

if annee_renovation == 0:
    annee_renovation = annee_construction

df_user = [chambres, salle_eau, m2_habitable, m2_total, etages, vue_mer, vue, condition, grade, m2_habitable-m2_cave, m2_cave, annee_construction, annee_renovation]

for code in cp:
    if code == code_postal:
        df_user.append(1)
    else:
        df_user.append(0)

if st.button('Calculer'):
    st.subheader('Le prix est de : {}$'.format(round(model.predict([df_user])[0], 2)))