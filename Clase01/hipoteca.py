# hipoteca.py
# Ejercicio de hipoteca (final 1.11)

nombre = "Naranja"
cajones = 100
precio = 91.1
print(f"{cajones} cajones de {nombre} a ${precio:0.2f}")


saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes = 0

pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000

while saldo > 0:
    mes = mes + 1
    if saldo > pago_mensual:
        if (mes >= pago_extra_mes_comienzo) & (mes <= pago_extra_mes_fin):
            saldo = saldo * (1 + tasa / 12) - pago_mensual - pago_extra
            total_pagado = total_pagado + pago_mensual + pago_extra
        else:
            saldo = saldo * (1 + tasa / 12) - pago_mensual
            total_pagado = total_pagado + pago_mensual
    else:
        pago_mensual = saldo
        saldo = saldo - pago_mensual

    print(
        f"Mes: {mes}. Total pagado: ${round(total_pagado, 2)}. Saldo a pagar: ${round(saldo, 2)}"
    )

print(f"El total pagado es {round(total_pagado, 2)}. Se pagó en {mes} meses.")
