import inquirer

def ask_language():
    questions = [
        inquirer.List('language',
                      message="Choose language",
                      choices=['JavaScript', 'TypeScript'])
    ]
    answers = inquirer.prompt(questions)
    return answers['language']

def ask_model_name():
    questions = [
        inquirer.Text('model_name', message="Enter model name")
    ]
    answers = inquirer.prompt(questions)
    return answers['model_name']

def ask_attributes():
    attributes = []
    while True:
        questions = [
            inquirer.Text('attr', message="Enter attribute (name:type) or leave blank to finish")
        ]
        answers = inquirer.prompt(questions)
        attr = answers['attr']
        if not attr:
            break
        if ':' not in attr:
            print("Invalid format, use name:type (e.g., email:String)")
            continue
        attributes.append(attr)
    return attributes

def main():
    language = ask_language()
    model_name = ask_model_name()
    attributes = ask_attributes()
    print(f"Language: {language}")
    print(f"Model: {model_name}")
    print(f"Attributes: {attributes}")
    return language, model_name, attributes

if __name__ == "__main__":
    main()
