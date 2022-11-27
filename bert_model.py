from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline

def load_model():
    bert_model = AutoModelForTokenClassification.from_pretrained('dslim/bert-large-NER')
    return bert_model

def load_tokenizer():
    bert_tokenizer = AutoTokenizer.from_pretrained('dslim/bert-large-NER')
    return bert_tokenizer
    
def get_tokens(text):
    bert_model = load_model()
    bert_tokenizer = load_tokenizer()
    nlp = pipeline('ner', model=bert_model, tokenizer=bert_tokenizer)
    ner_list = nlp(text)
    return ner_list