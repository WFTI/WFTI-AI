import os
import json
import random
import pandas as pd

def main():
    """
    Hyper-parameters
    """
    population_num = 99999

    """
    Load Dummy Items
    """
    print("Read jsons")
    character = readJson("characteristic.json")
    preferences = readJson("preference_list.json")

    """
    Generate Table
    """
    main_columns = ["name", "age", "sex", "residence"]
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
        df = pd.DataFrame(values, columns=columns)

        df_table.append(df, ignore_index=True)

    print("Generate All Population!")

    df_table.to_csv("Population.csv")
    print("Done")
    return

def readJson(fileName):
    with open(os.path.join(os.getcwd(), "DummyData", fileName), "r", encoding='UTF-8') as f:
        data = json.load(f)
    return data

if __name__=="__main__":
    print("START to generate population")
    main()