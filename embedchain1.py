from embedchain import App
from config import gethuggingface

gethuggingface()

app = App.from_config("yaml/mistral.yaml")
# app.reset()
app.add("https://www.forbes.com/profile/elon-musk")
app.add("https://en.wikipedia.org/wiki/Elon_Musk")
print(app.query("What is the net worth of Elon Musk today?"))
print(app.evaluate("what is the net worth of Elon Musk?"))
