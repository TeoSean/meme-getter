from selenium import webdriver
import os
import urllib.request
driver=webdriver.Chrome('\path\to\chromedriver')
driver.get('link here')
images=driver.find_elements_by_tag_name('img')
x=1
for img in images:
                source = img.get_attribute("src")
                if 'award_images' in source or 'communityIcon' in source:
                                pass
                else:
                                if 'i.redd.it' in source or 'preview.redd.it' in source:
                                                n='meme'+str(x)
                                                os.system('curl {} --output \path\to\meme\folder\{}.jpg'.format(source, n))
                                                print(source)
                                                x=x+1
                                else:
                                                pass

'''
Reddit memes:
https://reddit.com/r/dankmemes
https://reddit.com/r/memes
'''
