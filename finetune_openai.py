from config import getOpenai
from openai import OpenAI

getOpenai()
client = OpenAI()

# Upload the file to OpenAI => file_id 획득

"""
with open("./data/finetune_data.jsonl", "rb") as file_data:

    upload_response = client.files.create(
    file=file_data,
    purpose='fine-tune'
    )
    
    file_id = upload_response.id
    print(f"File uploaded successfully. ID: {file_id}")
"""

# fine-tuning job을 실행함 => 온라인에서 확인가능 => model_id 획득
"""
client.FineTuningJob.create(training_file="file-NHmo4FQx1R4e5PrlbBizLnDd",model="gpt-3.5-turbo")
"""

# fine-tuning 결과 모델에 채팅 메시지를 보내서 답변을 받음
model_id="ft:gpt-3.5-turbo-0125:personal::8zcYGtZ3"
completion = client.chat.completions.create(
    model = model_id ,
    messages = [
        {"role":"system", "content":"Kakao Friends Assistant Bot"},
        # {"role":"user","content":"Who is chunshik in Kakao Friends"}        
        {"role":"user","content":"카카오 프랜즈에서 춘식이가 누구인가?"}
    ]
)

print(completion.choices[0].message.content)