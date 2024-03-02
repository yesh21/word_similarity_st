import streamlit as st
from nltk.corpus import wordnet as wn
import nltk
import ssl

# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context

# nltk.download()


st.title('Word similarity check')

input_check = st.text_input('Enter the word: ')
# Get the size of the array from user input
input_array = st.text_input("Enter your array here")

st.caption("Example format(comma seperated):")
st.code("US, UK, China, India")


if 'similarity_array' not in st.session_state:
    st.session_state.similarity_array = []
if 'similarity_score' not in st.session_state:
    st.session_state.similarity_score = []
if 'return_words' not in st.session_state:
    st.session_state.return_words = []

def check(x, input_checks):
        arrq = wn.synsets(input_check)
        y = wn.synsets(x)
        if arrq != [] and y != []:
            return round(arrq[0].lch_similarity(y[0]), 2)
        
        return 0
# Split the input string by commas and create a list
similarity_array = [x.strip() for x in input_array.split(',')]
similarity_score = [check(x.strip(), input_check) for x in input_array.split(',')]
# for i, x in enumerate(similarity_array):
#     arrq = wn.synsets("dog")[0]
#     y = wn.synsets("dog")[0]
#     similarity_score.append(arrq.wup_similarity(y))
# Display the list
left_column, right_column = st.sidebar.columns(2)

# Add content to the left column
with left_column:
    st.header('Items')
    st.write("The separated list is:", similarity_array)

# Add content to the right column
with right_column:
    st.header('Scores')
    st.write("The separated list is:", similarity_score)
st.title("Result to ["+ input_check + "] Similar word/s:")

def check(x, input_checks):
        arrq = wn.synsets(input_check)
        y = wn.synsets(x)
        if arrq != [] and y != []:
            return round(arrq[0].lch_similarity(y[0]), 2)
        
        return 0

return_words = [similarity_array[x] for x in range(len(similarity_score)) if similarity_score[x] == max(similarity_score)]
st.write(return_words) 





