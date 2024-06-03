import streamlit as st 

st.title("Gimnasio para Perras")
st.image('https://phantom-expansion.unidadeditorial.es/a04167714c72f7bda85dac21a7351c69/crop/0x963/1294x1689/resize/1200/f/webp/assets/multimedia/imagenes/2022/10/28/16669489421882.jpg')

st.subheader('Bienvenido al gimnasio más famoso de la ciudad')


st.write('**Este gimnasio para perras fue fundado en el año 2018, y ha sido el único de su tipo durante todos estos años en la ciudad.Algunas de nuestras perras más famosas han sido la perra Mia y la perra Lana.¿Será su perra la próxima?**')


st.markdown(':orange[Para ingresar al gym, rellene el siguiente formulario]')

with st.form(key='my_form'):
    name=st.text_input('Ingrese el nombre y apellidos de su perra')
    if name=='Mia' or name == 'Lana':
        st.write("Es toda una leyenda esa perra🐩")
    edad=st.number_input('Cuántos años tiene su perra')
    if edad<15:
        edad= RuntimeError('Para ingresar al gym debe de tener más de 15 años,no entrenamos a perritas')
        st.exception(edad)
    raza=st.text_input('A qué raza pertenece')
    if raza == 'Hockey' or raza=='Dalmata' or raza=='Pequines':
        st.write("Una de mis favoritas🐕")
    ciudad= st.text_input('En que lugar reside')
    razón=st.text_input("Por qué razón quiere qué su perra vaya al gym")
    
    st.form_submit_button("Enviar Formulario")
    
st.subheader('Datos de su perra🐩')
col1,col2,col3,col4,col5= st.columns(5)
col1.write(f'nombre: :blue[{name}]')
col2.write(f'edad: :blue[{edad}]')
col3.write(f'raza: :blue[{raza}]')
col4.write(f'donde vive: :blue[{ciudad}]')
col5.write(f'Por qué ingresa al gym: :blue[{razón}]')

