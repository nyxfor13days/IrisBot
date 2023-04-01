import json


def AddDiet(current_time, food):
    diet = {
        'time': current_time,
        'food': food
    }

    try:
        with open('./data/diet.json', 'r+') as file:
            data = json.load(file)
            data['diet'].append(diet)
            file.seek(0)
            json.dump(data, file, indent=4)

    except Exception as e:
        print(e)
