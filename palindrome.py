def is_palindrome(teks):
     teks_bersih = "".join(char.lower() for char in teks if char.isalnum())

     teks_terbalik = teks_bersih[::-1]

     return teks_bersih == teks_terbalik

kata = input("Masukan Kata atau Kalimat: ")

if is_palindrome(kata):
     print(f"Mantap, '{kata}' itu adalah Palindrome!")
else:
     print(f"Yah, '{kata}' itu Bukan Palindrome.")