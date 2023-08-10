import streamlit as st
import helper

st.title("TSOAI dashboard")

st.write("Collections")
collections = helper.get_collections()

st.write("Papers")
papers = helper.get_papers()

st.write("Terms")
papers = helper.get_terms()

