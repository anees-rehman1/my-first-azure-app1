# Use a lightweight Python image
FROM python:3.11-slim

# Set the working folder inside the container
WORKDIR /app

# Copy your files into the container
COPY requirements.txt .
COPY app.py .

# Install the required libraries
RUN pip install --no-cache-dir -r requirements.txt

# Tell the container which port to use
EXPOSE 80

# Command to run when the container starts
CMD ["gunicorn", "--bind", "0.0.0.0:80", "app:app"]
