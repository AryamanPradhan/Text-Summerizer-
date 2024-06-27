import setuptools

with open("README.md", "r",encoding="utf-8") as f:
    dis= f.read()


__version__ = "0.0.0"

REPO_NAME = "Text-Summerizer"
AUTHOR_USER_NAME = "Aryaman"
SRC_REPO = "textSummerizer"
AUTHOR_EMAIL = "aryamanacepradhan@gmail.com"




setuptools.setup(
    name = SRC_REPO,
    version=__version__,
    author= AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Text Summerization using NLP",
    long_description=dis,
    long_description_content="text/markdown",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    package_dir = {"":"src"},
    packages = setuptools.find_packages(where="src")

)












