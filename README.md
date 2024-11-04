# Echo API

A simple Flask API that echoes back the value of the `q` query parameter.

## Setup

1. Create a virtual environment:

```sh
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```sh
pip install -r requirements.txt
```

3. Run the application:

```sh
python app.py
```

## Usage

Send a GET request to /echo with a q parameter:

```sh
curl "http://127.0.0.1:5000/echo?q=hello"
{
  "message": "hello"
}
```