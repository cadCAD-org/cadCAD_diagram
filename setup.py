from setuptools import setup, find_packages

long_description = """
Automated cadCAD system models diagram through GraphViz
"""

setup(name='cadCAD_diagram',
      version='0.0.1.0',
      description="Diagram tool for cadCAD",
      long_description=long_description,
      url='https://github.com/danlessa/cadCAD_diagram',
      author='Danilo Lessa Bernardineli',
      author_email='danilo@block.science, danilo.lessa@gmail.com',
      packages=find_packages(),
      install_requires=['graphviz', 'cadCAD']
)
