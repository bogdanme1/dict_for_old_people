meme_dict = {
            "КРИНЖ": "Что-то очень странное или стыдное",
            "ЛОЛ": "Что-то очень смешное",
            "КАКАШКА" : "плохой",
            "ЧЕЛ" : "достал",
            "ПОГНАЛИ" : "Пошли"
            }
            
word = input("Какое слово хотите узнать")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("такого слова нету")
