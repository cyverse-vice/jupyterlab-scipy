FROM cyversevice/jupyterlab-scipy:latest

USER root

RUN conda update -n base conda 

# Install Geospatial dependencies and Google Earth Engine API
RUN conda install -y -c conda-forge earthengine-api pandas folium nodejs cython gdal proj4 udunits2 pdal entwine 

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

RUN jupyter labextension install @jupyterlab/geojson-extension && \
    jupyter labextension install jupyter-leaflet && \
    jupyter labextension install @jupyter-widgets/jupyterlab-manager
    
RUN jupyter nbextension install --py --symlink --sys-prefix ipyleaflet && \
    jupyter nbextension enable --py --sys-prefix ipyleaflet && \
    jupyter labextension install ipyvolume

RUN jupyter nbextension enable --py --sys-prefix widgetsnbextension && \
    jupyter labextension install @jupyter-widgets/jupyterlab-manager && \
    jupyter nbextension enable --py widgetsnbextension --sys-prefix

RUN jupyter labextension install bqplot && \
    jupyter nbextension install bqplot --py --symlink --sys-prefix && \ 
    jupyter nbextension enable --py --sys-prefix bqplot

# Install R Kernel w/ spatial depends
RUN conda install -c r r-dplyr r-dt r-geosphere r-irkernel r-jsonlite \
       r-leaflet r-leaflet.extras r-lubridate r-shiny r-shinythemes \
       r-shinyWidgets r-shinyBS r-shinyjs r-sf r-stringi r-rstudioapi
RUN conda install -c conda-forge r-crul r-rgdal r-proj4

RUN apt-get update && \
	apt-get install -y --no-install-recommends \
		libapparmor1 \
		libedit2 \
		lsb-release \
		psmisc \
		libssl1.0.0 

# wierd error fix for neonUtilities
# Download the source code
RUN wget http://archive.ubuntu.com/ubuntu/pool/main/i/icu/icu_4.8.1.1.orig.tar.gz &&\
	tar xzf icu_4.8.1.1.orig.tar.gz && \
	rm -rf icu_4.8.1.1.orig.tar.gz && \
	cd icu/source && \
	./configure && \ 
	make && \
	make install && \
	rm -rf icu/
		
# You can use rsession from rstudio's desktop package as well.
ENV RSTUDIO_PKG=rstudio-server-1.0.136-amd64.deb

RUN wget -q http://download2.rstudio.org/${RSTUDIO_PKG}
RUN dpkg -i ${RSTUDIO_PKG}
RUN rm ${RSTUDIO_PKG}

RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install the VS code proxy
ADD setup.py setup.py
ADD jupyter_rsession_proxy jupyter_rsession_proxy

RUN pip install .

# Install NEON Utilities

#RUN echo "r <- getOption('repos'); r['CRAN'] <- 'http://cran.us.r-project.org'; options(repos = r);" > ~/.Rprofile
#RUN Rscript -e "install.packages('neonUtilities', dependencies=TRUE)"

USER jovyan

# The desktop package uses /usr/lib/rstudio/bin
ENV PATH="${PATH}:/usr/lib/rstudio-server/bin"
ENV LD_LIBRARY_PATH="/usr/lib/R/lib:/lib:/usr/lib/x86_64-linux-gnu:/usr/lib/jvm/java-7-openjdk-amd64/jre/lib/amd64/server:/opt/conda/lib/R/lib"

