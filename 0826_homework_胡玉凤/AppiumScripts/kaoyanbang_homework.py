from appium import webdriver
import random
import time

caps = {
  "platformName": "Android",
  "platformVersion": "5.1.1",
  "deviceName": "127.0.0.1:52001",
  "app": "E:\\ruanjian\\App\\kaoyan3.1.0.apk",
  "appPackage": "com.tal.kaoyan",
  "appActivity": "com.tal.kaoyan.ui.activity.SplashActivity",
  "noReset": False
}

# 连接启动设备
driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

driver.find_element_by_id("android:id/button2").click()
time.sleep(2)
driver.find_element_by_id("com.tal.kaoyan:id/tv_skip").click()
time.sleep(2)
driver.find_element_by_id("com.tal.kaoyan:id/login_register_text").click()
time.sleep(2)

# 设置头像
driver.find_element_by_id("com.tal.kaoyan:id/activity_register_userheader").click()
time.sleep(2)
imgs = driver.find_elements_by_xpath('//android.widget.GridView[@resource-id="com.tal.kaoyan:id/activity_photoentrance_gridview"]'
                              '//android.widget.ImageView[@resource-id="com.tal.kaoyan:id/item_image"]')
print(len(imgs))
random.choice(imgs[1:]).click()
time.sleep(1)
driver.find_element_by_id('com.tal.kaoyan:id/save').click()
time.sleep(2)

# 设置用户名
timestr = time.strftime("%H%M%S")
driver.find_element_by_id('com.tal.kaoyan:id/activity_register_username_edittext').send_keys(f'who{timestr}')
time.sleep(2)

# 设置密码
driver.find_element_by_id('com.tal.kaoyan:id/activity_register_password_edittext').send_keys('aaaa1221')
time.sleep(2)

# Email
driver.find_element_by_id('com.tal.kaoyan:id/activity_register_email_edittext').send_keys(f'{timestr}xxx@126.com')
time.sleep(3)

# 点击注册
driver.find_element_by_id('com.tal.kaoyan:id/activity_register_register_btn').click()
time.sleep(2)
driver.save_screenshot('./pics/%s.png'%timestr)

# 选择目标院校和专业
driver.find_element_by_id('com.tal.kaoyan:id/perfectinfomation_edit_school_name').click()
driver.find_element_by_id('com.tal.kaoyan:id/more_forum_title').click()
driver.find_element_by_id('com.tal.kaoyan:id/university_search_item_name').click()

driver.find_element_by_id('com.tal.kaoyan:id/activity_perfectinfomation_major').click()
driver.find_element_by_id('com.tal.kaoyan:id/major_subject_title').click()
subject = driver.find_elements_by_id('com.tal.kaoyan:id/major_search_item_name')
random.choice(subject).click()


# 进入考研帮
driver.find_element_by_id('com.tal.kaoyan:id/activity_perfectinfomation_goBtn').click()
time.sleep(3)
driver.find_element_by_id("com.tal.kaoyan:id/view_wemedia_cacel").click()
time.sleep(2)

# 我的
driver.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_mysefl').click()
time.sleep(2)

# 退出
driver.find_element_by_id('com.tal.kaoyan:id/myapptitle_RightButton_textview').click()
time.sleep(2)
driver.find_element_by_id('com.tal.kaoyan:id/setting_logout_text').click()
time.sleep(2)
driver.find_element_by_id('com.tal.kaoyan:id/tip_commit').click()
time.sleep(5)



driver.quit()