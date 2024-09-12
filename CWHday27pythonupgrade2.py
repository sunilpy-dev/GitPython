#Exercise 3
def ll(l,c1=0,c2=0,c3=0,c4=0):
    if(l==0):
        print("You have not choosen any life line")
    elif(c3==1):
        if(l==3):
            print(f"\"The correct ans according to me is: OPTION {crtanswers[i]}\"")
    elif(c1==1):
        if(l==1):
            ans.remove(ans[p1-1])
            ans.remove(ans[p2-1])
            for k in ans:
                print(k)
    elif(c4==1):
        if(l==4):
            print("Please enter two options as between (1-4) just like as(A-D):")
    elif(c2==1):
        if(l==2):
            print(f"The new question for {ammount[i]} is:")
            print(f"{question1[i]}")
            print("  ",end="")
            print(f"{ans2[0]}   {ans2[1]}")
            print(f"  {ans2[2]}   {ans2[3]}")
print("WELCOME TO THE KBC!!!")
print("\nINSTRUCTIONS:-\n1.You can not use one lifeline more than one\n2.You won't be given lifline in a lifeline\n3.Once you tried  to use lifline more than once then you will not get another lifeline in that question\n4.You can not use lifline to go from level 13 to level 14\n")
question=["1) Which planet is known as the red planaet?","2) In Indian mythology, who is the god of wisdom and beginnings?","3) Which river is also known as the Ganga in India?","4) What is the capital city of Australia","5) In which year did India gain independence from British rule?","6) Who is known as the \"Father of the Nation\" in India?","7) What is the largest mammal in the world?","8) Which famous scientist developed the theory of relativity?","9) Which Indian state is known as the \"Land of Five Rivers\"?","10) In cricket, what is the highest individual score in a Test match?","11) Who wrote the play \"Romeo and Juliet\"?","12) What is the chemical symbol for gold?","13) In which year did the Titanic sink?","14) Which famous painting features a woman with a mysterious smile?"]
question1=["Which river is considered the holiest in Hinduism?","Who was the first President of independent India?","Which Indian state is known as the \"Land of the Gods\"?","What is the national flower of India?","Who composed the Indian national anthem, \"Jana Gana Mana\"?","Which Indian city is known as the \"City of Lakes\"?","Who is known as the \"Nightingale of India\"?","What is the currency of India?","Which festival is known as the Festival of Lights in India?","Who was the first Indian woman to win an Olympic medal?","Which Indian state is known for its tea gardens?","Who is known as the \"Missile Man of India\"?","Which monument in India is also known as the \"Symbol of Love\"?","Who was the first Prime Minister of India?"]
answers=[["A) Venus", "B) Mars", "C) Jupiter", "D) Saturn"],["A) Shiva", "B) Brahma", "C) Vishnu", "D) Ganesha"],["A) Yamuna", "B) Godavari", "C) Saraswati", "D) Ganges"],["A) Sydney", "B) Melbourne", "C) Canberra", "D) Brisbane"],["A) 1945", "B) 1947", "C) 1950", "D) 1962"],["A) Jawaharlal Nehru", "B) Subhas Chandra Bose", "C) Mahatma Gandhi", "D) Sardar Patel"],["A) Elephant", "B) Blue Whale", "C) Giraffe", "D) Polar Bear"],["A) Isaac Newton", "B) Galileo Galilei", "C) Albert Einstein", "D) Marie Curie"],["A) Punjab", "B) Haryana", "C) Himachal Pradesh", "D) Uttarakhand"],["A) 299", "B) 311", "C) 400", "D) 400*"],["A) Charles Dickens", "B) William Shakespeare", "C) Jane Austen", "D) Mark Twain"],["A) Ag", "B) Au", "C) Fe", "D) Hg"],["A) 1910", "B) 1912", "C) 1920", "D) 1931"],[" A) Starry Night", "B) The Persistence of Memory", "C) The Last Supper", "D) Mona Lisa"]]
answers1=[["A) Yamuna","B) Ganges","C) Saraswati","D) Godavari"],["A) Jawaharlal Nehru","B) Dr. Rajendra Prasad","C) Sardar Patel","D) Dr. B.R. Ambedkar"],["A) Uttarakhand","B) Himachal Pradesh","C) Jammu and Kashmir","D) Arunachal Pradesh"],["A) Rose","B) Lotus","C) Lily","D) Jasmine"],["A) Rabindranath Tagore","B) Sarojini Naidu","C) Bankim Chandra Chattopadhyay","D) M. S. Subbulakshmi"],["A) Udaipur","B) Jaipur","C) Jodhpur","D) Bhopal"],["A) Lata Mangeshkar","B) Asha Bhosle","C) Sarojini Naidu","D) Indira Gandhi"],["A) Rupee","B) Rupiah","C) Taka","D) Baht"],["A) Diwali","B) Holi","C) Dussehra","D) Navratri"],["A) Mary Kom","B) Karnam Malleswari","C) Saina Nehwal","D) P. V. Sindhu"],["A) Assam","B) Kerala","C) Karnataka","D) Tamil Nadu"],["A) Dr. A.P.J. Abdul Kalam","B) Dr. Vikram Sarabhai","C) Dr. Homi J. Bhabha","D) Dr. Satish Dhawan"],["A) Qutub Minar","B) Red Fort","C) Taj Mahal","D) Hawa Mahal"],["A) Jawaharlal Nehru","B) Indira Gandhi","C) Rajiv Gandhi","D) Lal Bahadur Shastri"]]
crtanswers=[2,4,4,3,2,3,2,3,1,4,2,2,2,4]
crtanswers1=[2,2,1,2,1,1,3,1,1,2,1,1,3,1]
ammount=["5000Rs","10,000Rs","20,000Rs","40,000Rs","80,000Rs","1,60,000Rs","3,20,000Rs","6,40,000Rs","12,50,000Rs","25,00,000Rs","50,00,000Rs","1,00,00,000Rs","3,00,00,000Rs","7,00,00,000Rs"]
lifeline=["50-50","Q-replace","Ask the expert","Double tip"]
money=0
p=0
p1=0
p2=0
t=[]
rp1=0
rp2=0
print("You have 4 lifline in this game")
print("You have to use all lifeline till level 13 and there will be no lifeline at level 14")
for j in range(0,4):
    print(f"{j+1}.{lifeline[j]}")
