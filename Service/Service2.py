''''Un En un almacén se rebaja 10% del precio al cliente si compra mayor a 20 
artículos y 5% si compra hasta 20 artículos, pero más de 10. 
Ingrese el precio unitario de un artículo y la cantidad adquirida y 
muestre lo que debe pagar el cliente. '''''
def total(pu,cant):
    if cant>20:
        return pu*cant*0.9
    elif cant>10 and cant<=20:
        return pu*cant*0.95
    else:
        return pu*cant