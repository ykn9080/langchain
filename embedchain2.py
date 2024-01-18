from embedchain import App
from apikey import getOpenai

getOpenai()

app = App()
app.add("https://www.forbes.com/profile/elon-musk")
app.add("https://en.wikipedia.org/wiki/Elon_Musk")
print(app.query("What is the net worth of Elon Musk today?"))