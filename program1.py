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
