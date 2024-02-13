import streamlit as st

# counter = 0
# st.write("Counter:", counter)
# if st.button("up"):
#     counter = counter + 1
#     st.write("Counter:", counter)

main_container = st.container()

if "counter" not in st.session_state:
    st.session_state.counter = 0
    st.write("Counter:", st.session_state.counter)

if st.button("up"):
    st.session_state.counter += 1
    main_container.write("Counter:", st.session_state.counter)
if st.button("reset"):
    st.session_state.counter = 0
    st.write("Counter:", st.session_state.counter)
