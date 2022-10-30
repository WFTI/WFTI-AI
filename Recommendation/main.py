import os
import json
import argparse
import pandas as pd

from gnn import GNN

class argparser(object):

    def __init__(self):
        # process type
        self.pType: str = 'train'

        # train parameter
        self.epoch: int = 100
        self.batch: int = 8

        self.lrn_rate: float = 1e-4

        # model parameter
        return

    def make_args(self):
        parser = argparse.ArgumentParser()
        for attribute, default in self.__dict__.items():
            parser_str = '--{}'.format(str(attribute))
            parser.add_argument(parser_str, type=type(default), default=default)
        args = parser.parse_args()
        return args

def main():
    print("========== START AI ==========")

    parser = argparser()
    args = parser.make_args()

    print("Run type: {}".format(args.pType))

    if args.pType == 'train':
        pass
    elif args.pType == 'infer':
        pass
    else:
        raise ValueError("'{}' is not supported processing type".format(args.pType))

    print("=========== END AI ===========")
    return

if __name__=='__main__':
    main()