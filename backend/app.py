from flask import Flask,request
from flask.ext.cors import CORS
from spacy.en import English
pipeline = English()

app = Flask(__name__)
CORS(app)
@app.route("/", methods=['POST'])
def hello():
    print(request)
    tokens = pipeline(request.form['line'])
    headAndToken = [(token.idx,token.head.idx) for ind, token in enumerate(tokens)]
    totalScore = sum([abs(tokenIndex-tokenHeadIndex) for tokenIndex,tokenHeadIndex in headAndToken])
    totalScore = totalScore/len(request.form['line'])
    return str(totalScore)

if __name__ == "__main__":
    app.run(debug=True)
