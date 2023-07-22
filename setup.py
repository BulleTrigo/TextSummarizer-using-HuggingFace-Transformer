import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
__version__ = "0.0.1"

REPO_NAME = "TextSummarizer-using-HuggingFace-Transformer"
AUTHOR_USER_NAME = "BulleTrigo"
SRC_REPO = "textSummarizer"
AUTHOR_NAME = "Swapnesh Sanjeev Srivastava"
AUTHOR_EMAIL = "swapneshsrivastava@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package to summarize text using HuggingFace Transformers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"http://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)