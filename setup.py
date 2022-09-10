from setuptools import setup

setup(
    name="spm_convert",
    version="0.1.0",
    py_modules=["spm_convert"],
    install_requires=[
        "Click",
    ],
    entry_points="""
        [console_scripts]
        spm-convert=spm_convert:cli
    """,
)
