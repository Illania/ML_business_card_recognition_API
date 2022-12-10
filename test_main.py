import os
import sys
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

from fastapi.testclient import TestClient
from main import app
from contact_recognizer import get_contact_from_card
import jsonpickle
import json

client = TestClient(app)

def test_main_page():
    ''' Test main page is working and returns http status 200 - OK
    '''
    response = client.get("/")
    assert response.status_code == 200


def test_upload_and_parse_json():
    ''' Test image upload is working.
        Test json data returned for uploaded contact card is correct.
    '''
    file_path = 'test_data/card.jpg'
    if os.path.isfile(file_path):
        with open(file_path, 'rb') as f:
            response = client.post('/upload', files={"upload_file": ('card.jpg', f, "image/jpeg")})
            assert response.status_code == 200
    
    response = client.get("/contact/json/card.jpg")
    json_data = response.json()
    contact = get_contact_from_card(file_path)  
    assert json_data == jsonpickle.encode(contact)
    check_contact_data(json.loads(json_data))
    
    uploaded_file_path = 'uploads/card.jpg'
    if os.path.exists(uploaded_file_path):
        os.remove(uploaded_file_path)


def check_contact_data(json_object):
    ''' Helper method that asserts that all parsed business card data is correct.
    '''
    assert json_object["name"] == 'Larry Page'     
    assert json_object['organization'] == 'Google'
    assert json_object['emails'][0] == 'larry@google.com'
    assert json_object['website'][0] == 'http://google.com/'
    assert json_object['job_title'] == 'CEO'
    assert json_object['phones'] == ['650 330-0100', '650 618-1499']





    
