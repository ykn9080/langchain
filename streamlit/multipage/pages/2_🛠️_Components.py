import streamlit as st
import sys


def main():
    st.title("🛠️ Components Collections")
    st.header("Button")
    st.write("버튼 클릭시 메시지 출력")
    button1 = st.button("Button1")
    if button1:
        st.write("버튼을 클릭하셨습니다.")
    st.header("Checkbox section")
    like = st.checkbox("Like")
    button2 = st.button("Submit")
    if button2:
        if like:
            st.write("You liked the chatbot")
        else:
            st.write("You didn't like the chatbot")

    st.header("radiobtn section")
    animal = st.radio("which animal?", ("Dog", "Cat", "Rabbit"))
    button3 = st.button("Submit animal")
    if button3:
        switch = {
            "Dog": "Woof",
            "Cat": "Meow",
            "Rabbit": "Squeak"
        }
        st.write(animal, " cries ", switch[animal])

    st.header("Selectbox section")
    animal = st.selectbox("which animal?", ("Dog", "Cat", "Rabbit"))
    button4 = st.button("Submit animal2")
    if button4:
        switch = {
            "Dog": "Woof",
            "Cat": "Meow",
            "Rabbit": "Squeak"
        }
        st.write(animal, " cries ", switch[animal])

    st.header("MultiSelectbox section")
    animals = st.multiselect("which animal?", ["Dog", "Cat", "Rabbit"])
    button5 = st.button("Print Animals")
    if button5:
        st.write("I like ", animals)

    st.header("Slider section")
    epochs = st.slider("Number of epochs", 1, 100, 10)
    if st.button("Train"):
        st.write(f"Training for {epochs} epochs")

    st.header("TextInputr section")
    usertext = st.text_input("Enter your text")
    if st.button("Text Button"):
        st.write(f"your input is {usertext} ")

    st.header("NumberInputr section")
    usernumber = st.number_input("Enter your text")
    if st.button("Number Button"):
        st.write(f"your input is {usernumber} ")

    st.header("Text_area section")

    def run_sentiment_analysis(txt):
        return "positive" if "best" in txt else "negative"

    txt = st.text_area("Enter your text", """ It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only.""", height=300)
    st.write('Sentiment:', run_sentiment_analysis(txt))

    st.header("Tab section")
    tab1,tab2=st.tabs(["chart","table"])
    with tab1:
        st.write("chart")
    with tab2:
        st.write("table")
        
if __name__ == "__main__":
    sys.exit(main())
