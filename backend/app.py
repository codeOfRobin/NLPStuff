from flask import Flask,request,Response,json
from flask.ext.cors import CORS
from spacy.en import English
from scipy.stats import norm
import math
import scipy
pipeline = English()

app = Flask(__name__)
CORS(app)
@app.route("/", methods=['POST'])
def hello():
    tokens = pipeline(request.form['line'])
    headAndToken = [(token.idx,token.head.idx) for ind, token in enumerate(tokens)]
    totalScore = sum([abs(tokenIndex-tokenHeadIndex) for tokenIndex,tokenHeadIndex in headAndToken])
    totalScore = totalScore/len(request.form['line'])
    print(totalScore)
    z_score = (totalScore - 2.541)/(0.578)
    print(z_score)
    p_value = scipy.stats.norm.sf(abs(z_score))*2
    print(p_value)
    data = {
    "line" : request.form['line'],
    "score": p_value
    }
    js = json.dumps(data)
    resp = Response(js, status=200, mimetype='application/json')

    return resp

if __name__ == "__main__":
    app.run(debug=True)
