
            
            
            
            
            
            
   




import random
while True:
    print("o'ynashni hoxlaysizmi ha yoki yo'q")
    qwert = input(">>>")
    if qwert == "ha":
        def son_t(x=10):
            tasod_son=random.randint(1, x)
            print(f"Men 1 dan {x} gacha son o'yladin. Topishga urinib kuring")
            urinishlar = 0
            while True:
                urinishlar += 1
                urinish = int(input(">>>"))
                if urinish > tasod_son:
                    print("xato...Men o'ylagan son bu sondan kechikroq")
                elif urinish < tasod_son:
                    print("Xato...Men o'ylagan son bu sondan kattaroq")
                else:
                    break  
            print(f"Tabriklaymiz... siz {urinishlar}ta da topdingiz ")
        def m_son(x=10):
            input(f"1 dan {x} gacha son uylang men topaman")
            quyi = 1
            yuqo = x
            urinish=0
            while True:
                urinish += 1
                if quyi != yuqo:
                    k_taxmin =random.randint(quyi, yuqo)
                else:
                    k_taxmin=quyi
                natija = input(f"Siz {k_taxmin} sonini o'yladingiz; to'g'ri bo'lsa (t)harfini bosing"
                               f"Men o'ylagan o'ylagan son kattaroq bo'lsa(+), yoki kichikroq bo'lsa(-)")
                if natija=="-":
                    yuqo = k_taxmin-1
                elif natija=="+":
                    quyi=k_taxmin+1
                else:
                    break
            print(f"Men {urinish} ta da topdim" )
            return urinish
        def hisob(x=10):
            qwert =True
            while qwert:
                tax1 = son_t(x)
                tax2 = m_son(x)
                if tax1>tax2:
                    print("Men yudim  ha tupoy kompeyuterniyam yutolmading axmoq")
                elif tax1<tax2:
                    print("Siz yutdingiz! sizga chaynalgan saqich yutib oldingiz... Tabriklaymiz")
                else:
                    print("Durang! ha tupoy kompeyuterniyam yutolmading axmoq")
                qwert =int(input("yana uynaymizma ha=1 yo'q=0"))
            
            
            
            
            
            
            
            
            
            
            
    else:
        break

    hisob()








