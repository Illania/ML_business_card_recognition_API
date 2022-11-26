import os
import re
path = os.path.dirname(os.path.abspath(__file__))

job_titles = []

with open(path + '/../data/jobs') as job_names:
    for job_name in job_names:
        job_name = job_name.strip()
        if len(job_name) > 0:
            job_titles.append(job_name)

def get_job_title(text):
    for title in job_titles:
        if re.search(title, text, re.IGNORECASE):
            return title
