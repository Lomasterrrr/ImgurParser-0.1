import os
import random
import string
import requests 
import time
import urllib.request

os.system('cls')
print()
print("    ██▓     ▒█████   ███▄ ▄███▓ ▄▄▄        ██████ ▄▄▄█████▓▓█████  ██▀███  ")
time.sleep(0.3)
print("   ▓██▒    ▒██▒  ██▒▓██▒▀█▀ ██▒▒████▄    ▒██    ▒ ▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒")
time.sleep(0.3)
print("   ▒██░    ▒██░  ██▒▓██    ▓██░▒██  ▀█▄  ░ ▓██▄   ▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒")
time.sleep(0.3)
print("   ▒██░    ▒██   ██░▒██    ▒██ ░██▄▄▄▄██   ▒   ██▒░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄  ")
time.sleep(0.3)
print("   ░██████▒░ ████▓▒░▒██▒   ░██▒ ▓█   ▓██▒▒██████▒▒  ▒██▒ ░ ░▒████▒░██▓ ▒██▒")
time.sleep(0.3)
print("   ░ ▒░▓  ░░ ▒░▒░▒░ ░ ▒░   ░  ░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░  ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░")
time.sleep(0.3)
print("   ░ ░ ▒  ░  ░ ▒ ▒░ ░  ░      ░  ▒   ▒▒ ░░ ░▒  ░ ░    ░     ░ ░  ░  ░▒ ░ ▒░")
time.sleep(0.3)
print("     ░ ░   ░ ░ ░ ▒  ░      ░     ░   ▒   ░  ░  ░    ░         ░     ░░   ░ ")
time.sleep(0.4)
print(" Beta 0.1  ░  ░    ░ ░         ░         ░  ░      ░              ░  ░   ░   ")
time.sleep(0.4)
print(' ---------------------------------------------------------------------------')
print(' [1] - i.imgur.com')
print(' [2] - Help  ')
print(' [3] - Exit')
print(' ---------------------------------------------------------------------------')
what = input(' Enter: ')
if what == "1":
	length = 5
	os.system('cls')
	print()
	print("    ██▓     ▒█████   ███▄ ▄███▓ ▄▄▄        ██████ ▄▄▄█████▓▓█████  ██▀███  ")
	print("   ▓██▒    ▒██▒  ██▒▓██▒▀█▀ ██▒▒████▄    ▒██    ▒ ▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒")
	print("   ▒██░    ▒██░  ██▒▓██    ▓██░▒██  ▀█▄  ░ ▓██▄   ▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒")
	print("   ▒██░    ▒██   ██░▒██    ▒██ ░██▄▄▄▄██   ▒   ██▒░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄  ")
	print("   ░██████▒░ ████▓▒░▒██▒   ░██▒ ▓█   ▓██▒▒██████▒▒  ▒██▒ ░ ░▒████▒░██▓ ▒██▒")
	print("   ░ ▒░▓  ░░ ▒░▒░▒░ ░ ▒░   ░  ░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░  ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░")
	print("   ░ ░ ▒  ░  ░ ▒ ▒░ ░  ░      ░  ▒   ▒▒ ░░ ░▒  ░ ░    ░     ░ ░  ░  ░▒ ░ ▒░")
	print("     ░ ░   ░ ░ ░ ▒  ░      ░     ░   ▒   ░  ░  ░    ░         ░     ░░   ░ ")
	print(" Beta 0.1  ░  ░    ░ ░         ░         ░  ░      ░              ░  ░   ░   ")
	print(' ---------------------------------------------------------------------------')
	print(' [1] - .png')
	print(' [2] - .jpg  ')
	print(' [3] - .gif')
	print(' [4] - .all ')
	print(' ---------------------------------------------------------------------------')
	whatt = input(" Enter: ")
	os.system('cls')
	print()
	print("    ██▓     ▒█████   ███▄ ▄███▓ ▄▄▄        ██████ ▄▄▄█████▓▓█████  ██▀███  ")
	print("   ▓██▒    ▒██▒  ██▒▓██▒▀█▀ ██▒▒████▄    ▒██    ▒ ▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒")
	print("   ▒██░    ▒██░  ██▒▓██    ▓██░▒██  ▀█▄  ░ ▓██▄   ▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒")
	print("   ▒██░    ▒██   ██░▒██    ▒██ ░██▄▄▄▄██   ▒   ██▒░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄  ")
	print("   ░██████▒░ ████▓▒░▒██▒   ░██▒ ▓█   ▓██▒▒██████▒▒  ▒██▒ ░ ░▒████▒░██▓ ▒██▒")
	print("   ░ ▒░▓  ░░ ▒░▒░▒░ ░ ▒░   ░  ░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░  ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░")
	print("   ░ ░ ▒  ░  ░ ▒ ▒░ ░  ░      ░  ▒   ▒▒ ░░ ░▒  ░ ░    ░     ░ ░  ░  ░▒ ░ ▒░")
	print("     ░ ░   ░ ░ ░ ▒  ░      ░     ░   ▒   ░  ░  ░    ░         ░     ░░   ░ ")
	print(" Beta 0.1  ░  ░    ░ ░         ░         ░  ░      ░              ░  ░   ░   ")
	print(' ---------------------------------------------------------------------------')
	if whatt == '1':
		while True:
			start_time = time.time()
			letters_and_digits = string.ascii_letters + string.digits
			rand_string = ''.join(random.sample(letters_and_digits, length))

			url = " https://i.imgur.com/" + rand_string + ".png"
			destination = rand_string + '.png'
			urllib.request.urlretrieve(url, destination)
			r = requests.get(url) 
			result = url + ' ' + str(r.status_code) + " | Downloaded for: " + str((time.time() - start_time))
			print(result)

	if whatt == '2':
		while True:
			#jpg
			start_time = time.time()		
			letters_and_digits = string.ascii_letters + string.digits
			rand_string = ''.join(random.sample(letters_and_digits, length))

			url = " https://i.imgur.com/" + rand_string + ".jpg"
			destination = rand_string + '.jpg'
			urllib.request.urlretrieve(url, destination)
			r = requests.get(url) 
			result = url + ' ' + str(r.status_code) + " | Downloaded for: " + str((time.time() - start_time)) 
			print(result)

	if whatt == '3':
		while True:
			#gif
			start_time = time.time()		
			letters_and_digits = string.ascii_letters + string.digits
			rand_string = ''.join(random.sample(letters_and_digits, length))

			url = " https://i.imgur.com/" + rand_string + ".gif"
			destination = rand_string + '.gif'
			urllib.request.urlretrieve(url, destination)
			r = requests.get(url) 
			result = url + ' ' + str(r.status_code) + " | Downloaded for: " + str((time.time() - start_time)) 
			print(result)

	if whatt == '4':
		while True:
			#png
			start_time = time.time()
			letters_and_digits = string.ascii_letters + string.digits
			rand_string = ''.join(random.sample(letters_and_digits, length))

			url = " https://i.imgur.com/" + rand_string + ".png"
			destination = rand_string + '.png'
			urllib.request.urlretrieve(url, destination)
			r = requests.get(url) 
			result = url + ' ' + str(r.status_code) + " | Downloaded for: " + str((time.time() - start_time))
			print(result)

			#jpg
			start_time = time.time()		
			letters_and_digits = string.ascii_letters + string.digits
			rand_string = ''.join(random.sample(letters_and_digits, length))

			url = " https://i.imgur.com/" + rand_string + ".jpg"
			destination = rand_string + '.jpg'
			urllib.request.urlretrieve(url, destination)
			r = requests.get(url) 
			result = url + ' ' + str(r.status_code) + " | Downloaded for: " + str((time.time() - start_time)) 
			print(result)
	        
	        #gif
			start_time = time.time()		
			letters_and_digits = string.ascii_letters + string.digits
			rand_string = ''.join(random.sample(letters_and_digits, length))

			url = " https://i.imgur.com/" + rand_string + ".gif"
			destination = rand_string + '.gif'
			urllib.request.urlretrieve(url, destination)
			r = requests.get(url) 
			result = url + ' ' + str(r.status_code) + " | Downloaded for: " + str((time.time() - start_time)) 
			print(result)


