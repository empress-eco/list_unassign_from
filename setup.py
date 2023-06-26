# Frappe List Unassign Form © 2023
# Author:  Ameen Ahmed
# Company: Level Up Marketing & Software Development Services
# Licence: Please refer to LICENSE file


from setuptools import setup, find_packages
from frappe_list_unassign_from import __version__ as version


with open("requirements.txt") as f:
    install_requires = f.read().strip().split("\n")


setup(
    name="frappe_list_unassign_from",
    version=version,
    description="A Frappe plugin that adds the support of project tasks single or multiple unassign.",
    author="Ameen Ahmed (Level Up)",
    author_email="kid1194@gmail.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires
)