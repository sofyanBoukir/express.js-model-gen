import inquirer
import developer


print(developer.developer())

def ask_language():
    questions = [
        inquirer.List('language',
                      message="Choose language",
                      choices=['JavaScript', 'TypeScript'])
    ]
    answers = inquirer.prompt(questions)
    return answers['language']

def ask_model_names():
    model_names = []
    print('Enter model name for each one >>>>')
    while True:
        questions = [
            inquirer.Text('model_name', message="Enter model name (leave blank to finish)")
        ]
        answers = inquirer.prompt(questions)
        name = answers['model_name'].strip()
        if not name:
            break
        model_names.append(name)
    return model_names


def ask_attributes(models):
    model_attributes = {}

    for model in models:
        print(f"\nEnter attributes for model: {model}")
        print('if you want a reference to other collection you can write: userId: ref_to_users')
        attributes = []
        while True:
            questions = [
                inquirer.Text('attr', message="Enter attribute (name:type) or leave blank to finish")
            ]
            answers = inquirer.prompt(questions)
            attr = answers['attr'].strip()
            if not attr:
                break
            if ':' not in attr:
                print("Invalid format, use name:type (e.g., email:String)")
                continue
            attributes.append(attr)
        model_attributes[model] = attributes

    return model_attributes


def main():
    language = ask_language()
    model_names = ask_model_names()
    model_attributes = ask_attributes(model_names)
    print(f"Language: {language}")
    print(f"Models: {model_names}")
    print("Model Attributes:")
    for model, attrs in model_attributes.items():
        print(f"  {model}: {attrs}")

    return language, model_names, model_attributes


if __name__ == "__main__":
    main()
