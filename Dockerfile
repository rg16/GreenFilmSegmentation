# Use an official Python runtime as a base image
FROM continuumio/anaconda

# Install any needed packages
RUN conda install opencv
RUN pip uninstall matplotlib -y # Weird, but it works. Otherwise can't import pyplot
RUN pip install matplotlib

WORKDIR /app

# Run app.py when the container launches
CMD ["python", "segment.py"]
