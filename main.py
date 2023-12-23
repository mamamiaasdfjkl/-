#{Style.RESET_ALL} - в конце писать что бы остановить окрашивание букв
from PIL import Image, ImageFont, ImageDraw
from colorama import Fore, Style
print(f'{Fore.MAGENTA}Генератор мемов запущен.')

a = input('Если вы хотите текст и снизу, и сверху то напишите цифру 1, а если хотите только внизу цифру 2.Введите цифру:')
toptext = ''
bottomtext = ''

if a == '1':
    toptext = input('Введите что вы хотите написать на меме сверху:')
    bottomtext = input('Введите что вы хотите написать на меме снизу:')
elif a == '2':
    bottomtext = input('Введите что вы хотите написать на меме снизу:')
else:
    print(f'{Fore.CYAN}ДРУГИЕ ЧИСЛА ЗДЕСЬ ЗАПРЕЩЕНЫ{Style.RESET_ALL}')
    quit()

picters = ['Кот в ресторане.png', 'Кот в очках.png', 'злой кэт.jpg', 'СОНЯ.jpg', 'обезьяна.jpg']
print('Выберите картинку:')
for i in range(5):
    print(i,picters[i])
q = int(input('Введите номер картинки:'))
toptext = toptext.replace('краски', 'карандаши')
bottomtext = bottomtext.replace('краски', 'карандаши')

cat = Image.open(picters[q])
x, y = cat.size

catdraw = ImageDraw.Draw(cat)
font = ImageFont.truetype('arial.ttf', size=60)
text1 = catdraw.textbbox((0, 0), toptext, font)
text2 = catdraw.textbbox((0, 0), bottomtext, font)


d = input('если хотите надпись в начале напишите цифру 3, если хотите  в середине цифру 4, а если в конце 5:')
if d == '3':
     catdraw.text((0, 10), toptext, font = font, fill = 'black', stroke_width=6, stroke_fill='white' )
     catdraw.text((0, y - text2[3] - 10), bottomtext, font = font, fill = 'black', stroke_width=6, stroke_fill='white')
elif d == '4':
     catdraw.text(((x - text1[2]) / 2, 10),toptext, font = font, fill = 'black', stroke_width=6, stroke_fill='white')
     catdraw.text(((x - text2[2]) / 2, (y - text2[3] - 10)),bottomtext, font = font, fill = 'black',  stroke_width=6, stroke_fill='white')

elif d == '5':
     catdraw.text((x - text1[2] - 10, 10), toptext, font=font, fill='black', stroke_width=6, stroke_fill='white')
     catdraw.text((x - text2[2] - 10, y - text2[3] - 10), bottomtext, font=font, fill='black', stroke_width=6, stroke_fill='white' )
else:
     print(f'{Fore.CYAN}ДРУГИЕ ЧИСЛА ЗДЕСЬ ЗАПРЕЩЕНЫ{Style.RESET_ALL}')
     quit()

cat.show()

print(toptext,bottomtext)

#cat.save('f_мемчик.jpg')


