from barcode import EAN13
from barcode.writer import ImageWriter

dic_produtos = {
    'Feijão': '263862315909',
    'Arroz': '690023420846',
    'Macarrão': '267497923714',
    'Azeite': '562711161854'
}

for produto in dic_produtos:
    codigo_barra = EAN13(f'{dic_produtos[produto]}', writer=ImageWriter())
    codigo_barra.save(produto)

