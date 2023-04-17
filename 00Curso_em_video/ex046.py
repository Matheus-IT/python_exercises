from time import sleep
import emoji
for c in range(10, 0, -1):
    print('|{:2}|'.format(c))
    sleep(1)
print(emoji.emojize(':fireworks::fireworks::fireworks:', use_aliases=True))
print(emoji.emojize(':fireworks::fireworks::fireworks:', use_aliases=True))
