import json
from datetime import datetime
# from .SendMessage import SendMessage


def AddDisease(disease):
    now = datetime.now()
    hour = now.strftime("%H")
    minute = now.strftime("%M")
    diseases_list = []

    try:
        with open('./data/health.json', 'r') as file:
            data = json.load(file)

        data['disease'] = disease

        with open('./data/disease.json', 'r') as file:
            disease_data = json.load(file)
            diseases = disease_data['disease']

            for _ in diseases:
                diseases_list.append(_)

            if disease not in diseases_list:
                # print(disease)
                # Enter your phone number
                SendMessage(phone_number='', message='You have been diagnosed with ' +
                            disease + '.', hour=hour, minute=minute)

        with open('./data/health.json', 'w') as file:
            json.dump(data, file, indent=4)

    except Exception as e:
        print(e)


def RemoveDisease():
    try:
        with open('./data/health.json', 'r') as file:
            data = json.load(file)

        data['disease'] = ""

        with open('./data/health.json', 'w') as file:
            json.dump(data, file, indent=4)

    except Exception as e:
        print(e)
