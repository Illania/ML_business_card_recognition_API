def get_loc(ner_list):
    loc = []
    loc_tmp = []
    
    for ner_dict in ner_list:
        if ner_dict['entity'] == 'B-LOC':
            if len(loc) == 0:
                loc.append(ner_dict['word'])
            else:
                loc_tmp.append([loc])
                loc = []
                loc.append(ner_dict['word'])
        elif ner_dict['entity'] == 'I-LOC':
            loc.append(ner_dict['word'])
    loc_tmp.append([loc])
    
    final_loc_list = []
    for loc_list in loc_tmp:
        full_loc = ' '.join(loc_list[0]).replace(' ##', '').replace(' .', '.')
        final_loc_list.append(full_loc)
    
    loc = final_loc_list[0] if len(final_loc_list) > 0  else ''
   
    return loc