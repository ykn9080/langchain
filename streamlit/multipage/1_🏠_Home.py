import streamlit as st
import sys

hidemenu = """
<style>
    [data-testid="stSidebarNav"]{
        display:none
    }
</style>
"""

hidesidebar = """
<style>
    [data-testid="stSidebar"]{
        display:none
    }
</style>
"""


def main():
    st.title("💬 Streamlit Tutorial")
    # st.markdown(hidemenu, unsafe_allow_html=True)
    if st.button("Home"):
        st.switch_page("your_app.py")
    if st.button("Page 1"):
        st.switch_page("pages/2_🛠️_Components.py")


if __name__ == "__main__":
    main()
