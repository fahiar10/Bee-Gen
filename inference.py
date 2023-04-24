from roboflow import Roboflow
import os

def init_api():
    rf = Roboflow(api_key="n6v18JXhied6cfiOF5fr")
    project = rf.workspace().project("bee-gen")
    model = project.version(2).model
    return model

def infer(dirpath,filename,model):
    # rf = Roboflow(api_key="n6v18JXhied6cfiOF5fr")
    # project = rf.workspace().project("bee-gen")
    # model = project.version(2).model

    prediction = model.predict(os.path.join(dirpath,filename))
    print(prediction.json())

    prediction.save(os.path.join("C:/Users/Lenovo/Desktop/Code/FY Proj/gui/inferred_images",filename))

if __name__ == '__main__':
    print('PyCharm')
    infer()