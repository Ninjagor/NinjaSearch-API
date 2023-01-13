from flask import Flask
import googlesearch_py
from flask_cors import CORS

app = Flask(__name__)
CORS(app)



def returnSearch(query):
  results = googlesearch_py.search(query)
  print(results)
  return results

# returnSearch('hi')


@app.route('/search/<string:query>')
def home(query):
  try:
    return returnSearch(query)
  except:
    return "An Error Has Occured. Please Try Again."

@app.route('/test')
def test():
    return "test"
  
if __name__ == "__main__":
  app.run(debug=True, port=8080)