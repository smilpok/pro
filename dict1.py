#Программа считывает одну строку со стандартного ввода и выводит для каждого уникального слова в этой строке число его повторений (без учёта регистра) в формате "слово количество".
#Порядок вывода слов может быть произвольным, каждое уникальное слово﻿  выводится только один раз. 

a=input().lower().split()
d={}
for value in range(len(a)):
    d[a[value]]=a.count(a[value])
for i in d:
    print(i,d[i])
