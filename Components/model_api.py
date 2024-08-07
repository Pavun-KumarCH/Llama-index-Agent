import os
import sys
from dotenv import load_dotenv, find_dotenv

from llama_index.llms.gemini import Gemini
import google.generativeai as genai

from exception import customexception
from IPython.display import Markdown, display
from logger import logging

load_dotenv(find_dotenv())

genai.configure(api_key = os.environ['GOOGLE_API_KEY'])

def load_model():
    """
    Loads a Gemini-Pro model for natural language processing.

    Returns:
    - Gemini: An instance of the Gemini class initialized with the 'gemini-pro' model.
    """
    try:
        logging.info("Loading the model with API...")
        model = Gemini(model = "models/gemini-1.5-flash", api_key = os.environ['GOOGLE_API_KEY'])
        return model
    except Exception as e:
        logging.infot(f"{model} loaded from api..!")
        raise customexception(e, sys)

