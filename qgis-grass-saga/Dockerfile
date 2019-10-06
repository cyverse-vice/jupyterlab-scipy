FROM cyversevice/jupyterlab-scipy:latest

MAINTAINER Tyson Swetnam <tswetnam@cyverse.org>

USER root

# GDAL, GEOS, GRASS, QGIS, SAGA-GIS dependencies
RUN apt-get update \
    && apt-get install -y build-essential software-properties-common \
    && apt-get update && apt-get install -y --no-install-recommends --no-install-suggests \
        libblas-dev \
        libbz2-dev \
        libcairo2-dev \
        libfftw3-dev \
        libfreetype6-dev \
        libgdal-dev \
        libgeos-dev \
        libglu1-mesa-dev \
        libgsl0-dev \
        libjpeg-dev \
        liblapack-dev \
        libncurses5-dev \
        libnetcdf-dev \
        libopenjp2-7 \
        libopenjp2-7-dev \
        libpdal-dev pdal \
        libpdal-plugin-python \
        libpng-dev \
        libpq-dev \
        libproj-dev \
        libreadline-dev \
        libsqlite3-dev \
        libtiff-dev \
        libxmu-dev \
        libzstd-dev \
        bison \
        bzip2 \
        flex \
        g++ \
        gettext \
        gdal-bin \
        git \
        libfftw3-bin \
        make \
        ncurses-bin \
        netcdf-bin \
        proj-bin \
        proj-data \
        python3-pip \
        python3-dev \
        python-virtualenv \
        python \
        python-dev \
        python-numpy \
        python-pil \
        python-ply \
        python-requests \
        sqlite3 \
        subversion \
        sudo \
        wget \
        unixodbc-dev \
        xfce4-terminal \
        zlib1g-dev \
    && apt-get autoremove -y \
    && apt-get clean 

ENV DATA_DIR /data

RUN mkdir -p $DATA_DIR

RUN echo LANG="en_US.UTF-8" > /etc/default/locale
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

# Download the GRASS Github Repo
RUN mkdir -p /code/grass

# add GRASS source repository files to the image
RUN wget -nv --no-check-certificate https://grass.osgeo.org/grass76/source/grass-7.6.0.tar.gz \
	  && tar xzf grass-7.6.0.tar.gz -C /code/grass --strip-components=1

WORKDIR /code/grass

# Set gcc/g++ environmental variables for GRASS GIS compilation, without debug symbols
ENV MYCFLAGS "-O2 -std=gnu99 -m64"
ENV MYLDFLAGS "-s"
# CXX stuff:
ENV LD_LIBRARY_PATH "/usr/local/lib"
ENV LDFLAGS "$MYLDFLAGS"
ENV CFLAGS "$MYCFLAGS"
ENV CXXFLAGS "$MYCXXFLAGS"

# Configure, compile and install GRASS GIS
ENV NUMTHREADS=4
RUN cd /code/grass && ./configure \
    --enable-largefile \
    --with-cxx \
    --with-nls \
    --with-readline \
    --with-sqlite \
    --with-bzlib \
    --with-zstd \
    --with-cairo --with-cairo-ldflags=-lfontconfig \
    --with-freetype --with-freetype-includes="/usr/include/freetype2/" \
    --with-fftw \
    --with-netcdf \
    --with-pdal \
    --with-proj --with-proj-share=/usr/share/proj \
    --with-geos=/usr/bin/geos-config \
    --with-postgres --with-postgres-includes="/usr/include/postgresql" \
    --with-opengl-libs=/usr/include/GL \
    --with-openmp \
    --enable-64bit \
    && make -j 4 && make install 

RUN ldconfig
   
# enable simple grass command regardless of version number
RUN ln -s /usr/local/bin/grass* /usr/local/bin/grass

# Reduce the image size
RUN apt-get autoremove -y
RUN apt-get clean -y

# set SHELL var to avoid /bin/sh fallback in interactive GRASS GIS sessions in docker
ENV SHELL /bin/bash

# Fix permissions
RUN chmod -R a+rwx $DATA_DIR

# declare data volume late so permissions apply
VOLUME $DATA_DIR
WORKDIR $DATA_DIR

# Reduce the docker image size 
RUN rm -rf /code/grass

# once everything is built, install a couple of GRASS extensions
RUN grass -text -c epsg:3857 ${PWD}/mytmp_wgs84 -e && \
    echo "g.extension -s extension=r.sun.mp ; g.extension -s extension=r.sun.hourly ; g.extension -s extension=r.sun.daily" | grass -text ${PWD}/mytmp_wgs84/PERMANENT

# Install SAGA-GIS binary
#RUN apt-get install -y software-properties-common && \
#    add-apt-repository ppa:ubuntugis/ubuntugis-unstable && \
#    apt-get -y update && \
#    apt-get install -y saga

# Compile SAGA-GIS 7.2.0 
RUN apt-get install -y gtk2-engines-pixbuf
RUN mkdir /code/saga-gis && \
    wget -nv --no-check-certificate https://cfhcable.dl.sourceforge.net/project/saga-gis/SAGA%20-%207/SAGA%20-%207.2.0/saga-7.2.0.tar.gz && \
    tar xzf saga-7.2.0.tar.gz -C /code/saga-gis --strip-components=1 && rm saga-7.2.0.tar.gz
RUN apt-get install -y libwxgtk3.0-dev libtiff5-dev libgdal-dev libproj-dev \
    libexpat-dev wx-common libogdi3.2-dev unixodbc-dev
RUN cd /code/saga-gis \
        && ./configure \
        && make -j 12 \
        && make install

# Install QGIS Latest LTR Desktop binary
RUN apt-get -y update && apt-get -f install \
    && echo "deb https://qgis.org/ubuntu bionic main" >> /etc/apt/sources.list \
    && echo "deb-src https://qgis.org/ubuntu bionic main" >> /etc/apt/sources.list \
    && apt-key adv --keyserver keyserver.ubuntu.com --recv-key CAEB3DC3BDF7FB45 

# Install QGIS now
RUN apt-get -y update \
    && apt-get install -y \
        python-qgis-common \
        python-qgis \
        qgis-plugin-grass \
        qgis-providers \
        qgis \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
