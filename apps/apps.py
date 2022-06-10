from django.apps import AppConfig
from tensorflow import keras


class AppsConfig(AppConfig):
    model = keras.models.load_model('./apps/static/model')
    #model_result = model.predict()
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps'
