import streamlit as st
from scrape import scrape_website

st.title("Webscraper Deluxe")
url = st.text_input("Enter URL:")

if st.button("Scrape Site"):
    st.write("Scraping site...")
    # Scrape site here
    result = scrape_website(url)
    print(result)
