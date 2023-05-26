

import tensorflow
import json
import pandas as pd
#import uvicorn



model_keras_lstm = tensorflow.keras.models.load_model("model_keras_lstm")

# Check its architecture
#model_keras_lstm.summary()



def lambda_handler(event, context):

    # Make the input JSON into a dictionary
    data = json.loads(event['body'])

    # Make the dictionary into a dataframe
    df = pd.DataFrame.from_dict(data)

    probability = model_keras_lstm.predict(df)
    
    return {'statusCode': 200, 
            'body': json.dumps(
                               {"probability": probability[0][0].item(), }
                              )
          }

 