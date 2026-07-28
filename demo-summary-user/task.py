import numpy as np

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id




rng_local = np.random.default_rng(seed=42)
sample = rng_local.normal(loc=0, scale=1, size=(100, 4))

stats = {
    'mean': [round(float(v), 3) for v in sample.mean(axis=0)],
    'std': [round(float(v), 3) for v in sample.std(axis=0)],
    'rows': int(sample.shape[0]),
}
labels = ['A', 'B', 'C', 'D']

print('stats:', stats)
print('labels:', labels)

file_labels = open("/tmp/labels_" + id + ".json", "w")
file_labels.write(json.dumps(labels))
file_labels.close()
