from google.cloud import firestore
import streamlit as st
# Add a new user to the database
db = firestore.Client("outreachpro-60c24-firebase-adminsdk-ojzou-7681634a15.json")
Q1 = st.text_input("type your first name")
Q2 = st.text_input("type your last name")
doc_ref = db.collection('{}').document('{}').format(Q1, Q2)
doc_ref.set({
    'first': Q1,
    'last': Q2,
    'born': 2020
})

# Then query to list all users
users_ref = db.collection('users')

for doc in users_ref.stream():
    print('{} => {}'.format(doc.id, doc.to_dict()))
