import os

import rasa

from config import my_config

os.environ['CUDA_VISIBLE_DEVICES'] = my_config.depend['rasa_run_cuda']
# MODEL_PATH = "models/" + my_config.depend['rasa_run_model']
MODEL_PATH = "models/"

rasa.run(
    model=MODEL_PATH,
    endpoints="config/endpoints.yml",
    credentials="config/credentials.yml"
)
