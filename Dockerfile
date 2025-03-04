# Use a lightweight base image
FROM python:3.10-slim

# Set up a working directory
WORKDIR /app

# Install system dependencies required by OpenCV
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Install the package from PyPI
ARG PACKAGE_VERSION=latest
RUN pip install --pre alpss==$PACKAGE_VERSION

# Set a default command (optional)
CMD ["/bin/bash"]
