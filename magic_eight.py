import random

def question():
	answer = input("What is your question?")
	ans_list = ["Yes definitely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy try again", "Ask again later", "Better not tell you now"]
	final_answer = random.choice(ans_list)
	return final_answer