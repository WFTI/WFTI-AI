import os
import json
import random
import pickle
import pandas as pd

def main():
    path = os.path.join(os.getcwd(), "DummyData")
    """
    Hyper-parameters
    """
    population_num = 10

    """
    Load Dummy Items
    """
    print("Read jsons")
    character = readJson(path, "characteristic.json")
    preferences = readJson(path, "preference_list.json")

    """
    Generate Table
    """
    main_columns = ["NAME", "AGE", "SEX", "RESIDENCE"]
    sub_columns = []
    for class_1, class_2 in preferences.items():
        for item in class_2:
            sub_columns.append("{}_{}".format(class_1, item))

    df_table = pd.DataFrame()
    for idx in range(population_num):
        print("generate {}/{}..".format(idx, population_num), end='\r')

        name = random.choice(character['NAME']['last']) + random.choice(character['NAME']['first'])
        age = random.randrange(20, 60)
        sex = random.choice(['Male', 'Female'])
        residence = random.choice(character['RESIDENCE'])
        prefer = [random.randrange(0, 6) for _ in range(len(sub_columns))]

        values = [name, age, sex, residence] + prefer
        columns = main_columns + sub_columns

        if len(values) != len(columns):
            raise ValueError("columns({}) != values({})".format(len(columns), len(values)))
        df = pd.DataFrame([values], columns=columns)

        df_table = pd.concat([df_table, df], ignore_index=True)

    print("Generate All Population!")

    with open(os.path.join(path, "Population.pkl"), 'wb') as f:
        pickle.dump(df_table, f)

    print("Done")
    return

def readJson(path, fileName):
    with open(os.path.join(path, fileName), "r", encoding='UTF-8') as f:
        data = json.load(f)
    return data

if __name__=="__main__":
    print("START to generate population")
    main()