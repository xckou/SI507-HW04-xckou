import random

def question():
    answer=input("What is your question?")
    ans_list = ["Yes definitely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes",
                "Signs point to yes", "Reply hazy try again", "Ask again later", "Better not tell you now"]

    strrr="● It is certain● It is decidedly so● Without a doubt● Cannot predict now● Concentrate and ask again● Don't count on it● My reply is no● My sources say no● Outlook not so good● Very doubtful"
    ans_list=ans_list+strrr.split('●')
    final_answer=random.choice(ans_list)
    return final_answer

question()
