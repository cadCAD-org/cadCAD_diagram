# cadCAD_diagram
Automated cadCAD system models diagram through GraphViz.

This Python module generate diagrams for existing cadCAD models with an 
aesthetic similiar to the illustrations on the official documentation.
 (https://github.com/cadCAD-org/cadCAD/tree/master/documentation)

![Official documentation diagram](https://i.imgur.com/3L5CNUh.png)


## Installation

The recommended way is through pip:

```sh
pip install cadCAD_diagram
```

Alternatively, you can install a branch directly from the repository through:

```sh
pip install git+https://github.com/danlessa/cadCAD_diagram@master
```

## Usage

There are two way to generate a diagram. The first one involves providing
the objects which defines the cadCAD variables, parameters and PSUBs, and
the second one involves providing the Configuration object directly.

Generating a diagram from the cadCAD components is done through:

```python
>>> from cadCAD_diagram import diagram
>>> dia = diagram(initial_state, sys_params, partial_state_update_block)
>>> dia.format = 'png'
>>> dia.render()
```

While generating a diagram from a Configuration object would be as follows:

```python
>>> from cadCAD_diagram import diagram_from_config
>>> dia = diagram_from_config(config)
>>> dia.format = 'png'
>>> dia.render()
```

If you use the ``append_configs`` method, you could plot the diagram of the first config by:
```python
from cadCAD_diagram import diagram_from_config
from cadCAD import configs
diagram_from_config(configs[0])
``` 

## Examples

An minimal example is done by the following block:

```python
def policy_1(p, s, h, v):
    return {"pi_1": v["var_1"]}

def policy_2(p, s, h, v):
    return {"pi_1": v["var_1"], "pi_2": v["var_1"] * v["var_2"]}

def suf_1(p, s, h, v, pi):
    return ("var_1", pi["pi_1"])

def suf_2(p, s, h, v, pi):
    return ("var_2", pi["pi_2"])

psubs = [
    {
        "label": "Test",
        "policies": {"policy_1": policy_1, "policy_2": policy_2},
        "variables": {"var_1": suf_1, "var_2": suf_2},
    }
]
initial_state = {"var_1": 0, "var_2": 1}
params = {"param_1": 0, "param_2": 1}

from cadCAD_diagram.config_diagram import diagram
dia = diagram(initial_state, params, psubs)
dia
```

![Output diagram from the simple example](https://i.imgur.com/IHPqv2E.png)

Another example is the a colab version of the Prey & Predator demo available on the following link: https://colab.research.google.com/drive/1AQugR2m89SpAxobk6Y_cppAFsPN6Eg7b