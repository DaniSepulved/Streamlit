import streamlit as st
import pandas as pd
import csv
import random
from faker import Faker

# fake = Faker('es_ES')

# Colores = ['Rojo', 'Azul', 'Negro', 'Blanco', 'Gris', 'Verde', 'Amarillo', 'Naranja', 'Plateado', 'Café']

# Vehiculos = []

# for i in range(2000):
#     Id_Vehiculo = i + 100
#     Id_Usuario = i + 1
#     Placa = fake.license_plate()
#     Color = random.choice(Colores)
#     Vehiculos.append([Id_Vehiculo, Id_Usuario, Placa, Color])

# rutacsv = 'vehiculos.csv'

# with open('vehiculos.csv', mode='w', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file)
#     writer.writerow(['Id_Vehiculo', 'Id_Usuario', 'Placa', 'Color'])
#     writer.writerows(Vehiculos)


df = pd.read_csv("vehiculos.csv")  

st.write("Vista previa del DataFrame:")
st.dataframe(df)

st.subheader("Ver un vehículo por índice")
indice = st.slider("Selecciona un índice", 0, len(df) - 1, 0)
if st.button("Mostrar vehículo (por índice)"):
    st.write(df.iloc[indice])

st.subheader("Filtrar vehículos por Color o Placa")
col1, col2 = st.columns(2)

with col1:
    color = st.text_input("Buscar por color", "")

with col2:
    placa = st.text_input("Buscar por parte de la placa", "")

# Aplicar filtros
filtro = df
if color:
    filtro = filtro.loc[filtro['Color'].str.contains(color, case=False, na=False)]

if placa:
    filtro = filtro.loc[filtro['Placa'].str.contains(placa.upper(), na=False)]

st.write(f"Resultados filtrados: {len(filtro)} fila(s)")
st.dataframe(filtro)

st.subheader("Editar color de un vehículo")

id_vehiculo = st.number_input("ID del vehículo a editar", min_value=int(df['Id_Vehiculo'].min()), max_value=int(df['Id_Vehiculo'].max()), step=1)
nuevo_color = st.text_input("Nuevo color:")

if st.button("Actualizar color"):
    if id_vehiculo in df['Id_Vehiculo'].values:
        df.loc[df['Id_Vehiculo'] == id_vehiculo, 'Color'] = nuevo_color
        st.success(f"Color actualizado del vehículo con ID {id_vehiculo}.")
        st.write(df.loc[df['Id_Vehiculo'] == id_vehiculo])
    else:
        st.error("El ID de vehículo no existe.")

st.subheader("Descargar el CSV actualizado")
csv = df.to_csv(index=False).encode("utf-8")
st.download_button("Descargar CSV", data=csv, file_name="vehiculos_actualizado.csv", mime="text/csv")