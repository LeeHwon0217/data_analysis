import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# 베스트 댓글
driver = webdriver.Chrome()
driver.get('https://comic.naver.com/webtoon/detail?titleId=777767&no=214&week=fri')

time.sleep(1)

xpath = '/html/body/div[1]/div[5]/div/div/div[5]/div[1]/div[3]/div/section/ul/li'
best_comment_elements = driver.find_elements(By.XPATH, xpath)

for li in best_comment_elements:
    try:
        comment_p = li.find_element(By.XPATH, './div[1]/div[2]/div/p')
        comment_text = comment_p.text.strip()
        print(comment_text)
        print('-'*30)
    except Exception as e:
        print(e)

time.sleep(1)

# 전체 댓글
driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div/div/div[5]/div[1]/div[3]/div/section/div[4]/button[2]').click()

time.sleep(1)

print('***** 전체댓글 *****')
xpath = '/html/body/div[1]/div[5]/div/div/div[5]/div[1]/div[3]/div/section/ul/li'
total_comment_elements = driver.find_elements(By.XPATH, xpath)
for li in total_comment_elements:
    try:
        # /html/body/div[1]/div[5]/div/div/div[5]/div[1]/div[3]/div/section/ul/li[1]/div[1]/div[2]/div/p
        comment_p = li.find_element(By.XPATH, './div[1]/div[2]/div/p')
        comment_text = comment_p.text.strip()
        print(comment_text)
        print('-'*30)
    except Exception as e:
        print('********클린봇에 걸림********')
        print('-'*30)

# 창 안닫게 하기
time.sleep(2)