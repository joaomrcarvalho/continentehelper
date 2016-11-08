import time
import webbrowser

login_url = "http://www.continente.pt"
webbrowser.open(login_url)

# tempo para fazer login no site
time.sleep(7)

path_ficheiro_compras = "~/Dropbox/lista_compras.txt"
base_search_url = "https://www.continente.pt/pt-pt/public/Pages/searchresults.aspx?k="
items_a_comprar = [line.rstrip('\n') for line in open(path_ficheiro_compras)]

for item_a_comprar in items_a_comprar:
    tmp_url = base_search_url + item_a_comprar.replace(" ", "%20")
    webbrowser.open(tmp_url)
