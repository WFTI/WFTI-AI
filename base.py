import os
import json
import torch
import pickle
import numpy as np

from abc import *

class baseClass(metaclass=ABCMeta):

    @abstractmethod
    def __init__():
        pass

    def _read_(self, filePath: str):

        if filePath.endswith('.json'):
            with open(filePath, 'r') as f:
                data = json.load(f)

        elif filePath.endswith('.pickle') or filePath.endswith('.pkl'):
            with open(filePath, 'rb') as f:
                data = pickle.load(f)

        elif filePath.endswith('.npy'):
            data = np.load(filePath)

        elif filePath.endswith('.pt'):
            data = torch.load(filePath)

        else:
            raise ValueError("{} is not defined file type".format(filePath.split('.')[-1]))

        return data

    def _write_(self, filePath: str, data):

        if filePath.endswith('.json'):
            with open(filePath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent="\t", ensure_ascii=False)

        elif filePath.endswith('.pickle') or filePath.endswith('.pkl'):
            with open(filePath, 'wb') as f:
                pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)

        elif filePath.endswith('.npy'):
            np.save(filePath, data)

        elif filePath.endswith('.pt'):
            torch.save(data, filePath)

        else:
            raise KeyError("{} is not defined file type".format(filePath.split('.')[-1]))
            
        return