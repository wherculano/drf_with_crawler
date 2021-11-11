from time import sleep

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

from app.models import Notebook


class Crawler:
    def __init__(self, modelo):
        self.url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops'
        self.modelo = modelo
        self.notebook = Notebook

    def access_url(self):
        links = []
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        driver = Firefox(options=options)
        driver.get(self.url)
        main_div = driver.find_elements_by_xpath('//*[@class="row"]')[2]
        div_caption = main_div.find_elements_by_class_name('caption')

        for elem in div_caption:
            if self.modelo.lower() in elem.text.lower():
                for link in elem.find_elements_by_tag_name('a'):
                    links.append(link.get_attribute('href'))

        for l in links:
            driver.get(l)
            sleep(2)
            div_caption_header = driver.find_element_by_class_name('caption')
            valor_principal = div_caption_header.find_elements_by_tag_name('h4')[0].text.replace('$', '')
            modelo = div_caption_header.find_elements_by_tag_name('h4')[1].text

            descricao = driver.find_element_by_class_name('description').text
            avaliacoes = driver.find_element_by_xpath('//*[@class="ratings"]')
            nota = len(avaliacoes.find_elements_by_tag_name('span'))

            btn_hdd = driver.find_elements_by_class_name('swatches')

            for btn in btn_hdd:
                armazenamento = btn.find_elements_by_class_name('swatch')
                dct_hdds = {}
                for btn_arm in armazenamento:
                    if btn_arm.value_of_css_property('cursor') != 'not-allowed':
                        btn_arm.click()
                        valor = driver.find_element_by_xpath('//*[@class="pull-right price"]').text.replace('$', '')
                        dct_hdds[btn_arm.text + ' GB'] = float(valor)

                self.notebook.objects.create(**{
                    'modelo': modelo, 'descricao': descricao, 'valor': valor_principal, 'nota': nota, 'hdd': dct_hdds,
                    'avaliacoes': avaliacoes.text.split()[0]
                })

                break

        driver.quit()
        return
