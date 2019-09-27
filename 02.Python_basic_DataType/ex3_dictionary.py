dict = { 'name':'pey',
        'phone':'01010101010',
        'birth':'0102'
}

print(dict)     # {'name': 'pey', 'phone': '01010101010', 'birth': '0102'}

print(dict['name'])         # pey

dict['name'] = 'jhone'
print(dict['name'])         # jhone
######################################

grade = {'pey':10, 'julliet':99}
print(grade)                # {'pey': 10, 'julliet': 99}
print(grade['pey'])         # 10
print(grade['julliet'])     # 99

names = grade.keys()
print(names)              # dict_keys(['pey', 'julliet'])

nameList = list(names)
print(nameList[0])          # pey

scores = grade.values()
print(scores)           # dict_values([10, 99])

scoreList = list(scores)
print(scoreList)        # [10, 99]

print(grade.get('pey'))     # 10

print(grade.get('me'))      # None
print(grade.get('me','0'))  # 0    <- if tuple has not key return the default value

if 'pey' in grade:
    print(True)             # True

grade.clear()
print(grade)            # {}
