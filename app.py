import os
from dotenv import load_dotenv, find_dotenv
import openai
import gradio as gr

_ = load_dotenv(find_dotenv()) # read local .env file
openai.api_key  = os.environ['OPENAI_API_KEY']

def get_completion_from_messages(messages, 
                                 model="gpt-3.5-turbo", 
                                 temperature=0, 
                                 max_tokens=500):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, 
        max_tokens=max_tokens,
    )
    return response.choices[0].message["content"]

def predict(prompt):

    delimiter = "####"
    
    system_message = f"""
    Act as a professional medical coder, you will provide all possible ICD-10 codes based on the clinical notes. 
    list as many codes as possible.
    list all the possible ICD-10 codes and their descriptions, nothing else. 
    The doctor's clinical note will be delimited with {delimiter} characters.
    """
    
    user_message = f"""\
                  {prompt}
                  """
    
    messages =  [  
        {'role':'system', 
         'content': system_message},    
          {'role':'user', 
           'content': f"{delimiter}{user_message}{delimiter}"},
    ]
 
    completion = get_completion_from_messages(messages)
    return completion

# print(predict("Patient presents with pain and swelling in the right knee."))

title = "ICD-10 Diagnosis Codes Suggestion for Clinical Note"
description = """
OpenAI GPT powered ICD-10 codes for medical coding and billing!
"""

textbox = gr.Textbox(label="Type your clinical note here:", 
                     placeholder="Example: Patient presents with a cough, fever, and shortness of breath.", 
                     lines=15)
suggested_icd = gr.Textbox(label="ICD-10 codes will appear here once you hit ENTER, or click on Submit button", 
                     lines=15)

examples = [["Patient presents with a cough, fever, and shortness of breath."], 
            ["Patient presents with a cough, fever, and shortness of breath. Chest X-ray shows bilateral pneumonia."], 
            ["Patient with a history of type 2 diabetes presents with new-onset blurry vision."],
            ["Patient with a history of type 2 diabetes presents with new-onset blurry vision. Eye examination consistent with diabetic retinopathy."],
            ["65-year-old female presents with memory loss and disorientation. "],
            ["65-year-old female presents with memory loss and disorientation. Clinical findings consistent with Alzheimer’s disease."],
            ["45-year-old female presents with persistent abdominal pain in the right upper quadrant, nausea, and vomiting."],
            ["45-year-old female presents with persistent abdominal pain in the right upper quadrant, nausea, and vomiting. Ultrasound shows gallstones."]]

gr.Interface(
    fn=predict,
    inputs=textbox,
    outputs=suggested_icd,
    title=title,
    description=description,
    examples=examples
    ).launch()