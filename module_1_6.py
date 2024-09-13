date_of_birth = { 'Polya' : 1999, 'max' : 2003,'Laplas' : 777 ,"black_cat" : 666}
print(date_of_birth)
print(date_of_birth['Laplas'])
print(date_of_birth.get('Mr.Kukumber'))
date_of_birth['Royho'] = 1992   #если в словаре обратится к несуществующему ключу,то он его просто создает,и добавляет к основному словарю
date_of_birth.update({"Kolin" : 1899 , "Nibelung" : -233})
print(date_of_birth)
a = date_of_birth.pop('Kolin')
print(date_of_birth)
print(a)



my_set = {232,4432,"Kolin",'NoneKolin',9933.323,3434.555,9933.323,232,'Kolin'}
print(my_set)
my_set.update({'Aplle'},{(444,333)})
my_set.discard('Aplle')
print(my_set)
#множества не содержат повторяющихся элементов(хранит ун. значения,разные типы(картежи,списки))
