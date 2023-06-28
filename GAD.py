################################################ IMPORTS #############################################################
import time
from datetime import datetime
from selenium import webdriver
from selenium import __version__
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import os
import psutil
import connect_db
from dotenv import load_dotenv
import json
############################################## NAVEGADOR #################################################################
servico = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
# options.add_argument('--headless') # ativa o modo headless.
options.add_argument("--no-sandbox") # o modo no-sandbox reduz o número de camadas de segurança, porém pode ser necessário para garantir a execução.
options.add_argument("--disable-dev-shm-usage") # desativo o armazenamento de arquivos temporários, reduzindo o gasto de memória.
options.add_argument("--disable-gpu") # desativa a GPU
navegador = webdriver.Chrome(service=servico)
navegador.get('https://webtropics.aimmutual.com/webtropics/Login.asp?timed_out=')
############################################### CREDENCIALS ####################################################################
USERNAME_AIM_MUTUAL = "brz_kmota"
PASSWORD_AIM_MUTUAL = "75qzeFA4cmDppppLi"
############################################### JSON ###########################################
J = {}
B = {}
C = {}
############################################### LOGIN ####################################################################
navegador.find_element(By.XPATH, '//*[@id="m_txtUserName"]').click()
navegador.find_element(By.XPATH, '//*[@id="m_txtUserName"]').send_keys(USERNAME_AIM_MUTUAL)
navegador.find_element(By.XPATH, '//*[@id="m_txtPassword"]').click()
navegador.find_element(By.XPATH, '//*[@id="m_txtPassword"]').send_keys(PASSWORD_AIM_MUTUAL)
navegador.find_element(By.XPATH, '//*[@id="m_btnLogin"]').click()

frame_element = navegador.find_element(By.CLASS_NAME, 'termsFooter')
navegador.switch_to.frame(frame_element)
time.sleep(1)
try:
    navegador.execute_script(""" document.querySelector("#m_btnSave").click() """)
    print("Elemento clicado com sucesso!")
except NoSuchElementException:
    print("Elemento não encontrado. Continuando o fluxo normal.")
navegador.switch_to.default_content()
############################################### BUSCAR POLICIES ####################################################################
navegador.find_element(By.XPATH, '//*[@id="Policies"]/span/span/span').click()
time.sleep(2)

unique_ph = navegador.execute_script(""" ph_text = []
    ph = document.querySelectorAll('[class="RowBackgroundOdd"],[class="RowBackgroundEven"]')
    ph.forEach(
        (e)=>{
            ph_text.push(e.querySelectorAll('td')[3].innerText)
        }
    )
    unique_ph = []
    ph_text.forEach(
        (elem)=>{
            if(!unique_ph.includes(elem)){
                unique_ph.push(elem)
            }
        }
    ) return unique_ph  """)
navegador.find_element(By.XPATH, '//*[@id="txtSearchFor"]').click()
navegador.find_element(By.XPATH, '//*[@id="txtSearchFor"]').send_keys(unique_ph)
navegador.find_element(By.XPATH, '//*[@id="commandRow"]/div/span/input[2]').click()
navegador.find_element(By.XPATH, '//*[@id="gridFormat"]/tbody/tr/td[4]/a').click()
print("BUSQUEI A APOLICIES")

############################################### Insured_units ####################################################################
time.sleep(1)

Insured_units = navegador.execute_script(""" J = {}
    keys = []
    values = []
    document.querySelectorAll('[class="CtlSpace"]').forEach(
        (e)=>{keys.push(e.children[0].innerText)
            values.push(e.children[1].getAttribute('value'))})


    for (let index = 0; index < keys.length; index++) {
        J[keys[index]] = values[index]
    }
    return J """)
J['Insured_units'] = Insured_units
print("Insured units OK")

############################################### Work places ####################################################################
time.sleep(1)

navegador.find_element(By.XPATH, '//*[@id="Workpl"]').click()
Work_places = navegador.execute_script(""" J = {}
    keys = []
    values = []
    document.querySelectorAll('[class="CtlSpace"]').forEach(
        (e)=>{keys.push(e.children[0]?.innerText)
            values.push(e.children[1]?.getAttribute('value'))})


    for (let index = 0; index < keys.length; index++) {
        J[keys[index]] = values[index]
    }
    return J """)
J['Work_places'] = Work_places
print("Work places OK")
############################################### Polices ####################################################################
time.sleep(1)

navegador.find_element(By.XPATH, '//*[@id="InsPolicies"]').click()
Policies = navegador.execute_script(""" var polices = document.querySelector("#gridFormat");
    var rows = polices.querySelectorAll('tr');
    var headers = polices.querySelectorAll('th');

    table_history = [];
    rows = Array.from(rows);
    rows.shift();
    rows.pop();
    for (let i = 0; i < rows.length; i++) {
    let j = {};
    let cells = rows[i].querySelectorAll('td');

    for (let i2 = 0; i2 < headers.length; i2++) {
        let keytext = headers[i2]?.innerText;
        let celltext = cells[i2]?.innerText;
        j[keytext] = celltext;
        delete j['']
    }

    table_history.push(j);
    } return table_history""")
