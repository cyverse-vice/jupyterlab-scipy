FROM cyversevice/jupyterlab-scipy:latest

# reset user to root to install depenencies
USER root

# Install Geospatial dependencies and Google Earth Engine API
RUN conda update -n base conda && conda install -y -c conda-forge earthengine-api pandas folium nodejs cython gdal proj4 udunits2 pdal entwine 
# install a bunch of dependencies with pip
RUN pip install --upgrade pip && \
    pip install altair && \
    pip install bqplot && \
    pip install fiona && \
    pip install google-api-python-client && \
    pip install humanize && \
    pip install ipyleaflet && \
    pip install ipywidgets && \
    pip install ipyvolume && \
    pip install kml2geojson && \
    pip install matplotlib && \
    pip install nbdime && \
    pip install oauth2client && \
    pip install palettable && \
    pip install pathlib && \
    pip install planet && \
    pip install pyCrypto && \
    pip install rasterio && \
    pip install vega_datasets

# add GEOJSON widget
RUN jupyter labextension install @jupyterlab/geojson-extension && \
    jupyter labextension install jupyter-leaflet && \
    jupyter labextension install @jupyter-widgets/jupyterlab-manager
    
# add IPyleaflet 
RUN jupyter nbextension install --py --symlink --sys-prefix ipyleaflet && \
    jupyter nbextension enable --py --sys-prefix ipyleaflet && \
    jupyter labextension install ipyvolume

# add widgets extension manager
RUN jupyter nbextension enable --py --sys-prefix widgetsnbextension && \
    jupyter labextension install @jupyter-widgets/jupyterlab-manager && \
    jupyter nbextension enable --py widgetsnbextension --sys-prefix

# add bqplot extension
RUN jupyter labextension install bqplot && \
    jupyter nbextension install bqplot --py --symlink --sys-prefix && \ 
    jupyter nbextension enable --py --sys-prefix bqplot

# EXPERIMENTAL Jupyter R Proxy Service with R-Studio & Shiny outside of Jupyter Lab

# RUN jupyter labextension install jupyterlab-server-proxy

# Install R Kernel w/ spatial depends
RUN conda install -c r \
	r-base \
	r-caret \
	r-devtools \
	r-dplyr \
	r-dt \
	r-forecast \
	r-geosphere \
	r-hexbin \
	r-htmltools \
	r-htmlwidgets \
	r-irkernel \
	r-jsonlite \
        r-leaflet \ 
        r-leaflet.extras \
        r-lubridate \
        r-plyr \ 
        r-rcurl \
        r-reshape2 \
        r-rmarkdown \
        r-rodbc \
        r-rsqlite \
        r-shiny \
        r-shinythemes \
        r-shinyWidgets \
        r-shinyBS \
        r-shinyjs \
        r-sf \
        r-sparklyr \
        r-stringi \
        r-rstudioapi \
        r-tidyverse \
    && conda install -c conda-forge \
        r-crul \
        r-rgdal \
        r-proj4

# more R stuff
RUN apt-get update && apt-get install -y --no-install-recommends \
	libapparmor1 \
	libedit2 \
	lsb-release \
	psmisc \
	libssl1.0.0 \
        fonts-dejavu \
        unixodbc \
        unixodbc-dev \
        r-cran-rodbc \
        gfortran \
        gcc

# Wierd error fix for neonUtilities
# Download the source code
RUN wget http://archive.ubuntu.com/ubuntu/pool/main/i/icu/icu_4.8.1.1.orig.tar.gz &&\
	tar xzf icu_4.8.1.1.orig.tar.gz && \
	rm -rf icu_4.8.1.1.orig.tar.gz && \
	cd icu/source && \
	./configure && \ 
	make && \
	make install && \
	rm -rf icu/

RUN echo "r <- getOption('repos'); r['CRAN'] <- 'http://cran.us.r-project.org'; options(repos = r);" > ~/.Rprofile
RUN Rscript -e "install.packages('neonUtilities', dependencies=TRUE)"
		
# Use rsession from rstudio's desktop package
#RUN apt-get install -y libclang-dev
#ENV RSTUDIO_PKG=rstudio-server-1.2.5001-amd64.deb
#RUN wget -q https://download2.rstudio.org/server/bionic/amd64/rstudio-server-1.2.5001-amd64.deb
#RUN dpkg -i ${RSTUDIO_PKG}
#RUN rm ${RSTUDIO_PKG}

# The desktop package uses /usr/lib/rstudio/bin
#ENV PATH="${PATH}:/usr/lib/rstudio-server/bin"
#ENV LD_LIBRARY_PATH="/usr/lib/R/lib:/lib:/usr/lib/x86_64-linux-gnu:/usr/lib/jvm/java-7-openjdk-amd64/jre/lib/amd64/server:/o$

RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install the proxy
ADD setup.py setup.py
ADD jupyter_rsession_proxy/ jupyter_rsession_proxy/
RUN pip install .

# Last update and re-build
RUN conda clean --all -f -y
RUN jupyter lab build

# Change user back to jovyan

USER jovyan

# Entrypoint is set in previous cyversevice/jupyterlab-scipy:latest container

