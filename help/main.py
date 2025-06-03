
def showHelp():
    print('for better experience to generate express models with js or ts, follow this steps')

    steps = [
        "name models like for example like this: user | product | message ...,",
        "for types you can write attribute like this for ex.: username:string,required,unique...",
        "for references to other collection, you can write attribute like this for ex.: userId:ref_to_users",
        "for an attribute that can be an object write it like this : education:{school,city...}",
    ]

    for step in steps:
        print(f'====> {step}')