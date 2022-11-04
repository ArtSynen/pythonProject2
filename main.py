list_= list('абвгґдеєжзиійїклмнопрстуфхцчшщьюя')
list__ = list('abcdefghijklmnopqrstuvwxyz')
message = str(input('Введіть текст '))
message_ = list(message)
length1 = len(list_)
length2 = len(list__)
length3 = len(message_)
upper = ''
for i in range(0, length1):
    if message_[0] == list_[i]:
        upper = 'ukr'
for i in range(0, length2):
    if message_[0] == list__[i]:
        upper = 'eng'
if upper == 'ukr':
    for i in range(0, length3):
        for j in range(0, length1):
            if message_[i] == list__[j]:
                message_[i] = list__[j + 1]
                break
elif upper == 'eng':
    for i in range(0, length3):
        for j in range(0, length2):
            if message_[i] == list__[j]:
                message_[i] = list__[j + 1]
                break

print(''.join(message_))