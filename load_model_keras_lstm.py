
import uvicorn
import tensorflow


model_keras_lstm = tensorflow.keras.models.load_model("model_keras_lstm")

# Check its architecture
#model_keras_lstm.summary()

