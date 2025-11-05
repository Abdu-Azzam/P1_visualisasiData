import streamlit as st  
st.write("Displaying an Images")  
# Displaying Image by specifying path  
st.image("D:/Gambar/3.jpeg")  
#Image Courtesy by unplash  
st.write("Image Courtesy: unplash.com")  

import streamlit as st  
# Image Courtesy  
st.write("Diplaying Multiple Images")  
# Listing out animal images  
animal_images = [  
'D:/Gambar/1.jpeg',  
'D:/Gambar/2.jpeg',  
'D:/Gambar/3.jpeg',  
'D:/Gambar/4.jpeg',  
]  
# Displaying Multiple images with width 150  
st.image(animal_images, width=150)  
# Image Courtesy  
st.write("Image Courtesy: Unplash")  



import streamlit as st
import base64

# Fungsi untuk menambahkan gambar lokal sebagai background
def add_local_background_image(image_path):
    with open(image_path, "rb") as img_file:
        encoded_string = base64.b64encode(img_file.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/jpeg;base64,{encoded_string});
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Judul atau teks di halaman
st.write("Background Image Test")

# Panggil fungsi dengan path ke gambarmu
add_local_background_image("D:/Gambar/2.jpeg")




import streamlit as st
from PIL import Image
original_image = Image.open("D:/Gambar/4.jpeg")
# Display Original Image
st.title("Original Image")
st.image(original_image)
# Resizing Image to 600*400
resized_image = original_image.resize((600, 400))
#Displaying Resized Image
st.title("Resized Image")
st.image(resized_image)