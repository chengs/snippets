import setuptools

setuptools.setup(
    name="mypkg",
    description="An example of generating HTML for a Python package.",
    packages=setuptools.find_packages(),
    tests_require=[
        # extensions for doc
        "sphinx",
        "recommonmark",
        "sphinx_rtd_theme",
        "sphinx-autobuild",
        "sphinx-press-theme"
    ],
)
