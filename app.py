from sklearn.linear_model import LogisticRegression
import pickle

model = pickle.load(open('model.pkl','rb'))

def classify(num):
    if num<1:
        return 'negative'
    else:
        return 'positive'
import gradio as gr
import numpy as np
def predict_diabetes(preg,glu,bp,st,ins,bmi,dpf,age):
    input_array=np.array([[preg,glu,bp,st,ins,bmi,dpf,age]])
    pred=model.predict(input_array)
    output=classify(pred[0])
    if output=='negative':
      return [(0,output)]
    else:
      return [(1,output)]
preg = gr.inputs.Slider(minimum=0, maximum=17, default=2, label="Pregnancy")
glu = gr.inputs.Slider(minimum=0, maximum=199, default=2, label="glucose")
bp = gr.inputs.Slider(minimum=0, maximum=122, default=2, label="blood prussure")
st = gr.inputs.Slider(minimum=0, maximum=99, default=2, label="skin thickness")
ins = gr.inputs.Slider(minimum=0, maximum=846, default=2, label="insulin")
bmi = gr.inputs.Slider(minimum=0, maximum=67.1, default=2, label="bmi")
dpf = gr.inputs.Slider(minimum=0, maximum=2.5, default=2, label="diabetes pedigree function")
age = gr.inputs.Slider(minimum=20, maximum=100, default=2, label="age")


op=gr.outputs.HighlightedText(color_map={ "negative": "green",
        "positive": "red",})

gr.Interface(predict_diabetes, inputs=[preg,glu,bp,st,ins,bmi,dpf,age], outputs=op,live=True).launch()
