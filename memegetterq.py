from selenium import webdriver
import os
import urllib.request
driver=webdriver.Chrome('\path\to\chromedriver')
driver.get('quora link here')
images=driver.find_elements_by_tag_name('img')
x=1
for img in images:
                source = img.get_attribute("src")
                if source.endswith('.jpeg') or source.endswith('.png') or source.endswith('jpg'):
                                pass
                else:
                                n='meme'+str(x)
                                os.system('curl {} --output C:\\Users\woons\OneDrive\Desktop\Coding\Python\Memes\{}.jpg'.format(source, n))
                                print(source)
                                x=x+1
                                
'''
Quora memes:
https://www.quora.com/What-are-some-funny-memes
https://www.quora.com/What-are-some-of-the-greatest-and-funniest-internet-memes
https://www.quora.com/Can-you-post-the-last-five-screenshots-you-have-taken
'''
