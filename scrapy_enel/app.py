from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

import os
from dotenv import load_dotenv

load_dotenv()

with webdriver.Chrome() as driver:
    # Define configs
    enel_url = 'https://www.eneldistribuicao.com.br/go/LoginAcessoRapidoPagamento.aspx'    
    unity_consumer = os.getenv("UNITY_CONSUMER")
    client_identification = os.getenv("CLIENT_IDENTIFICATION")
        
    # Initialize
    wait = WebDriverWait(driver, 5, 3)
    
    # Open URL
    driver.get(enel_url)
    
    # set values in inputs
    driver.find_element_by_name('ctl00$CONTENT$Formulario$NumeroCliente').send_keys(unity_consumer)
    driver.find_element_by_name('ctl00$CONTENT$Formulario$Documento').send_keys(client_identification)
    
    # Submit form
    driver.find_element_by_id("CONTENT_Formulario_Acessar").click()
    
    # Await show modal confirm protocol
    wait.until(presence_of_element_located((By.CLASS_NAME, "bootstrap-dialog-message")))
    
    ## Close modal confirm protocol
    driver.find_element_by_class_name("dialog-fix-size-button").click()
        
    # Set click checkbox button
    driver.execute_script("document.getElementById('CONTENT_Formulario_GridViewSegVia_CheckFatura_0').checked = true;")
    
    print("sleeping after click checkbox button")
    sleep(0.3)
    
    # Click button to generate bar code
    driver.find_element_by_id("CONTENT_Formulario_CodigoBarras").click()
    
    sleep(1)
    
    # Tag with bar code in html
    bar_code = driver.find_element_by_id("CONTENT_Formulario_BarCode")
    
    # Download image bar code
    driver.find_element_by_id('CONTENT_Formulario_ImpressaoCodigoBarras').click()
    
    # Print in console bar code
    print(bar_code.text)
    
    # Await to download image bar code
    sleep(3)
        
    # close driver   
    driver.quit()
