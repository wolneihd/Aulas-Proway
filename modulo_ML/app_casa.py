import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import plotly.express as px

# ter dados
def generate_house_data(n_samples=100):
    np.random.seed(42)
    size = np.random.normal(1500, 500, n_samples)
    price = size * 100 + np.random.normal(0, 10_000, n_samples)
    return pd.DataFrame({'size_sqft': size, 'price': price})

# treinamento
def train_model():
    df = generate_house_data()
    X = df[['size_sqft']]
    y = df['price']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model    

st.title('Predições de valores de casas')
st.write('Digite o tamanho da casa em pés quadrados:')

# ponto chave
modelo = train_model()
size = st.number_input('Tamanho da casa em pés: ', min_value=500, max_value=1500, placeholder='Digite um número')

def avaliation_model():
    from sklearn.metrics import mean_absolute_error as mae
    from sklearn.metrics import root_mean_squared_error as rmse
    accuracy_score = 
    r2_score = r2_score()
    root_mean_square = mean_squared_error()
    print(accuracy_score, r2_score, root_mean_square)

if st.button('Predição'):
    prediction = modelo.predict([[size]])
    st.success(f'Preço estimado: {prediction[0]:.2f} USD')
    # visualização
    df = generate_house_data()
    fig = px.scatter(df, x='size_sqft', y='price', title='preço vs. tamanho')
    fig.add_scatter(x=[size], y=[prediction[0]], mode='markers')
    st.plotly_chart(fig)
