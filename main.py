import streamlit as st
from streamlit_option_menu import option_menu
import account,chatbot,career_development,home
import toml 
st.set_page_config(page_title="Pathcoder",)

class MultiApp:
     def __init__(self):
        self.apps = []
     def add_app(self, title, function):
         self.apps.append({
            "title": title,
            "function": function
         })

     def run():
         with st.sidebar:
             app=option_menu(
                menu_title="pathcoder",
                 options=['home','account','career_development','chatbot'],
                 icons=['house','user','chat','person'],
                 menu_icon="cast",
                 default_index=1 ,
                 styles={
                     "countainer": {"padding": "1rem 1rem"},
                     "icon": {"color":"white","font-size": "23px"},
                     "nav-link": {"font-size": "20px","text-align": "left","margin":"0px","text-transform":"uppercase","color":"white"},
                     "nav-link-selected": {"background-color": "green"},
                 }
             )
         if app == 'home':
             home.app()

         if app == 'account':
             account.app()

         if app == 'career_development':
             career_development.app()

         if app == 'chatbot':
             chatbot.app()
     run()









