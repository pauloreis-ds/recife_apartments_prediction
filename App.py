import streamlit as st
from util import *


def check_float_value(value):
    value = value.replace(",", ".")
    try:
        value = float(value)
    except:
        pass

    return value


def get_brazilian_money_format(money_str):
    money_str = money_str.replace(',', 'comma')
    money_str = money_str.replace('.', ',')
    money_str = money_str.replace('comma', '.')
    return money_str


if __name__ == "__main__":
    print("Initializing App.")

    background_image = '''
    <style>
        body {
            background-image: url("https://raw.githubusercontent.com/pauloreis-ds/Projetos/master/Previs%C3%A3o%20-%20Pre%C3%A7o%20Apartamentos%20Recife/images/recife.png");
            background-size: cover;
        }
    </style>'''
    st.markdown(background_image, unsafe_allow_html=True)

    load_saved_artifacts()
    location_names = get_location_names()

    st.header("**Localização**")
    location = st.selectbox("", location_names)
    st.header("**Área (m²)**")
    square_foot = st.text_input("", 50)
    st.header("**Quartos**")
    bedroom = st.selectbox("", [1, 2, 3, 4, 5])
    st.header("**Banheiros**")
    bathroom = st.selectbox(" ", [1, 2, 3, 4, 5])

    square_foot = check_float_value(square_foot)

    if isinstance(square_foot, float):
        if square_foot > 600 or square_foot < 30:
            st.error("**Área(m²) inválida!**")
        else:
            prediction = get_estimated_price(location, square_foot, bedroom, bathroom)
            prediction_txt = "R$ {:,.2f}".format(prediction)
            prediction_txt = get_brazilian_money_format(prediction_txt)
            st.markdown(f"<h1 style='text-align: center; color: white;'>{prediction_txt}</h1>", unsafe_allow_html=True)
    else:
        st.error("**Valor não numérico detectado!**")


