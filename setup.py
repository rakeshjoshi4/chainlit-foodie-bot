from setuptools import find_packages, setup

setup(
    name = "Generative AI Project",
    version = "0.0.0",
    author = "Rakesh Joshi",
    author_email = "rakeshgjoshi4@gmail.com",
    packages = find_packages(),
    install_requires=[
        'chainlit',
        'openai',
        'python-dotenv',
    ]

)