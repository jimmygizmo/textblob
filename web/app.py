from flask import Flask
# from flask import Flask, jsonify, request

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


# @app.route("/blob", methods=["POST"])
# def set_name():
#     if request.method == 'POST':
#         posted_data = request.get_json()
#         data = posted_data['data']
#         return jsonify(str("Successfully stored  " + str(data)))

