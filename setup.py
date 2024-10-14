from setuptools import setup, find_packages

setup(
    name="language_translator",
    version="0.1",
    description="A simple language translation application using Tkinter and gTTS.",
    author="Luke Pricone",  # Replace with your name
    author_email="lukey.pricone@icloud.com",  # Replace with your email
    packages=find_packages(),
    install_requires=[
        "requests",
        "gtts",
    ],
    entry_points={
        'console_scripts': [
            'language_translator=translator:main',  # Assuming your main function is defined in translator.py
        ],
    },
)
