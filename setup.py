from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in fleet_mgmt/__init__.py
from fleet_mgmt import __version__ as version

setup(
	name="fleet_mgmt",
	version=version,
	description="fleet management",
	author="gokul",
	author_email="go.kul.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
