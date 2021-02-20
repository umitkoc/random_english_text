from bs4 import BeautifulSoup as bs
from requests import get
from flask import Flask


def Text():
    url="https://randomword.com/paragraph"
    req=get(url)
    html=req.content
    soup=bs(html,'html.parser')
    return soup.find("div",{"id":"random_word_definition"}).text

app=Flask(__name__)
app.config['Debug']=False
@app.route('/',methods=['Get'])
def Home():
    return Text()

if __name__=="__main__":
    app.run()




