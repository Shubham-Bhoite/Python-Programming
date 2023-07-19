questions = [
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Ricky Ponting is also known as what?", "The Rickster", "Ponts", "Ponter",
    "Punter", "None", 4
  ],
  [
    "'.MOV' extension refers usually to what kind of file?", "Image file", "Animation/movie file", "Audio file",
    "MS Office", "None", 2
  ],
  [
    "Fastest shorthand writer was?", "Dr. G. D. Bist", "J.R.D. Tata", "J.M. Tagore",
    "Khudada Khan", "None", 1
  ],
  [
    "Entomology is the science that studies?", "Behavior of human beings", "Insects", "The formation of rocks",
    "The origin and history of technical term", "None", 2
  ],
  [
    "The present Lok Sabha is the?", "14th Lok Sabha", "15th Lok Sabha", "16th Lok Sabha",
    "17th Lok Sabha", "None", 4
  ],
  [
    "When is Independence Day in Australia?", "03 March", "03 Feb", "03 April",
    "03 May", "None", 1
  ],
  [
    "The members of the Rajya Sabha are elected by?", "the people", "Lok Sabha", "elected members of the legislative assembly",
    "elected members of the legislative council", "None", 3
  ]
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0
for i in range(0, len(questions)):
  
  question = questions[i]
  print(f"\n\nQuestion for Rs. {levels[i]}")
  print(f"a. {question[1]}          b. {question[2]} ")
  print(f"c. {question[3]}          d. {question[4]} ")
  reply = int(input("Enter your answer (1-4) or  0 to quit:\n" ))
  if (reply == 0):
    money = levels[i-1]
    break
  if(reply == question[-1]):
    print(f"Correct answer, you have won Rs. {levels[i]}")
    if(i == 4):
      money = 10000
    elif(i == 9):
      money = 320000
    elif(i == 14):
      money = 10000000
  else:
    print("Wrong answer!")
    break 

print(f"Your take home money is {money}")
