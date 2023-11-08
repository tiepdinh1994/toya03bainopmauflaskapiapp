"""
00 fork this replit to your replit 

01a do your code
01b your final goal is to hit Run and have all tests PASS IN GREEN

02a git commit push to github repo - view guide https://drive.google.com/file/d/1PZZ2xIlamM0pPtLlbpDodseCKcIVhTzW/view?usp=sharing
02b get url to your git repo in 02a above - we call it :gitrepourl

03 paste :gitrepourl into this google form and submit it
   https://forms.gle/cuxhb8cbYaJLHRYz5
   ma_debai = toya03bainopmauflaskapiapp
"""

from flask import Flask, jsonify
import os
#
from src.helper import github_request

app = Flask(__name__)


@app.route('/')
def index():
  return {}


@app.route('/release')
def release():
  return github_request(f'https://api.github.com/repos/{os.environ.get("OWNER")}/{os.environ.get("REPO")}/releases')


@app.route('/most_3_recent/release')
def most_3_recent__release():
  return github_request(f'https://api.github.com/repos/{os.environ.get("OWNER")}/{os.environ.get("REPO")}/releases?per_page=3')


if __name__ == '__main__':
  app.run(debug=True, port=os.environ.get('PORT', 5000))
