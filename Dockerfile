# Use a lightweight base image
FROM python:3.10-slim

# Set up a working directory
WORKDIR /app

# Install system dependencies (optional)
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

# Set a build argument for package version (default: latest)
ARG PACKAGE_VERSION=latest

# Install the correct package version from PyPI
RUN pip install --pre alpss==$PACKAGE_VERSION

CMD ["/bin/bash"]

