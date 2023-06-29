# ICD-10 Diagnosis Codes Suggestion for Clinical Note
#### © 2023 Xinjie Qiu ℠

This application uses OpenAI's GPT to suggest ICD-10 codes based on the input clinical notes. It acts as a 
professional medical coder providing as many possible ICD-10 codes based on the given clinical notes.

## App Usage
- **Input**: Users can input a wide variety of clinical notes.
- **Code Extraction**: The application uses OpenAI's GPT model's zero-short learning capability to extract 
all possible relevant ICD-10 codes from the provided clinical notes.
- **Output**: It display the generated ICD-10 codes instantly upon hitting ENTER or clicking on the Submit button.

## Installation

To install this app:

Clone this repository:
```bash
git clone https://github.com/tjphoton/ICD_code_gen.git
```

Navigate into the cloned repository:

```bash
cd icd10-codes-suggestion
```

Create a virtual environment and install the required packages:

```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Set up your OpenAI API key in a .env file in the root directory of the cloned repository. The file should look like this:
```bash
OPENAI_API_KEY=your-openai-api-key
```

Run the app:

```bash
gradio app.py
```
A browser window should open displaying the app.

## Usage
To use the ICD-10 Diagnosis Codes Suggestion for Clinical Note: 
Type in your clinical note in the provided textbox.
Hit ENTER or click on the Submit button. The ICD-10 codes will appear in the output textbox below.
The application also provides examples of clinical notes for you to try. 
Click on one of the examples and see the corresponding ICD-10 codes generated.

**Please note that the application should be used for reference purposes only. 
Always consult with a professional coder or practitioner when dealing with medical coding.**