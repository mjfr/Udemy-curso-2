from selenium import webdriver

# Driver baixado do site: https://chromedriver.chromium.org/downloads

# É necessário especificar ao selenium o local do driver do navegador que escolhemos.
chrome_driver_path = "D:\\Python aprendizado\\Angela Yu\\100 Days of Code - The Complete Python Pro Bootcamp" \
                     " for 2022\\chromedriver.exe"
# O pacote do Selenium contém códigos que nos possibilita interagir com o navegador.
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Abre uma página no navegador
driver.get("https://www.amazon.com.br")

# Visto que terminamos o que estávamos fazendo no navegador, devemos fechar o driver
driver.close()

# Também há outro método: .quit() enquanto o .close() fecha apenas a aba, o .quit() fecha o navegador por completo
# driver.quit()
