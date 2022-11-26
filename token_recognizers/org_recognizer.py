def get_org(ner_list):
    org = []
    orgs_tmp = []
    
    for ner_dict in ner_list:
        if ner_dict['entity'] == 'B-ORG':
            if len(org) == 0:
                org.append(ner_dict['word'])
            else:
                orgs_tmp.append([org])
                org = []
                org.append(ner_dict['word'])
        elif ner_dict['entity'] == 'I-ORG':
            org.append(ner_dict['word'])
    orgs_tmp.append([org])
    
    final_org_list = []
    for org_list in orgs_tmp:
        full_org = ' '.join(org_list[0]).replace(' ##', '').replace(' .', '.')
        final_org_list.append(full_org)
    
    org = final_org_list[0] if len(final_org_list) > 0  else ''
   
    return org


