from channels import Group
from .behavior_setting import behavior_chat_group_name,LOCK_MESSAGE
import json
from sklearn.externals import joblib
from queue import Queue,Empty
import numpy as np
from .preprocessing import GestureFeatureExtractor


model_path = "behavior_model.pkl"
scaler_path = "behavior_scaler.pkl"

extractor = GestureFeatureExtractor()
clf = joblib.load(model_path)
scaler = joblib.load(scaler_path)

result_queue = Queue()

def authenticate(slide_json):
    slide = json.loads(slide_json)
    feature = extractor.extract(slide)
    feature = scaler.transform(np.array([feature]))
    return clf.predict(feature)[0]


def be_connect(message):
    message.reply_channel.send({'accept':True})
    Group(behavior_chat_group_name).add(message.reply_channel)


def be_message(message):
    content = message['text']
    print(content)
    result = authenticate(content)
    print(result)
    if result == 1:
        try:
            result_queue.get_nowait()    
        except Empty:
            pass
    elif result == -1:
        count = result_queue.qsize()
        result_queue.put_nowait(1)
        if count + 1 >= 2:
            while True:
                try:
                    result_queue.get_nowait()
                except Empty:
                    break
            lock() 

        

def be_disconnect(message):
    Group(behavior_chat_group_name).discard(message.reply_channel)

def lock():
    Group(behavior_chat_group_name).send({"text":LOCK_MESSAGE})