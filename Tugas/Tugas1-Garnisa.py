#!/usr/bin/env python
# coding: utf-8

# ## TUGAS 1

# In[ ]:


print('TUGAS 1 - GARNISA')
print("")
print("")


# ### Nomer 1

# In[1]:


print('Nomer 1')
print("")

Nama = str(input("Nama: "))
Umur = int(input("Umur: "))
Tinggi = float(input("Tinggi: "))

print("Nama saya",Nama,end=", ")
print("umur saya",Umur,"tahun dan ", end="")
print("tinggi saya",Tinggi,end=" cm.")
print("")
print("")


# ### Nomer 2

# In[2]:


print('Nomer 2')
print("")

r = int(input("Masukkan jari-jari lingkaran dalam cm: "))
phi = 22/7
luas = phi*r*r
print("Luas lingkaran dengan jari-jari", r,"cm adalah ", end="")
print(round(luas, 2), end=" ")
print("cm""\u00b2", end=".")

print("")
print("")


# ### Nomer 3

# In[4]:


print('Nomer 3')
print("")
a = float(input("Nilai ujian teori :"))
b = float(input("Nilai ujian praktek :"))

if a >= 70 and b >= 70:
    print("Selamat, anda lulus!")
elif a >= 70 and b < 70:
    print("Anda harus mengulang ujian praktek.")  
elif a < 70 and b >= 70:
    print("Anda harus mengulang ujian teori.")
else:
    print("Anda harus mengulang ujian teori dan praktek.")
    
print("")
print("")


# ### Soal Bonus

# In[14]:


print('Soal Bonus')

t = int(input("Ketinggian piramid adalah :"))

#spasi
s = t - 1

for i in range(1, t + 1):
    for j in range(0, s):
        print(' ', end='')
    s -= 1
   
    for j in range(0, i):
        print("* ", end='')
    
    print('')
    print('')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




