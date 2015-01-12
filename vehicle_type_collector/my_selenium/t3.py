__author__ = 'yiqing'

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get('http://data.auto.china.com/auto.html')
try:
    element = WebDriverWait(driver,20).until(
        # EC.text_to_be_present_in_element((By.ID,'catalogList'))
        EC.presence_of_element_located((By.ID,'catalogList'))
    )
    print(
        dir(element),
       ## element.text,
    )
    fileObj = open('content.html','wt')
    '''
    @see http://stackoverflow.com/questions/7263824/get-html-source-of-webelement-in-selenium-webdriver-python

    WebElement element = driver.findElement(By.id("foo"));
 String contents = (String)((JavascriptExecutor)driver).executeScript("return arguments[0].innerHTML;", element);

    '''
    fileObj.write(element.get_attribute('innerHTML'))
    fileObj.close()

    file2 = open('source.html','w')
    '''
    file2.write(
        str(
            element.get_attribute('outerHTML').encode('utf-8')
        )
    )
    '''
    file2.write(
           str.encode( element.get_attribute('outerHTML').encode('utf-8') )
    )
    file2.close()

finally:
    driver.quit()

'''
    elem = driver.find_element_by_xpath("//*")
    source_code = elem.get_attribute('outerHTML')

    f = open('source.html','w')
    ##  f.write(source_code.encode('utf-8'))
    f.write(
        str(
            source_code.encode('utf-8')
        )
    )
    f.close()
'''
