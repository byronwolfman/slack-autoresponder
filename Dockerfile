FROM python:2.7.14-slim

# Setup app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Install requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy app files
COPY . .

CMD ["/usr/src/app/responder.py"]
