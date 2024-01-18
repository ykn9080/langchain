from transformers import pipeline

# classifier = pipeline("sentiment-analysis") 
# test=classifier("I've been waiting for a HuggingFace course my whole life.")
# print(test)

# generator=pipeline("text-generation", model="distilgpt2")
# test1=generator("In this course, we will teach you how to", 
#           max_length=30,
#           num_return_sequences=2,
#           )
# print(test1)

# unmasker = pipeline("fill-mask", model="bert-base-uncased") 

# test2=unmasker("Hello I'm a [MASK] model.")
# print(test2)

# ner=pipeline("ner", model="dslim/bert-base-NER", grouped_entities=True)
# test3=ner("My name is Sylvain and I work at Hugging Face in Brooklyn.")
# print(test3)

# question_answerer = pipeline("question-answering")
# test4=question_answerer(
#     question="Where do I work?",
#     context="My name is Sylvain and I work at Hugging Face in Brooklyn"
# )
# print(test4)

# summarizer = pipeline("summarization")
# test5=summarizer("""
#     America has changed dramatically during recent years. Not only has the number of
#     graduates in traditional engineering disciplines such as mechanical, civil, electrical,
#     chemical, and aeronautical engineering declined, but in most of the premier American
#     universities engineering curricula now concentrate on and encourage largely the study
#     of engineering science. As a result, there are declining offerings in engineering
#     subjects dealing with infrastructure, the environment, and related issues, and greater
#     concentration on high technology subjects, largely supporting increasingly complex
#     scientific developments. While the latter is important, it should not be at the expense
#     of more traditional engineering.
#     """)
# print(test5)

translator=pipeline("translation",model="Helsinki-NLP/opus-mt-en-es")
translator1=translator("Hugging Face is a technology company based in New York and Paris", max_length=40)   
print(translator1)