J['Policies'] = Policies
print("Polocies OK")
################################################ Audits ###########################################
time.sleep(1)
navegador.execute_script(""" document.querySelector("#Officers").click() """)
try:
    Audits = navegador.execute_script(""" var polices = document.querySelector('[id="gridFormat"]');
    var rows = polices.querySelectorAll('tr');
    var headers = polices.querySelectorAll('th');

    var table_history = [];
    rows = Array.from(rows);
    rows.shift();

    for (let i = 0; i < rows.length; i++) {
    let j = {};
    let cells = rows[i].querySelectorAll('td');

    for (let i2 = 0; i2 < headers.length; i2++) {
        let keytext = headers[i2]?.innerText;
        let celltext = cells[i2]?.innerText;
        if (celltext) {
        j[keytext.replaceAll('\n', ' ')] = celltext.replaceAll('\n', '|').trim();
        }
    }
    
    if (Object.keys(j).length > 0) {
        table_history.push(j);
    }
    } return table_history """)
    print('Audits OK')
    J['Audits'] = Audits
except:
    print('Audits NAO EXISTE ')
################################################ Officers/Entities ################################
time.sleep(1)
navegador.execute_script(""" document.querySelector("#Officers").click() """)
try:
    Officers_Entities = navegador.execute_script(""" var polices = document.querySelector('[id="gridFormat"]')
    var rows = polices.querySelectorAll('tr');
    var headers = polices.querySelectorAll('th');

    table_history = [];
    rows = Array.from(rows);
    rows.shift();

    for (let i = 0; i < rows.length; i++) {
    let j = {};
    let cells = rows[i].querySelectorAll('td');

    for (let i2 = 0; i2 < headers.length; i2++) {
        let keytext = headers[i2]?.innerText;
        let celltext = cells[i2]?.innerText;
        j[keytext.replaceAll('\\n',' ')] = celltext.trim()
        delete j['']
    }

    table_history.push(j);
    } return table_history """)
    print('Officers/Entities OK')
    J['Officers/Entities'] = Officers_Entities
except:
    print('Officers/Entities NAO EXISTE ')
################################################# Certificate Holders ##############################
time.sleep(1)
navegador.execute_script(""" document.querySelector("#CertHolders").click() """)
try:
    Certificate_Holders  = navegador.execute_script(""" var polices = document.querySelector('[id="gridFormat"]');
    var rows = polices.querySelectorAll('tr');
    var headers = polices.querySelectorAll('th');

    var table_history = [];
    rows = Array.from(rows);
    rows.shift();

    for (let i = 0; i < rows.length; i++) {
    let j = {};
    let cells = rows[i].querySelectorAll('td');

    for (let i2 = 0; i2 < headers.length; i2++) {
        let keytext = headers[i2]?.innerText;
        let celltext = cells[i2]?.innerText;
        if (celltext) {
        j[keytext.replaceAll('\\n', ' ')] = celltext.replaceAll('\\n', '|').trim();
        }
    }
    
    if (Object.keys(j).length > 0) {
        table_history.push(j);
    }
    } return table_history """)
    print('Certificate_Holders OK')
    J['Certificate_Holders'] = Certificate_Holders
except:
    print('Certificate_Holders NAO EXISTE ')
################################################ Statemets #########################################
time.sleep(1)

navegador.execute_script(""" document.querySelector("#Billing").click() """) # click em billing
try:
    Details_taments = navegador.execute_script(""" var statements = document.querySelector('[class="TwoColumnsRight"]')
    var rows = statements.querySelectorAll('tr');
    var headers = statements.querySelectorAll('th');

    table_history = [];
    rows = Array.from(rows);
    rows.shift();
    rows.pop();
    for (let i = 0; i < rows.length; i++) {
    let j = {};
    let cells = rows[i].querySelectorAll('td');

    for (let i2 = 0; i2 < headers.length; i2++) {
        let keytext = headers[i2]?.innerText;
        let celltext = cells[i2]?.innerText;
        j[keytext] = celltext;
        delete j['']
    }

    table_history.push(j);
    } return table_history """)
    J['Details_taments'] = Details_taments
    print("Billing OK")
except:
    print('Staments NAO EXISTE ')
################################################ Account Balance #########################################
time.sleep(1)
navegador.execute_script(""" document.querySelector("#Balance").click() """) # click em account balance
try:
    Account_Balance = navegador.execute_script(""" var polices = document.querySelector('[class="TwoColumnsRight"]')
    var rows = polices.querySelectorAll('tr');
    var headers = polices.querySelectorAll('th');

    table_history = [];
    rows = Array.from(rows);
    rows.shift();
    rows.pop();
    for (let i = 0; i < rows.length; i++) {
    let j = {};
    let cells = rows[i].querySelectorAll('td');

    for (let i2 = 0; i2 < headers.length; i2++) {
        let keytext = headers[i2]?.innerText;
        let celltext = cells[i2]?.innerText;
        j[keytext] = celltext.trim()
        delete j['']
    }

    table_history.push(j);
    }  return table_history """)
    J['Account_Balance'] = Account_Balance
    print("Account_Balance OK")
except:
    print('Account_Balance NAO EXISTE ')


jsonString = json.dumps(J)
json_file = open('super_json.json','w')
json_file.write(jsonString)
json_file.close()

navegador.execute_script(""" document.querySelector("#Policies > span > span > span").click() """)