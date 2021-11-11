from django.shortcuts import redirect

from crawler import Crawler


def iniciar_crawler(request, modelo):
    crawler = Crawler(modelo)
    crawler.access_url()
    return redirect('/notebooks/?ordering=-valor')
