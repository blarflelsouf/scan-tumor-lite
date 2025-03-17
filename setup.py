from setuptools import find_packages
from setuptools import setup

with open("requirements.txt") as f:
    content = f.readlines()
requirements = [x.strip() for x in content if "git+" not in x]

setup(name='scantumor-lite',
      version="0.0.1",
      description="UI of scan tumor IA V1",
      license="None",
      author="Team Louis",
      author_email="contact@lewagon.org",
      #url="https://github.com/blarflelsouf/Scan-tumor",",
      install_requires=requirements,
      packages=find_packages(),
      test_suite="test",
      # include_package_data: to install data from MANIFEST.in
      include_package_data=True,
      zip_safe=False)
