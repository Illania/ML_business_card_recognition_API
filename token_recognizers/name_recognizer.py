def get_name(ner_list):
    name = []
    names_tmp = []
    
    for ner_dict in ner_list:
        if ner_dict['entity'] == 'B-PER':
            if len(name) == 0:
                name.append(ner_dict['word'])
            else:
                names_tmp.append([name])
                name = []
                name.append(ner_dict['word'])
        elif ner_dict['entity'] == 'I-PER':
            name.append(ner_dict['word'])
    names_tmp.append([name])
    
    final_name_list = []
    for name_list in names_tmp:
        full_name = ' '.join(name_list[0]).replace(' ##', '').replace(' .', '.')
        final_name_list.append(full_name)
    
    name = final_name_list[0] if len(final_name_list) > 0  else ''
   
    return (name)