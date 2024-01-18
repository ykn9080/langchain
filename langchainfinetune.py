import apikey
from openai import OpenAI

apikey.getOpenai()

client = OpenAI()

# rtn=client.files.create(
#   file=open("data/chatbot.jsonl", "rb"),
#   purpose="fine-tune"
# )
# print(rtn)
# client.fine_tuning.jobs.create(
#     training_file="file-4ppzMmiPN0SswscpY0PGZz0G",
#      model="gpt-3.5-turbo"
# )
# list=client.fine_tuning.jobs.list()

# job=client.fine_tuning.jobs.retrieve("ftjob-zKrBu0GgSjnISSbi9xd16Oza")
# print(job)
response = client.chat.completions.create(
  model="ft:gpt-3.5-turbo-0613:personal::8bN3GrMM",
  messages=[
    {"role": "system", "content": "Marv is a factual chatbot that is also sarcastic."},
    {"role": "user", "content": "What's the capital of Korea?"}
  ]
)
response1 = client.chat.completions.create(
  model="ft:gpt-3.5-turbo-0613:personal::8bN3GrMM",
  messages=[
    {"role": "system", "content": "You are a helpful chatbot."},
    {"role": "user", "content": "What's the capital of Korea?"}
  ]
)
print(response.choices[0].message.content)
print(response1.choices[0].message.content)
