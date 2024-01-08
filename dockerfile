# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory in the container
WORKDIR /usr/src/app

# Install git, necessary for some huggingface models
RUN apt-get update && apt-get install -y git

# Install any needed packages specified in requirements.txt
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /usr/src/app
COPY . /usr/src/app

# Download the model using the huggingface_hub library
RUN python -c "from huggingface_hub import snapshot_download; snapshot_download('amgadhasan/phi-2', cache_dir='/usr/src/app/model')"

# Modify your Python script to load the model from the baked-in directory
# Ensure loadmodel.py uses the path '/usr/src/app/model' for loading the model

# Use ENTRYPOINT to specify the script to be run, allowing for additional command-line arguments
ENTRYPOINT ["python", "/usr/src/app/loadmodel.py"]
