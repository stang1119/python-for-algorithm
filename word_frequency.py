mytext= '''
where have all the flowers gone
long time passing
where have all the flowers gone
long time ago
where have all the flowers gone
young girls picked them every one
when will they ever learn
when will they ever learn
where have all the young girls gone
long time passing
where have all the young girls gone
long time ago
where have all the young girls gone
gone to young men every one
when will they ever learn
when will they ever learn
where have all the young men gone
long time passing
where have all the young men gone
long time ago
where have all the young men gone
gone for soldiers every one
when will they ever learn
when will they ever learn
where have all the soldiers gone
long time passing
where have all the soldiers gone
long time ago
where have all the soldiers gone
gone to graveyards every one
when will they ever learn
when will they ever learn
where have all the graveyards gone
long time passing
where have all the graveyards gone
long time ago
where have all the graveyards gone
gone to flowers every one
when will they ever learn
when will they ever learn
'''
mytext_lower= mytext.lower()  # transform to lower case
mytext_lower= mytext_lower.replace(',', ' ').replace('?', ' ')
mytext_list= mytext_lower.split()  # split to a word list
mytext_set= set(mytext_list)  # become a word set
mytext_dict= {}
for word in mytext_set:
    mytext_dict[word] = mytext_list.count(word)
    #print("%15s %5d"%(word, mytext_dict[word]))
#print(mytext_dict)
#print(mytext_dict.items())
print("number of distinct words: ",len(mytext_dict))
mytext_dict_sort= sorted(mytext_dict.items(), key=lambda d:d[1], reverse=True) 
for wf in mytext_dict_sort:
    if wf[1] > 1:
        print(wf)
