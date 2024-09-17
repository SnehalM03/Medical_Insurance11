
import os

PATH = os.path.dirname(os.path.abspath(__file__))


FLASK_PORT_NUMBER = 8080

MODEL_FILE_NAME = os.path.join(PATH, "artifacts", "Linear_reg_model.pkl")
COLUMN_DATA = os.path.join(PATH, "artifacts", "column_data")