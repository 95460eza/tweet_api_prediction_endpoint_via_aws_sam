
# THE API ENDPOINT MUST BE ALREADY RUNNING!!!!!!!!!!!!!

import requests

url = "http://127.0.0.1:8000/predict"

headers_for_response = {'accept': 'application/json'}

new_tweet = '{"0":{"1866":7216},"1":{"1866":2724},"2":{"1866":17},"3":{"1866":17},"4":{"1866":225},"5":{"1866":121},"6":{"1866":0},"7":{"1866":0},"8":{"1866":0},"9":{"1866":0},"10":{"1866":0},"11":{"1866":0},"12":{"1866":0},"13":{"1866":0},"14":{"1866":0},"15":{"1866":0},"16":{"1866":0},"17":{"1866":0},"18":{"1866":0},"19":{"1866":0},"20":{"1866":0},"21":{"1866":0},"22":{"1866":0},"23":{"1866":0},"24":{"1866":0},"25":{"1866":0},"26":{"1866":0},"27":{"1866":0},"28":{"1866":0},"29":{"1866":0},"30":{"1866":0},"31":{"1866":0},"32":{"1866":0},"33":{"1866":0},"34":{"1866":0},"35":{"1866":0},"36":{"1866":0},"37":{"1866":0},"38":{"1866":0},"39":{"1866":0},"40":{"1866":0},"41":{"1866":0},"42":{"1866":0},"43":{"1866":0},"44":{"1866":0},"45":{"1866":0},"46":{"1866":0},"47":{"1866":0},"48":{"1866":0},"49":{"1866":0}}'

# When making a POST request, you can specify query parameters by appending them to the URL of the request.
# Query parameters are key-value pairs that are used to provide additional information or data to the server.
query_parameters = {'data_as_json': new_tweet}


response = requests.post(url, headers=headers_for_response, params=query_parameters)
print(response.content)











