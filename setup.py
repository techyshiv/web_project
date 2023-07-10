from setuptools import find_packages, setup

HYPEN_E_DOT = "-e ."


def get_requirements(file_path: str):
    """
    This function will return a list
    """
    requirements = []
    with open(file_path) as path:
        requirements = path.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name="WebProject",
    version="1.0.0",
    author="Shivang Saxena",
    author_email="shivangsaxena177@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
