import requests
from fastapi import APIRouter

from model import ResponseModel
from model.exception import MyCustomException
from config import settings

