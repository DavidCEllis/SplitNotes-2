from setuptools import setup, find_packages

__version__ = "0.5.0"
__author__ = "DavidCEllis"


setup(
    name="splitnotes2",
    version=__version__,
    packages=find_packages("src"),
    url="",
    license="GPLv3",
    description="Speedrun notes tool for advancing notes automatically with Livesplit.",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 1 - Early Development",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    package_dir={"": "src"},
    install_requires=["pyside2", "jinja2", "bleach", "flask", "attrs"],
    tests_require=["pytest", "pytest-cov", "pytest-qt"],
    extras_require={"build_exe": ["cx-freeze", "pywin32"], "dev": ["black"]},
)
