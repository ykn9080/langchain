import streamlit as st

# hidemenu = """
# <style>
#     [data-testid="stSidebarNav"]{
#         display:none
#     }
# </style>
# """

# hidesidebar = """
# <style>
#     [data-testid="stSidebar"]{
#         display:none
#     }
# </style>
# """


def main():
    st.title("💬 Streamlit Tutorial")
    # st.markdown(hidemenu, unsafe_allow_html=True)
    if st.button("Components"):
        st.switch_page("pages/2_🛠️_Components.py")


if __name__ == "__main__":
    main()
