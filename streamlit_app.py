import streamlit as st

st.title("🎈 Cihangir's app")
st.write(
    "This is the start of the new app!"
)

# App title
st.title("Simple Input-Output App")

# Input field
user_input = st.text_input("Enter your text here:")

# Save button
if st.button("Save"):
    # Display the input in the output area
    st.write("Your saved text:")
    st.write(user_input)
