import random

def question():
    answer=input("What is your question?")
    strrr="● Cannot predict now● Concentrate and ask again● Don't count on it● My reply is no● My sources say no● Outlook not so good● Very doubtful"
    ans_list=strrr.split('●')
    final_answer=random.choice(ans_list)
    return final_answer

question()
