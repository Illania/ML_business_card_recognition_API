import io
from PIL import Image
from token_recognizers.email_recognizer import get_emails
from token_recognizers.job_recognizer import get_job_title
from token_recognizers.name_recognizer import get_name
from token_recognizers.org_recognizer import get_org
from token_recognizers.loc_recognizer import get_loc
from token_recognizers.phone_recognizer import get_phones
from token_recognizers.website_recognizer import get_websites
from card_recognizer import find_card_contour
from text_recognizer import get_text
from bert_model import get_tokens
from contact import Contact


def recognize_contact(text):
    contact = Contact()
    ner_list = get_tokens(text)
    contact.name = get_name(ner_list)
    contact.organization = get_org(ner_list)
    contact.addr = get_loc(ner_list)
    contact.job_title = get_job_title(text)
    contact.phones = get_phones(text)
    contact.emails = get_emails(text)
    contact.website = get_websites(text)
    return contact


def get_contact_from_card(file_path):
    with open(file_path, "rb") as image:
        image_data = image.read()
        pil_img = Image.open(io.BytesIO(image_data)).convert("RGB")
        business_card = find_card_contour(pil_img)
        text = get_text(business_card)
        contact = recognize_contact(text)
    return contact
