# let us have a look how to put something into production
import streamlit as st

def main():
    st.header("Hello World")
    if st.button("Click here: "):
        st.markdown("This belongs to the app!")


if __name__ == "__main__":
    main()