for i in range(0,len(question)):
    if(i==12):
        print("CONGRATULATION YOU HAVE UNLOCKED THE JACKPOT LEVEL!!!")
    print(f"\nLEVEL {i+1}:")
    print(f"\nYour question for {ammount[i]} is:")
    c1=0
    c2=0
    c3=0
    c4=0
    reply=0
    reply1=0
    rp1=0
    rp2=0
    chk=0
    print(question[i])
    ans1=answers[i]
    ans2=answers1[i]
    print("  ",end="")
    print(f"{ans1[0]}   {ans1[1]}")
    print(f"  {ans1[2]}   {ans1[3]}")
    if(i<12):
        l=int(input("Which lifeline you want to use between(1-4) or 0 to no use:"))
        match l:
            case 0:
                ll(l)
            case _ if((f"{lifeline[0]}"=="-----||------") and (f"{lifeline[1]}"=="-----||------") and (f"{lifeline[2]}"=="-----||------") and (f"{lifeline[3]}"=="-----||------")):
                print("Sorry you don't have any lifeline!!")
                chk=2
            case _ if((f"{lifeline[l-1]}"=="-----||------")):
                print("Sorry you can not use one lifeline more than once!!!!")
                chk=2
            case _ if(l==1):
                c1=c1+1
                ans=answers[i]
                p=crtanswers[i]
                if(p==1):
                    p1=2
                    p2=3
                elif(p==2):
                    t=ans[1]
                    ans[1]=ans[0]
                    ans[0]=t
                    p1=2
                    p2=3
                elif(p==3):
                    t=ans[2]
                    ans[2]=ans[0]
                    ans[0]=t
                    p1=2
                    p2=3
                elif(p==4):
                    t=ans[3]
                    ans[3]=ans[0]
                    ans[0]=t
                    p1=2
                    p2=3
                ll(l,c1,c2,c3,c4)
            case _ if(l==2):
                chk=0
                c2=c2+1
                ll(l,c1,c2,c3,c4)
            case _ if(l==3):
                c3=c3+1
                ll(l,c1,c2,c3,c4)
            case _ if(l==4):
                c4=c4+1
                ll(l,c1,c2,c3,c4)
                rp1=int(input("Option 1:"))
                rp2=int(input("Option 2:"))
    if(l==2 and chk==0):
        reply1=int(input("Enter your option between((1-4) repectively as (A-D)) or 0 to quit:"))
    elif(l!=4):
        reply=int(input("Enter your option between((1-4) repectively as (A-D)) or 0 to quit:"))
    elif(rp1==0 and rp2==0):
        reply=int(input("Enter your option between((1-4) repectively as (A-D)) or 0 to quit:"))
    if(reply==0 and rp1==0 and rp2==0 and reply1==0):
        money=ammount[i-1]
        print(f"Your take home money is {money}")
        break
    elif(reply==crtanswers[i] or reply1==crtanswers1[i] or rp1==crtanswers[i] or rp2==crtanswers[i]):
        if(reply1==crtanswers1[i] and chk==0):
            print(f"Correct ans!!!, You won {ammount[i]}")
            if(i==4):
                money="80,000Rs"
            elif(i<4):
                money="0Rs"
            elif(i==9):
                money="25,00,000Rs"
            elif(i==12):
                money="3,00,00,000Rs"
                print("Now you don't have any lifeline for level 14!!")
            if(c1>=1 or c2>=1 or c3>=1 or c4>=1):
                if(l==1 or l==2 or l==3 or l==4):
                    lifeline[l-1]="-----||------"
                    if(i<=12):
                        print("The revised lifelines are:")
                        for j in range(0,4):
                            print(f"{j+1}.{lifeline[j]}")
        elif(reply==crtanswers[i]):
            print(f"Correct ans!!!, You won {ammount[i]}")
            if(i==4):
                money="80,000Rs"
            elif(i<4):
                money="0Rs"
            elif(i==9):
                money="25,00,000Rs"
            elif(i==12):
                money="3,00,00,000Rs"
                print("Now you don't have any lifeline for level 14!!")
            if(c1>=1 or c2>=1 or c3>=1 or c4>=1):
                if(l==1 or l==2 or l==3 or l==4):
                    lifeline[l-1]="-----||------"
                    if(i<=12):
                        print("The revised lifelines are:")
                        for j in range(0,4):
                            print(f"{j+1}.{lifeline[j]}")
        elif(rp1==crtanswers[i] or rp2==crtanswers[i]):
            print(f"Correct ans!!!, You won {ammount[i]}")
            print(f"One of your correct option was option {crtanswers[i]}")
            if(i==4):
                money="80,000Rs"
            elif(i<4):
                money="0Rs"
            elif(i==9):
                money="25,00,000Rs"
            elif(i==12):
                money="3,00,00,000Rs"
                print("Now you don't have any lifeline for level 14!!")
            if(c1>=1 or c2>=1 or c3>=1 or c4>=1):
                if(l==1 or l==2 or l==3 or l==4):
                    lifeline[l-1]="-----||------"
                    if(i<=12):
                        print("The revised lifelines are:")
                        for j in range(0,4):
                            print(f"{j+1}.{lifeline[j]}")
    else:
        print("Sorry wrong ans!!")
        if(l==2 and chk==0):
            print(f"The correct ans was option {crtanswers1[i]}")
        elif(l>=0 and l<=4 or chk==2):
            print(f"The correct ans was option {crtanswers[i]}")
        print(f"The money that you have earned is:{money}")
        break