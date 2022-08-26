import os

import rasa

from config import my_config

os.environ['CUDA_VISIBLE_DEVICES'] = my_config.depend['rasa_run_cuda']

rasa.train(
    domain="config/domain.yml",
    config="config/config.yml",
    training_files="train_data",
)
