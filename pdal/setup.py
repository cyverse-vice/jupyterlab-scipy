import setuptools

setuptools.setup(
    name="jupyter-rsession-proxy",
    version='dev',
    url="https://github.com/cyverse-vice/jupterlab-scipy/gee",
    author="Tyson Lee Swetnam",
    description="Jupyter extension to proxy RStudio & Shiny",
    packages=setuptools.find_packages(),
	keywords=['Jupyter'],
	classifiers=['Framework :: Jupyter'],
    install_requires=[
        'jupyter-server-proxy'
    ],
    entry_points={
        'jupyter_serverproxy_servers': [
            'rstudio = jupyter_rsession_proxy:setup_rstudio',
            'shiny = jupyter_rsession_proxy:setup_shiny'
        ]
    },
    package_data={
        'jupyter_rsession_proxy': ['icons/*'],
    },
)
