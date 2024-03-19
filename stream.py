# Import the Streamlit library
import streamlit as st

# Define the main function
def main():
  # Set the title of the app
  st.title("Welcome to My Streamlit App!")

  # Display a welcome message
  st.write("Hello, welcome to my Streamlit app!")

  # Create a button
  if st.button('Say Hello'):
    # Display a message when the button is clicked
    st.write("Hello, Streamlit!")

# Run the main function
if __name__ == '__main__':
  main()