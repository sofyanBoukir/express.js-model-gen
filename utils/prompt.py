def promptToAi(language, model_attributes):
    prompt = f"Generate an Express {language} model with this attributes {model_attributes} add the validation for each attribute based on your DATA, \n Please only provide the code without explanation."
    return prompt