def question():
	answer = input("What is your question?")
	if answer[-1] != "?":
		print("I’m sorry, I can only answer questions.")
	while answer !="quit":
		answer = input("What is your question?")
		if answer == "quit":
			return
		elif answer[-1] != "?":
			print("I’m sorry, I can only answer questions.")
question()