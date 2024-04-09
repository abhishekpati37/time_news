# import requests

# def fetch_time_stories():
#     url = "https://time.com"
#     response = requests.get(url)
    
#     if response.status_code == 200:
#         html_content = response.text
#         stories = []
#         index = 0
        
#         while len(stories) < 6:
#             start_index = html_content.find('<a class="headline" href
            
           
# from flask import Flask, render_template
# import requests

# app = Flask(__name__)

# def fetch_time_stories():
#     url = "https://time.com"
#     response = requests.get(url)
    
#     if response.status_code == 200:
#         html_content = response.text
#         stories = []
#         index = 0
        
#         while len(stories) < 6:
#             start_index = html_content.find('<a class="headline" href="', index)
#             if start_index == -1:
#                 break 
#             start_index = html_content.find('>', start_index) + 1
#             end_index = html_content.find('</a>', start_index)
#             headline = html_content[start_index:end_index]
#             stories.append(headline)
#             index = end_index
#         return stories

# @app.route('/')
# def index():
#     stories = fetch_time_stories()
#     return render_template('a.html', stories=stories)

# if __name__ == '__main__':
#     app.run(debug=True)











import urllib.request

def fetch_time_stories():
    url = "https://time.com"
    response = urllib.request.urlopen(url)
    html_content = response.read().decode("utf-8")

    stories = []
    index = 0

    while len(stories) < 6:
        start_index = html_content.find('<a class="headline" href="', index)
        if start_index == -1:
            break
        start_index = html_content.find('>', start_index) + 1
        end_index = html_content.find('</a>', start_index)
        headline = html_content[start_index:end_index].strip()
        stories.append(headline)
        index = end_index

    return stories

if __name__ == "__main__":
    latest_stories = fetch_time_stories()
    for i, story in enumerate(latest_stories, start=1):
        print(f"{i}. {story}")
