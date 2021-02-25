import sys, os

if len(sys.argv) < 2:
	print(f'Please use {sys.argv[0]} <file>')
	exit(255)

if os.path.exists(sys.argv[1]):
	exit(0)
exit(1)