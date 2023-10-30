
import pyautogui
from time import sleep
from datetime import datetime

# INICIALIZA O NAVEGADOR  ----------------------------------------------------------------------------------------------
pyautogui.press('winleft')
sleep(3)
pyautogui.write('google')
sleep(5)
pyautogui.press('enter')
sleep(5)


# MAXIMIZANDO A JANELA -------------------------------------------------------------------------------------------------
pyautogui.hotkey('winleft', 'up')
sleep(5)


# ENTRANDO NO EMAIL ----------------------------------------------------------------------------------------------------
pyautogui.click(231,57,duration=0.5)
pyautogui.write("outlook.com")
sleep(2)
pyautogui.press('enter')
sleep(16) # aguardando a página carregar


# FILTRANDO EMAIL ------------------------------------------------------------------------------------------------------
pyautogui.click(373,133, duration=0.1) # clicar no campo de pesquisa
sleep(2)
pyautogui.write('Lpnet Fatura') # Substitua pelo
sleep(2)
pyautogui.press('enter')
sleep(5)
pyautogui.click(547,254, duration=0.1) # Filtrando emails com anexos
pyautogui.click(454,376, duration=0.5) # Clicando no email
sleep(8)
pyautogui.click(820,462, duration=0.1) # Clicando no anexo
sleep(5)
pyautogui.click(201,169, duration=0.1) # Baixando o anexo
sleep(5)
 
pyautogui.hotkey('alt', 'f4') # fechando página


# COLANDO ANEXO --------------------------------------------------------------------------------------------------------
sleep(1)
pyautogui.hotkey('winleft','r') # abrindo o executar
sleep(1)
pyautogui.write('C:\\Users\\Henrique\\Downloads')  # Substitua com o caminho do seu arquivo PDF)
sleep(1)
pyautogui.press('enter')
pyautogui.hotkey('win', 'up')
sleep(2)
pyautogui.hotkey('ctrl', 'f') # filtrando....
sleep(4)
pyautogui.write('FaturaLPNet') # Substitua com o nome do seu arquivo PDF
sleep(5)
pyautogui.press('enter')
sleep(5)
pyautogui.moveTo(250,250, duration=1)
pyautogui.click()
pyautogui.hotkey('ctrl', 'c') # colando
sleep(1)
pyautogui.hotkey('alt', 'f4')
sleep(5)

# ABRINDO O WHATSAAP ---------------------------------------------------------------------------------------------------
pyautogui.press('winleft')
sleep(8)
pyautogui.write('whatsapp')
sleep(3)
pyautogui.press('enter')
sleep(8) # Aguarde mais alguns segundos para o WhatsApp carregar


# Encontrar e clicar no contato "pai"
pyautogui.hotkey('ctrl', 'f')  # Abre a caixa de busca
sleep(2)
pyautogui.write('pai')  # Digita o nome do contato
sleep(2)  # Aguarde um pouco para a busca
pyautogui.press('tab')
sleep(2)
pyautogui.press('enter')
sleep(2)


# Anexar o arquivo PDF
pyautogui.click(603,712, duration=1)  # clicar no campo d enviar mensagem
sleep(2)
pyautogui.hotkey('ctrl', 'v')
sleep(8)
pyautogui.write(f'*Fatura do mes {datetime.now().month}/{datetime.now().year}*')
sleep(2)
pyautogui.write(f' *NAO SE ESQUECA, ELA VENCE NO DIA 10* ')
sleep(5)

# Enviando o anexo
pyautogui.press('enter')  # Confirma a seleção do arquivo


# Aguarde alguns segundos para o arquivo ser enviado
sleep(5)

# Feche o WhatsApp
pyautogui.hotkey('alt', 'f4')

# FIM DO PROGRAMA ------------------------------------------------------------------------------------------------------
