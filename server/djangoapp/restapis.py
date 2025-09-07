import requests
import os
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv(
    "backend_url",
    default=(
        "https://sunnytarunsh-3030.theiadockernext-1-labs-prod-"
        "theiak8s-4-tor01.proxy.cognitiveclass.ai/"
    ),
)
sentiment_analyzer_url = os.getenv(
    "sentiment_analyzer_url", default="http://localhost:5050/"
)


def get_request(endpoint, **kwargs):
    """Makes a GET request to the backend API."""
    params = "&".join(f"{key}={value}" for key, value in kwargs.items())
    if params:
        request_url = f"{backend_url}{endpoint}?{params}"
    else:
        request_url = f"{backend_url}{endpoint}"

    print(f"GET from {request_url}")
    try:
        response = requests.get(request_url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Network exception occurred: {e}")
        return None


def post_request(endpoint, data):
    """Makes a POST request to the backend API."""
    request_url = f"{backend_url}{endpoint}"
    print(f"POST to {request_url} with data: {data}")
    try:
        response = requests.post(request_url, json=data, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Network exception occurred: {e}")
        return None


def analyze_review_sentiments(text):
    """
    Calls sentiment analysis service for a review.

    Args:
        text (str): Review text to analyze.
    
    Returns:
        str: Sentiment result ('positive', 'negative', 'neutral').
    """
    request_url = f"{sentiment_analyzer_url}analyze/{text}"
    try:
        response = requests.get(request_url)
        return response.json()
    except Exception as err:
        print(f"Unexpected error: {err} ({type(err)})")
        print("Network exception occurred")
        return None


def post_review(data_dict):
    """
    Posts a review to the backend API.

    Args:
        data_dict (dict): Review data (dealerId, name, review, etc.).
    
    Returns:
        dict: JSON response if successful, else None.
    """
    request_url = f"{backend_url}insert_review"
    try:
        response = requests.post(request_url, json=data_dict)
        response.raise_for_status()
        print(response.json())
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Network exception occurred: {e}")
        return None
