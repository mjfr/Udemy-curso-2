from bs4 import BeautifulSoup
with open(file="website.html", mode="r") as data:
    html_contents = data.read()
print(html_contents)

soup = BeautifulSoup(markup=html_contents, parser="html.parser")
'''
Também poderia ser usado um lxml.parser caso o markup usado fosse um xml. Também deveríamos importar o módulo lxml.
Comentando em multilinha pois parece que comentários normais causam conflito caso possuam a palavra xml
'''
# Tag completa
print(soup.title)
# Nome da tag
print(soup.title.name)
# Conteúdo da tag
print(soup.title.string)
# Retorna apenas o primeiro anchor-tag, mesmo que haja mais que um.
print(soup.a)

# Name recebe o nome de qualquer tag do site.
all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)

for tag in all_anchor_tags:
    # Pega apenas o texto da anchor-tag
    print(tag.getText())
    # Pega apenas o href da anchor-tag
    print(tag.get("href"))

# Também é possível pegar dados através de atributos
heading = soup.find(name="h1", id="name")
print(heading)

# Como class é uma palavra reservada do Python, foi-se usada o kwarg class_
section_heading = soup.find(name="h3", class_="heading")
print(section_heading)
print(section_heading.getText())

# Usando seletores do CSS, select_one nos retorna apenas o primeiro achado e o select retorna todos os achados.
company_url = soup.select_one(selector="p a")
print(company_url)

# Também podemos usar classes e ids
name = soup.select_one(selector="#name")
print(name)

# Recuperando todos os elementos que possuam a classe heading
heading_ = soup.select(selector=".heading")
print(heading_)
