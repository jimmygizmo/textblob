from flask import Flask, jsonify
from textblob import TextBlob


# https://www.linode.com/docs/guides/create-restful-api-using-python-and-flask/

app = Flask(__name__)

in_memory_datastore = {
   "COBOL": {"name": "COBOL", "publication_year": 1960, "contribution": "record data"},
   "ALGOL": {"name": "ALGOL", "publication_year": 1958, "contribution": "scoping and nested functions"},
   "APL": {"name": "APL", "publication_year": 1962, "contribution": "array processing"},
}


@app.get('/programming_languages')
def list_programming_languages():
    return {"programming_languages": list(in_memory_datastore.values())}


@app.route('/programming_languages/<programming_language_name>')
def get_programming_language(programming_language_name):
    return in_memory_datastore[programming_language_name]


def package_textblob(onevzn):
    tb = TextBlob(onevzn['vzn_text'])
    return jsonify({
        'vzn_name': onevzn['vzn_name'],
        'tb_text': onevzn['vzn_text'],
        'tb_sentiment': tb.sentiment,
        'tb_tags': tb.tags,
        'noun_phrases': tb.noun_phrases
    })


@app.route('/textblob/<vocalization_text>')
def get_textblob(vocalization_text):
    print(f"\n\n{vocalization_text}\n")
    # Handle cleaning, en/de-coding and any pre-processing here.
    # Will need to test and figure out what is needed. This is a security risk area if this is in any way called
    # from anonymous web or even authenticated user input. It is planned as an internal API but still, it must
    # be cleansed and made safe before going past this point here.
    request_vzn = {"vzn_name": "rest-call", "vzn_text": vocalization_text}
    return package_textblob(request_vzn)


# @app.route("/blob", methods=["POST"])
# def set_name():
#     if request.method == 'POST':
#         posted_data = request.get_json()
#         data = posted_data['data']
#         return jsonify(str("Successfully stored  " + str(data)))

