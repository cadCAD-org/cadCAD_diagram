# cadCAD_diagram
Automated cadCAD system models diagram through GraphViz

## Usage

There are two way to generate a diagram. The first one involves providing
the objects which defines the cadCAD variables, parameters and PSUBs, and
the second one involves providing the Configuration object directly.

The first one is done by:

```python
>>> from cadCAD_diagram import diagram
>>> dia = diagram(initial_state, sys_params, partial_state_update_block)
>>> dia.format = 'png'
>>> dia.render()
```

While the second one would be:

```python
>>> from cadCAD_diagram import diagram_from_config
>>> dia = diagram_from_config(config)
>>> dia.format = 'png'
>>> dia.render()
```
