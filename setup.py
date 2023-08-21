from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in bookings/__init__.py
from bookings import __version__ as version

setup(
	name="bookings",
	version=version,
	description="Hotel Reservation System",
	author="Ali % Arsalan",
	author_email="baltialinaqi@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires,
)
