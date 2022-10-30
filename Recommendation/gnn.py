from turtle import forward
import torch
import torch.nn as nn

class EMBEDDER(nn.Module):

    def __init__(self, param: dict) -> None:
        super(EMBEDDER, self).__init__()

        categ_num = param['categ_num']
        embed_dim = param['embed_dim']

        self.embedder = nn.Embedding(categ_num, embed_dim)
        return

    def forward(self):
        return

class PROJECTOR(nn.Module):

    def __init__(self, param: dict) -> None:
        super(PROJECTOR, self).__init__()

        prefr_num = param['prefr_num']
        embed_dim = param['embed_dim']

        
        return

    def forward(self):
        return

class GNN(nn.Module):

    def __init__(self, param: dict) -> None:
        super(GNN, self).__init__()
        return

    def forward(self):
        return