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
# Function to get AI response
def get_ai_response(prompt):
    try:
        # Using the free Hugging Face Inference API with a public model
        API_URL = "https://api-inference.huggingface.co/models/gpt2"
        headers = {"Content-Type": "application/json"}
        payload = {"inputs": prompt, "parameters": {"max_length": 100, "return_full_text": False}}
        
        response = requests.post(API_URL, headers=headers, json=payload)
        
        if response.status_code == 200:
            return response.json()[0]["generated_text"]
        else:
            # Handle API errors gracefully
            if response.status_code == 503:
                return "The AI model is currently loading. Please try again in a moment."
            else:
                return f"Error getting response. Please try again."
    except Exception as e:
        return f"Something went wrong. Please try again."

# Save button (same as before, but now gets AI response)
if st.button("Save"):
    if user_input:
        with st.spinner("Getting AI response..."):
            # Get response from AI
            ai_response = get_ai_response(user_input)
            
            # Display the AI response in the output area
            st.write("Your saved text:")
            st.write(ai_response)
    else:
        st.write("Please enter some text first.")
