# To see the Streamlit App results in a browser, open an Anaconda Powershell with an ACTIVATED
#environment where streamlit is installed!!!
# 1- Then on CLI do: cd "D:\ANALYTICS - Continuous Education\OpenClassrooms\Projet 7 - Detectez_Bad_Buzz_via_Deep_Learning\tweet_api_prediction_endpoint_via_aws_sam"
# 2- run command: streamlit run post_request_streamlit_model_keras_lstm.py
# 3- Finally Go to local website that will appear

import streamlit as st
import requests

# # THE API ENDPOINT MUST BE ALREADY RUNNING!!!!!!!!
# Declare an EXISTING API ENDPOINT (for example created in FastAPI)
url_of_exisitng_api_endpoint = "http://127.0.0.1:8000/predict"

headers_for_response = {'accept': 'application/json'}
#new_tweet = '{"0":{"1866":7216},"1":{"1866":2724},"2":{"1866":17},"3":{"1866":17},"4":{"1866":225},"5":{"1866":121},"6":{"1866":0},"7":{"1866":0},"8":{"1866":0},"9":{"1866":0},"10":{"1866":0},"11":{"1866":0},"12":{"1866":0},"13":{"1866":0},"14":{"1866":0},"15":{"1866":0},"16":{"1866":0},"17":{"1866":0},"18":{"1866":0},"19":{"1866":0},"20":{"1866":0},"21":{"1866":0},"22":{"1866":0},"23":{"1866":0},"24":{"1866":0},"25":{"1866":0},"26":{"1866":0},"27":{"1866":0},"28":{"1866":0},"29":{"1866":0},"30":{"1866":0},"31":{"1866":0},"32":{"1866":0},"33":{"1866":0},"34":{"1866":0},"35":{"1866":0},"36":{"1866":0},"37":{"1866":0},"38":{"1866":0},"39":{"1866":0},"40":{"1866":0},"41":{"1866":0},"42":{"1866":0},"43":{"1866":0},"44":{"1866":0},"45":{"1866":0},"46":{"1866":0},"47":{"1866":0},"48":{"1866":0},"49":{"1866":0}}'
#query_parameters = {'data_as_json': new_tweet}

# CREATE a Streamlit APPLICATION
def main():
    # Add title and description to Streamlit application
    st.title("Test of an EXISTING API with Streamlit")
    st.write("This Streamlit app tests a local prediction API.")

    # User Input REQUEST (Add a FIELD asking for input into the Streamlit app)
    your_tweet = st.text_input("your tweet?:")

    # Add a button to allow user to SUBMIT his input to the Streamlit app
    if st.button("Submit"):
        #Prepare JSON to sent to the API
        #tweet_as_dict = { "inputed_tweet": your_tweet }

        # Send a POST request to the API
        query_parameters = {'data_as_json': your_tweet}
        response = requests.post(url_of_exisitng_api_endpoint, headers=headers_for_response, params=query_parameters)
        # Show the response in Streamlit app
        st.write("Response:")
        st.write(response.json())

if __name__ == "__main__":
    main()