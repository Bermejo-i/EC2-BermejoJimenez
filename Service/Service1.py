def calcular(hora,minut):
    if minut!=0:
        return (((hora*60 + minut)//60)+1)*1.5
    else:
        return hora*1.5
    
    