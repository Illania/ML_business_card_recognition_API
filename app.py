import streamlit as st
import io
from PIL import Image
from contact_recognizer import recognize_contact
from card_recognizer import detect_contours
from text_recognizer import get_text

def load_image():
    """Создание формы для загрузки изображения"""
    uploaded_file = st.file_uploader(
        label='Выберите изображение для распознавания')
    if uploaded_file is not None:
        image_data = uploaded_file.getvalue()
        st.image(image_data)
        image = Image.open(io.BytesIO(image_data)).convert('RGB') 
        return image
    else:
        return None
    
st.title('Business card text recognition')
pil_img = load_image()

result = st.button('Распознать')
if result:
    if(pil_img is None):
        st.write("Вы не загрузили изображение.")   
    else:
        business_card =  detect_contours(pil_img)
        text = get_text(pil_img)
        contact = recognize_contact(text)
        contact.print_contact()

