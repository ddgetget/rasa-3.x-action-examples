import os

from rasa_sdk.endpoint import run

from config import my_config

os.environ['CUDA_VISIBLE_DEVICES'] = my_config.depend['rasa_action_cuda']
run(
    action_package_name="actions",
    port=5055
)
