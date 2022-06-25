c = float(input('\033[1;32mInforme a temperatura em °C:\033[m'))
f = (c * 9/5) + 32
print('\033[1;32mA temperatura de {}°C corresponde a {:.1f}°F!\033[m'.format(c, f))
