from setuptools import setup

setup(
    name="textract",
    version="0.0.2",
    description="a lightweight and minimalist python module that takes a .txt file, and provides some context for any given token within the input corpus.",
    py_modules=["textract"],
    package_dir={"": "src"}
     )