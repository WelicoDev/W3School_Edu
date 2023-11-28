# UTF-8 qatorni kodlaydi:

txt = "My name is Stale"

x = txt.encode()
print(x)

# Ta'rifi va qo'llanilishi
# Usul encode()belgilangan kodlashdan foydalanib, satrni kodlaydi. Agar kodlash belgilanmagan bo'lsa, UTF-8 ishlatiladi.

# Sintaksis
# string.encode(encoding=encoding, errors=errors)