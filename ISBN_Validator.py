isbnKodu=[9,7,8,6,0,5,6,1,8,0,1,8]


a = 0 #Dikkat ettiyseniz pozisyon olarak çift sayılarda
      # 3 ile çarpıyoruz, bu satır sayının tekliğini
      # çiftliğini kontrol etmek için.

toplam= 0 

for i in range(len(isbnKodu)):
  
  if a % 2 == 1:  
    toplam = toplam + (isbnKodu[i]*3)  

    a = a + 1
  
    #Eğer şu an bulunduğum pozizyon tek ise
    # 3 ile çarp ve toplama ekle
    # Python sayıları saymaya 0'dan başladığını unutmayın
    # Bu yüzden tek sayıları kontrol ediyoruz.

  else:
    toplam = toplam + isbnKodu[i]

    a = a + 1
    # Eğer bulunduğum pozisyon çift bir sayı ise 
    # olduğu gibi topla
  


if toplam % 10 == 0 :
  print("Bu ISBN kodu GEÇERLİDİR!")
else:
  print("Bu ISBN kodu GEÇERESİZDİR!")

  # Eğer tüm bu işlemlerden sonra 'toplam' ifadesinin 10'a
  # bölümünden kalan 0 ise ISBN kodu geçerlidir.
  # Eğer 0'a eşit değilse geçersizdir.
