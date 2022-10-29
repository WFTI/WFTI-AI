import os
import json
import pickle
import numpy as np
import pandas as pd

from base import baseClass

class preprocess(baseClass):

    """
    Graph Representation
        edge: person, class 2
        link: class 1
    """

    def __init__(self):
        return

    def __call__(self, preference_list: dict, data: pd.DataFrame):
        
        """ get base information """
        character_info = ["NAME", "AGE", "SEX", "RESIDENCE"]
        all_class2_info = []
        for _, class2_list in preference_list.items():
            all_class2_info.extend(class2_list)

        p = data[data.columns.difference(character_info)].copy()

        # rename columns
        p.columns = all_class2_info
        p = p.applymap(lambda xx: 1 if xx else 0)

        """ represent graph """
        mat_len = len(all_class2_info) + len(data)
        adjacencyM = np.array([[0 for _ in range(mat_len)] for _ in range(mat_len)])

        # upper left
        start_id = 0
        for _, class2_list in preference_list.items():
            end_id = start_id + len(class2_list)

            for row_idx in range(start_id, end_id):
                adjacencyM[row_idx, start_id: row_idx] = 1

            start_id = end_id

        # lower left
        adjacencyM[len(all_class2_info):, :len(all_class2_info)] = p.to_numpy()

        # lower right
        for idx, row in data.iterrows():
            trueFalse = (data.RESIDENCE == row['RESIDENCE']).astype(int)
            adjacencyM[len(all_class2_info) + idx, len(all_class2_info):] = trueFalse.to_numpy()

        # duplicate along diagonal
        for i in range(mat_len):
            for j in range(i, mat_len):
                adjacencyM[i][j] = 1 if i == j else adjacencyM[j][i]

        return adjacencyM

if __name__=='__main__':
    with open(os.path.join(os.getcwd(), 'DummyData', 'Population.pkl'), 'rb') as f: 
        data = pickle.load(f)

    with open(os.path.join(os.getcwd(), 'DummyData', 'preference_list.json'), 'r') as f:
        pref = json.load(f)
    
    pp = preprocess()
    M = pp(pref, data)

    df = pd.DataFrame(M, columns=[idx for idx in range(len(M))])
    df.to_csv(os.path.join(os.getcwd(), 'DummyData', 'adjacencyM.csv'))