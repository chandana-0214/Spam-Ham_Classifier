import streamlit as st
import pickle

model = pickle.load(open('spam-ham.sav', 'rb'))

# Add background image using CSS
st.markdown(
    '''
    <style>
        body {
            background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
            background-size: cover;
        }
    </style>
    ''', unsafe_allow_html=True
)

# Set the title for the Streamlit app
st.title('Spam-Ham Classifier')

# Get user input
ip = st.text_input("Enter the message")

# Make predictions when the 'predict' button is clicked
if st.button('Predict'):
    op = model.predict([ip])
    st.title(op[0])
