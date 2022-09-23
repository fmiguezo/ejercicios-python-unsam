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
    if (mes >= pago_extra_mes_comienzo) & (mes <= pago_extra_mes_fin):
        saldo = saldo * (1 + tasa / 12) - pago_mensual - pago_extra
        total_pagado = total_pagado + pago_mensual + pago_extra
    else:
        saldo = saldo * (1 + tasa / 12) - pago_mensual
        total_pagado = total_pagado + pago_mensual

print("Total pagado", round(total_pagado, 2), "en", mes, "meses")
