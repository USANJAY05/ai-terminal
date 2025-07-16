from setuptools import setup, find_packages

setup(
    name="ai_terminal",
    version="1.0.4",
    packages=find_packages(),
    install_requires=[
        "typer[all]",
        "rich",
        "langchain",
        "langchain-google-genai",
        "python-dotenv"
    ],
    entry_points={
        "console_scripts": [
            "ati=ai_terminal.main:app",
        ],
    },
)
