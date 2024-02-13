import streamlit as st
import spacy


@st.cache_data()
def load_spacy_model(model_name):
    nlp = spacy.load(model_name)
    return nlp


nlp = load_spacy_model("en_core_web_sm")
# nlp = spacy.load('en_core_web_md')
text = 'Yuh-jung Youn won the Oscar for best supporting actress for her performance in "Minari" on Sunday and made history by becoming the first Korean actor to win an Academy Award.'
# doc = nlp(text)
# tokenized = list(doc)
# print(tokenized)


def extract_entities(ent_types, text):
    results = []
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ in ent_types:
            # st.write(f"{ent.text} ({ent.label_})")
            results.append((ent.text, ent.label_))
    return results


st.title("Forms in Streamlit")

form1 = st.sidebar.form(key='form1')

form1.header("Params")
ent_types = form1.multiselect("Entity Types", ["PERSON", "ORG", "GPE", "DATE", "TIME", "MONEY",
                                               "PERCENT", "FAC", "PRODUCT", "EVENT", "WORK_OF_ART", "LAW", "LANGUAGE"], ["PERSON", "ORG"])

text = st.text_area("Enter Text", text)
if form1.form_submit_button("Click me"):
    hits = extract_entities(ent_types, text)
    st.write(hits)

# if __name__ == "__main__":
#     print(extract_entities(['PERSON', 'ORG'], text))
