import numpy as np

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id




rng = np.random.default_rng(seed=42)
data = rng.normal(loc=0, scale=1, size=(100, 4))

print(f'Shape:  {data.shape}')
print(f'Mean:   {data.mean(axis=0).round(3)}')
print(f'Std:    {data.std(axis=0).round(3)}')
print(f'Min:    {data.min(axis=0).round(3)}')
print(f'Max:    {data.max(axis=0).round(3)}')

file_data = open("/tmp/data_" + id + ".json", "w")
file_data.write(json.dumps(data))
file_data.close()
file_rng = open("/tmp/rng_" + id + ".json", "w")
file_rng.write(json.dumps(rng))
file_rng.close()
