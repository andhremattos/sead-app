#importando bibliotecas
import streamlit as st


# To make things easier later, we're also importing numpy and pandas for
# working with sample data.


import numpy as np
import pandas as pd

st.title('Meu primeiro App usando Streamlit - Este é diferente.')

st.write("Temos a informação de um data frame:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

""" 
# Meu primeiro app

Este é um **Aplicativo**. Carlos André Lima de Matos
""" 