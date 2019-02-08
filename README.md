Program mencari bilangan terbesar dari 3 buah bilangan

=>> ALur algoritmanya :


```
1. Mendefinisikan perulangan dengan mengetikkan :
	def pengulangan():
2. Memasukkan 3 buah bilangan yg di inginkan :
	print ('Masukkan 3 bilangan yang diinginkan!')
    a = input ("masukkan bilangan pertama :")
    b = input ("masukkan bilangan kedua :")
    c = input ("masukkan bilangan ketiga :")
3. Membandingkan nilai a,b,c dengan rumus if :
	    if a>b:
        if a>c:
            print('Bilangan terbesar adalah :',a)
        else:
            print('Bilangan terbesar adalah :',c)
    else:    
        if b>c:
            print('Bilangan terbesar adalah :',b)
        else:
            print('Bilangan terbesar adalah :',c)
4. Buat pilihan menu :
	  print ('Ingin coba lagi? (Ya/Tidak)')
    x=input()
    if x=='Ya':
        return pengulangan()
    if x=='Tidak':
        print('Terima kasih')
5. Lalu ketikkan "pengulangan()"
	agar program perulangan dapat berjalan
```


=>> Kode python :


```
print ('Program mencari nilai tertinggi dari 3 buah bilangan')

def pengulangan():
    print ('Masukkan 3 bilangan yang diinginkan!')
    a = input ("masukkan bilangan pertama :")
    b = input ("masukkan bilangan kedua :")
    c = input ("masukkan bilangan ketiga :")

    if a>b:
        if a>c:
            print('Bilangan terbesar adalah :',a)
        else:
            print('Bilangan terbesar adalah :',c)
    else:    
        if b>c:
            print('Bilangan terbesar adalah :',b)
        else:
            print('Bilangan terbesar adalah :',c)
        
    print ('')
    print ('Ingin coba lagi? (Ya/Tidak)')
    x=input()
    if x=='Ya':
        return pengulangan()
    if x=='Tidak':
        print('Terima kasih')

pengulangan()
```



=>> Hasil screenshoot program :

![mencari bilangan tertinggi dari 3 buah bilangan](https://user-images.githubusercontent.com/43899109/52463692-7d695300-2baa-11e9-855e-a96c818d835a.jpg)
