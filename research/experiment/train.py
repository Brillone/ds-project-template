# base
from labs import experiment_path
import json
import argparse

# internal
from research.experiment.modeling import *
from research.experiment.setting import *
from research.utils.data_handling import *
from research.utils.evaluation import *


def experiment(experiment_params, artifacts_path, metrics):
    """Run experiment"""


def get_parser():
    parser = argparse.ArgumentParser(description='Experiment params')

    # add arguments

    return parser


def process_arg_parser(parser):
    args = parser.parse_args()

    experiment_params = {'hyperparams': json.loads(args.hyperparams)}

    # get args

    # fill experiment func kwargs
    kwargs = {}

    return kwargs


if __name__ == '__main__':
    my_parser = get_parser()

    kwargs = process_arg_parser(my_parser)

    main(**kwargs)

