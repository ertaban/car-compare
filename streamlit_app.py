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
# Function to get AI response
def get_ai_response(prompt):
    try:
        # Using a different Hugging Face model that's more likely to be available
        API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
        headers = {"Content-Type": "application/json"}
        payload = {
            "inputs": prompt,
            "parameters": {
                "max_length": 100,
                "min_length": 30,
                "do_sample": True
            }
        }
        
        response = requests.post(API_URL, headers=headers, json=payload)
        
        if response.status_code == 200:
            # BART is a summarization model, it returns a different JSON structure
            return response.json()[0]["summary_text"]
        else:
            # If the first model fails, try a backup model
            backup_url = "https://api-inference.huggingface.co/models/google/flan-t5-small"
            backup_payload = {"inputs": prompt}
            backup_response = requests.post(backup_url, headers=headers, json=backup_payload)
            
            if backup_response.status_code == 200:
                return backup_response.json()[0]["generated_text"]
            else:
                return f"Error getting response (Status: {response.status_code}). Please try again."
    except Exception as e:
        return f"Something went wrong: {str(e)}. Please try again."

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
