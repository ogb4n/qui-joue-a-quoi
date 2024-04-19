from flask import Flask, request, render_template
import requests
import matplotlib.pyplot as plt
import asyncio
from bs4 import BeautifulSoup



res = requests.get('https://store.steampowered.com/stats/userdata.json?days_back=3')
data2 = res.json()

print(data2[0]['data'][-1])