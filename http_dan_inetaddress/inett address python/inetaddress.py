import socket as s
import platform
host = 'google.com'


# LocalIP = ''.join(s.gethostbyname_ex(s.gethostname())[2])

# print(LocalIP)

print(f'IP alamat web host  {host} is : {s.gethostbyname(host)}')
print('')
print('alamat lokal : ')
print(platform.node())
print(s.gethostbyname(s.gethostname()))
print('')

print(f'{host} :')
alamat = s.gethostbyaddr(host)
for x in alamat :
  print(x)


