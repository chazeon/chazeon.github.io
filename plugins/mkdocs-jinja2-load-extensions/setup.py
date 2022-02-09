from setuptools import setup, find_packages

setup(
    name="mkdocs-jinja2-load-extensions",
    version="0.0.1",
    packages=find_packages(),
    entry_points={
        'mkdocs.plugins': [
            'jinja2_load_extensions = mkdocs_jinja2_load_extensions:Jinja2LoadExtensionPlugin',
        ]
    },
    requires=[
        "mkdocs",
    ]
)