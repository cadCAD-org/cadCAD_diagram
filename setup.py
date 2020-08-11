from setuptools import setup, find_packages

long_description = """
Automated cadCAD system models diagram through GraphViz
"""

setup(name='cadCAD_diagram',
      version='0.0.1',
      description="Diagram tool for cadCAD",
      long_description=long_description,
      url='https://github.com/danlessa/cadCAD_diagram',
      author='Danilo Lessa Bernardineli',
      author_email='danilo@block.science, danilo.bernardineli@usp.br',
      packages=find_packages(),
      install_requires=['graphviz', 'cadCAD']
)