if what == "2":
	length = 6
	os.system('cls')
	print()
	print("    ██▓     ▒█████   ███▄ ▄███▓ ▄▄▄        ██████ ▄▄▄█████▓▓█████  ██▀███  ")
	print("   ▓██▒    ▒██▒  ██▒▓██▒▀█▀ ██▒▒████▄    ▒██    ▒ ▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒")
	print("   ▒██░    ▒██░  ██▒▓██    ▓██░▒██  ▀█▄  ░ ▓██▄   ▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒")
	print("   ▒██░    ▒██   ██░▒██    ▒██ ░██▄▄▄▄██   ▒   ██▒░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄  ")
	print("   ░██████▒░ ████▓▒░▒██▒   ░██▒ ▓█   ▓██▒▒██████▒▒  ▒██▒ ░ ░▒████▒░██▓ ▒██▒")
	print("   ░ ▒░▓  ░░ ▒░▒░▒░ ░ ▒░   ░  ░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░  ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░")
	print("   ░ ░ ▒  ░  ░ ▒ ▒░ ░  ░      ░  ▒   ▒▒ ░░ ░▒  ░ ░    ░     ░ ░  ░  ░▒ ░ ▒░")
	print("     ░ ░   ░ ░ ░ ▒  ░      ░     ░   ▒   ░  ░  ░    ░         ░     ░░   ░ ")
	print(" Beta 0.1  ░  ░    ░ ░         ░         ░  ░      ░              ░  ░   ░   ")
	print(' ---------------------------------------------------------------------------')

if what == "3":
	length = 6
	os.system('cls')
	print()
	print("    ██▓     ▒█████   ███▄ ▄███▓ ▄▄▄        ██████ ▄▄▄█████▓▓█████  ██▀███  ")
	print("   ▓██▒    ▒██▒  ██▒▓██▒▀█▀ ██▒▒████▄    ▒██    ▒ ▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒")
	print("   ▒██░    ▒██░  ██▒▓██    ▓██░▒██  ▀█▄  ░ ▓██▄   ▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒")
	print("   ▒██░    ▒██   ██░▒██    ▒██ ░██▄▄▄▄██   ▒   ██▒░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄  ")
	print("   ░██████▒░ ████▓▒░▒██▒   ░██▒ ▓█   ▓██▒▒██████▒▒  ▒██▒ ░ ░▒████▒░██▓ ▒██▒")
	print("   ░ ▒░▓  ░░ ▒░▒░▒░ ░ ▒░   ░  ░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░  ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░")
	print("   ░ ░ ▒  ░  ░ ▒ ▒░ ░  ░      ░  ▒   ▒▒ ░░ ░▒  ░ ░    ░     ░ ░  ░  ░▒ ░ ▒░")
	print("     ░ ░   ░ ░ ░ ▒  ░      ░     ░   ▒   ░  ░  ░    ░         ░     ░░   ░ ")
	print(" Beta 0.1  ░  ░    ░ ░         ░         ░  ░      ░              ░  ░   ░   ")
	print(' ---------------------------------------------------------------------------')
	print(' Удачи!')
	time.sleep(2)
	raise SystemExit


