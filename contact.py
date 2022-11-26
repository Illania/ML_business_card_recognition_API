import streamlit as st

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
        st.write(f'Name: {self.name}')   
        st.write(f'Organization: {self.organization}')   
        st.write(f'Address: {self.addr}')  
        st.write(f'Job title: {self.job_title}') 
        st.write(f'Phones: {", ".join(self.phones)}') 
        st.write(f'Email: {", ".join(self.emails)}') 
        st.write(f'Website: {", ".join(self.website)}')    