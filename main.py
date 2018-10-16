file = open("text.txt")
text = file.read()
#text = input()                              #ввожу текст
words = text.split()                        #делю текст на слова по пробелам
b = {}                                      #создаю пустой массив
y = 1                                       #указываю, что изначальное значение каждого ключа равно 1
for i in range(len(words)):                 #перебираю слова из списка
    if words[i] not in b:                  
        b[words[i]] = y                     #добавляю в словарь новый ключ - слово из списка и присваиваю ему значение
    else:
        b[words[i]] += 1                    #иначе значение этого ключа увеличивается на 1
print('В вашем тексте:')
for w in sorted(b, key=b.get, reverse=True):
    print('"',w,'" встречается ', b[w], ' раз(а).')
