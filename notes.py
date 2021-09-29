#!/usr/bin/env python3
import yaml
import sys
import numpy as np

from jinja_env import ENV

with open("data.yml") as fp:
    data = yaml.safe_load(fp)

for name, values in data['courses'].items():
    values['mean'] = np.mean(values['notes'])
    values['notes'].extend([
        None for k in range(
            data['size'] - len(values['notes'])
            )
        ]
    )

if __name__ == '__main__':
    sys.stdout.write(ENV.get_template('template.tex').render(
        data=data['courses'],
        nb_notes=data['size'])
    )
