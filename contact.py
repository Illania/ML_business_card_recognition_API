class Contact(object):
    def __init__(self):
        self.name = 'N/A'
        self.emails = []
        self.phones = []
        self.job_title = 'N/A'
        self.organization = 'N/A'
        self.website = 'N/A'
        self.addr = []
        
    def print_contact(self):
        print(f'Name: {self.name}')   
        print(f'Organization: {self.organization}')   
        print(f'Address: {self.addr}')  
        print(f'Job title: {self.job_title}') 
        print(f'Phones: {", ".join(self.phones)}') 
        print(f'Email: {", ".join(self.emails)}') 
        print(f'Website: {", ".join(self.website)}')    