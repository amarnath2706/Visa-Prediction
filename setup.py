from setuptools import setup, find_packages

setup(

    name = "visa_prediction",
    version = "0.0.0",
    author = "Amarnath",
    author_email="amarnath.arjsd@gmail.com",
    packages = find_packages()
)

# -e . -> look for setup.py file -> setup.py file look for constructor file in each and every folder (__init__.py)
# wherever we have constructor file that files will be considered as my local package