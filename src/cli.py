import inquirer


def askForLanguage():
    while True:
        language = input('Choose a language supported: Javascript || Typescript: ')
        if language.lower() == 'javascript' or language.lower() == 'typescript':
            return language.capitalize()
        else:
            print("Invalid choice. Please enter 'Javascript' or 'Typescript'.")

def askForModelNames():
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

def askForAttributes(models):
    model_attributes = []

    for model in models:
        print(f"\nEnter attributes for model: {model}")
        print('If you want a reference to another collection, you can write for example: userId: ref_to_users')
        attributes = []
        while True:
            questions = [
                inquirer.Text('attr', message="Enter attribute or press Enter to finish")
            ]
            answers = inquirer.prompt(questions)
            attr = answers['attr'].strip()
            if not attr:
                break
            attributes.append(attr)

        model_attributes.append({
            "model": model,
            "attributes": attributes
        })

    return model_attributes

