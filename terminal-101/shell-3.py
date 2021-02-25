while True:
	args = input('> ').split(' ')
	args[0] = args[0].lower()
	if args[0] == 'echo':
		print(' '.join(args[1:]))
	elif args[0] == 'ping':
		print('pong')
	elif args[0] == 'exit':
		print('bye :)')
		exit()
	elif args[0] == 'help' or args[0] == '?':
		print('Available commands:')
		print(' * echo [args...] - Echo args back to you')
		print(' * ping - pong')
		print(' * exit - exit shell')
	else:
		print(f'Unknown command "{args[0]}"')
		print('Use "help" for list of commands')