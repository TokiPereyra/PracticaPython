# hipoteca.py
# Archivo de ejemplo
# Ejercicio de hipoteca
saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
primer_año = 12
mes = 0

pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000

while saldo > 0:
    if primer_año>0:
        pago = pago_mensual + 1000
        saldo = saldo * (1+tasa/12) - pago
        total_pagado = total_pagado + pago
        mes = mes + 1
        primer_año = primer_año - 1
        print(mes, round(total_pagado, 2), round(saldo, 2))
    elif mes >= pago_extra_mes_comienzo and mes <= pago_extra_mes_fin:
        pag = pago_mensual + pago_extra
        saldo = saldo * (1+tasa/12) - pag
        total_pagado = total_pagado + pag
        mes = mes + 1
        print(mes, round(total_pagado, 2), round(saldo, 2))
    elif saldo - pago_mensual < 0:
        pag = saldo * (1+tasa/12)
        saldo = saldo * (1+tasa/12) - pag
        total_pagado = total_pagado + pag
        mes = mes + 1
        print(mes, round(total_pagado, 2), round(saldo, 2))
    else:
        saldo = saldo * (1+tasa/12) - pago_mensual
        total_pagado = total_pagado + pago_mensual
        mes = mes + 1
        print(mes, round(total_pagado, 2), round(saldo, 2))
print(f'Total cuotas: {mes}') 
print(f'Total pagado: {round(total_pagado, 2)}')  


    

