from selenium import webdriver
from bs4 import BeautifulSoup

urls=[
    'UCkXmLjEr95LVtGuIm3l2dPg'
]

def main():
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/c/WebProgrammingUNPAS/videos?view=0&sort=dd&flow=grid".format(urls[0]))
    content = driver.page_source.encode('utf-8').strip()
    soup = BeautifulSoup(content, 'lxml')
    titles = soup.findAll('a', id='video-title')
    views = soup.findAll('span', class_='style-scope ytd-grid-video-renderer')
    video_urls = soup.findAll('a', id='video-title')
    # print(titles)
    # for view in views:
    #    print(view.text)
    print('Channel: {}'.format(urls[0]))
    i = 0
    j = 0
    for title in titles[:20]:
        print('\n{}\t{}\t{}\thttps://www.youtube.com{}'.format(title.text, views[i].text, views[i+1].text, video_urls[j].get('href')))
        i+=2
        j+=1
        
main()