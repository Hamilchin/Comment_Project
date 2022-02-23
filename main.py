import csv

description_dict = {"English 9":"The 9th grade class initiates students into the world of literature and writing at the high school level, building skills and understandings that will serve them in their English classes and beyond. At its core, the class is about stories and the communities for whom they have meaning; students learn to read closely, taking their own observations and inferences as starting points for interpretation."}

def get_data(student_name):
  '''
  Returns:
  Dictionary containing data for student, with headers as keys. 
  '''
  with open("teacher.csv") as data:
      student_data = csv.reader(data)
      headers = next(student_data)
      for line in student_data:
        # Line 0 is the students name in the file
        if line[0] == student_name:
          comment_data_list = line
      # Strips the headers and the information
      comment_data_list = [data.strip() for data in comment_data_list]
      headers = [header.strip() for header in headers]
      # Dictionary with headers as keys and information as values
      comment_data = {}
      for index, val in enumerate(comment_data_list):
        comment_data[headers[index]] = val
      return(comment_data)

def course_description(comment_data):
  '''
  Returns:
  String with course description
  '''
  return description_dict[comment_data["Class Name"]]

def final_grade(comment_data):
  '''
  Returns:
  String, e.g. B+, F, that quantifies all of the data for the student
  '''
  #Averages all of the learning outcomes (LOS)
  LOS = (int(comment_data['Writing']) + int(comment_data['Reading']) + int(comment_data['Communication']) + int(comment_data['Thinking']))/4
  #Averages homework, test, and LOS to get final score (1/3 weighted each)
  final_score = (LOS*10 + 60 + int(comment_data["Homework Score"]) + int(comment_data["Test Score"]))/3
  if final_score <= 64:
    return "F"
  grades = ["A+","A", "A-", "B+", "B", "B-","C+","C", "C-","D+","D", "D-"]
  #Uses some clever indexing with a difference variable to find the final grade. 
  diff = 100 - final_score
  return grades[round(diff/3)]
  return(final_grade)


def change_scores(comment_data):
  '''
  Returns:
  Dictionary of skills with there scores in a form of 0-4
  '''
  file_scores = {}
  updated_file_scores = {}
  # Gets all the indexes of the items that should be numbers within the file
  for index, key in enumerate(comment_data.keys()):
    if index >= 5:
      file_scores[key] = comment_data.get(key)
  # Changes the numbers in the file_scores dictionary to 0-4 like the OES number system
  for key, value in file_scores.items():
    if int(value) >= 90:
      number = 4
    elif int(value) >= 80:
      number = 3
    elif int(value) >= 70:
      number = 2
    elif int(value) >= 50:
      number = 1
    elif int(value) < 50:
      number = 0
    updated_file_scores[key] = number
  return updated_file_scores


def p1(comment_data):
  '''
  Returns:
  String with paragraph about work ethic, homework completion, class discussion, and some learning objectives that they have or haven't met
  '''

  # Changes first part of sentence 1 depending on their work ethic
  # Includes transition words to transition to second part of sentence 1
  if int(comment_data['Work Ethic']) >= 90:
    first_part_sentence1 = f"First of all, you have a stellar work ethic"
    # If the second part of the sentence is positive then it will use the positive_transition_word which is 'and' in this case since this first part is also positive
    positive_transition_word = 'and'
    # If the second part of the sentence is constructive then it will use the constructive_transition_word which is 'but' in this case since this first part is positive but the second part is not
    constructive_transition_word = 'but'
  elif int(comment_data['Work Ethic']) >= 80:
    first_part_sentence1 = f"First of all, you have a great work ethic"
    positive_transition_word = 'and'
    constructive_transition_word = 'but'
  elif int(comment_data['Work Ethic']) >= 70:
    first_part_sentence1 = f"First of all, you can show your great work ethic at times"
    positive_transition_word = 'and'
    constructive_transition_word = 'but'
  elif int(comment_data['Work Ethic']) >= 50:
    positive_transition_word = 'but'
    constructive_transition_word = 'and'
    first_part_sentence1 = f"First of all, your need to improve on your work ethic"
  else:
    first_part_sentence1 = f"First of all, you have rarely shown your work ethic and I would love to meet to talk about it"
    positive_transition_word = 'but'
    constructive_transition_word = 'and'

  # Changes second part of the first sentence depending on the homework assignments they have turned in out of the total homework assignments.
  if int(comment_data.get('Total Homework Assignments')) - int(comment_data.get('Completed Homework Assignments')) < 3:
    second_part_sentence1 = f"{positive_transition_word} you have done an astounding job with {comment_data.get('Completed Homework Assignments')}/{comment_data.get('Total Homework Assignments')} homework assignments completed!"
  elif int(comment_data.get('Total Homework Assignments')) - int(comment_data.get('Completed Homework Assignments')) < 8:
    second_part_sentence1 = f"{positive_transition_word} you have done a good job with {comment_data.get('Completed Homework Assignments')}/{comment_data.get('Total Homework Assignments')} homework assignments turned in."
  elif int(comment_data.get('Total Homework Assignments')) - int(comment_data.get('Completed Homework Assignments')) < 15:
    second_part_sentence1 = f"{constructive_transition_word} you have done an alright job with doing your homework but I think you have a lot of room to improve."
  else:
    second_part_sentence1 = f"{constructive_transition_word} you need to work on completing your homework assignments and only have {comment_data.get('Completed Homework Assignments')}/{comment_data.get('Total Homework Assignments')} homework assignments turned in."

  # Combines the first and second part of the sentence together
  sentence1 = first_part_sentence1 + ' ' + second_part_sentence1

  # Changes first part of second sentence depending on their class discussion contribution
  if comment_data.get('Discussion Contribution Amount') == 'High':
    first_part_sentence2 = f"You have done an astounding job at contributing in class conversations by being one of the main contributers"
    positive_transition_word = 'and'
    constructive_transition_word = 'but'
  elif comment_data.get('Discussion Contribution Amount') == 'Medium':
    first_part_sentence2 = f"You sometimes contribute in class discussions"
    positive_transition_word = 'and'
    constructive_transition_word = 'but'
  else:
    first_part_sentence2 = f"You rarely contribute in class discussions"
    positive_transition_word = 'but'
    constructive_transition_word = 'and'

  # Changes second part of first sentence depending on the value of the comments they make
  if comment_data.get('Discussion Contribution Value') == 'High':
    second_part_sentence2 = f"{positive_transition_word} you share meaningful ideas, questions, and thoughts!"
  elif comment_data.get('Discussion Contribution Value') == 'Medium':
    second_part_sentence2 = f"{positive_transition_word} most of the time you share meaningful ideas, questions, and thoughts."
  else:
    second_part_sentence2 = f"{constructive_transition_word} you need to work on making your ideas, questions, and thoughts more meaningful."
  
  # Adds the parts together to make a whole sentence
  sentence2 = first_part_sentence2 + ' ' + second_part_sentence2

  # Changes first part of third sentence depending on their writing skills
  if comment_data.get('Writing') == '4':
    first_part_sentence3 = f"In addition, you are an amazing writer"
    positive = True
  if comment_data.get('Writing') == '3':
    first_part_sentence3 = f"In addition, you are a great writer"
    positive = True
  if comment_data.get('Writing') == '2':
    first_part_sentence3 = f"In addition, you can show me your writing skills at times"
    positive = False
  if comment_data.get('Writing') == '1':
    first_part_sentence3 = f"In addition, you need to work on your writing skills"
    positive = False

  # Changes second part of third sentence depending on their reading skills
  if comment_data.get('Reading') == '4' or comment_data.get('Reading') == '3' and positive:
    second_part_sentence3 = "and reader."
  elif comment_data.get('Reading') == '4' and not positive:
    second_part_sentence3 = "but you are an amazing reader."
  elif comment_data.get('Reading') == '3' and not positive:
    second_part_sentence3 = "but you are a good reader."
  elif comment_data.get('Reading') == '2' or comment_data.get('Reading') == '1' and not positive:
    second_part_sentence3 = "and reader"
  elif comment_data.get('Reading') == '2' and positive:
    second_part_sentence3 = "but you need to work on your reading"
  elif comment_data.get('Reading') == '1' and positive:
    second_part_sentence3 = "but you really need to work on your reading"
  
  # Adds the parts of the third sentence together
  sentence3 = first_part_sentence3 + ' ' + second_part_sentence3

  # Returns the sentences in a paragraph form
  return sentence1 + ' ' + sentence2 + ' ' + sentence3


def p2(comment_data, student_name):
  '''
  Returns:
  String with paragraph about test scores, deep thinking, and a mention of proactivity (and where to improve). 
  '''
  comment_data = change_scores(comment_data)
  #Provides a series of options for each sentence in the form of a dictionary
  first_sentence_opts = {0: "We really need to talk about your tests. You have been performing incredibly minimally in terms of test scores, and even with my help, you have been getting below 50% on the cumulative test score. ", 1: "We need to talk about your tests. You have been performing pretty badly, and I'm concerned that you don't really know your material (getting below 70% on your cumulative test score). ", 2: "Tests have been more of a difficulty for you. You have been getting consistently below 80% on your cumulative test scores, so I suggest you practice a bit more to solidify the concepts. ", 3: "You have been doing pretty well in terms of tests - just a little more practice, and you will get there. You got above 80% on your cumulative test scores, so nice job! ", 4:"You have been really well on your tests, showing how well you know your stuff. Over 90% consistently on your cumulative test scores, so nice job! "}
  first_sentence = first_sentence_opts[int(comment_data["Test Score"])]

  #Creates a contrast word that determines if the previous sentence contrasts with the next one. 
  if abs(int(comment_data["Test Score"]) - int(comment_data["Improvement"])) >= 2:
    contrast_word = "However, "
  else:
    contrast_word = "Indeed, "
  
  second_sentence_opts = {0:"I have seen little to no improvement for you this year, showing that you don't put enough effort into this class. ", 1:"I have seen little improvement for you this year, showing that you don't put quite enough effort into this class. ", 2:"I can see the effort you put into this class, but I think you still have a lot of room to improve. ", 3:"I can see the effort you put into this class, and I can really see the improvement from the first semester. ", 4:"I can see the effort you put into this class, and you really improved a huge amount from the first semester! "}
  second_sentence = second_sentence_opts[int(comment_data["Improvement"])]

  #Proactivity, then Improvement
  #Creates a different dictionary - one that takes in two binary values, proactivity and improvement, and has 4 possible options. 
  third_sentence_opts = {11:"Truly, I know you are reluctant to do so, but I really think you should be more proactive in seeking help. I would encourage you to seek more help during office hours, where we can do some practice problems to help boost your understanding and improvement. ", 14:"Even though you have been improving, I think you still have room to grow. Being more proactive by emailing questions or meeting during office hours could bolster your understanding of the material. ", 41:"Even though you still have a lot of room to improve, I'm glad you are being so proactive in seeking out help. It shows. ", 44:" Truly, thanks for being so proactive when it comes to asking for help. Your improvement really shows. "}
  
  pro = "4"
  imp = "4"
  if comment_data["Proactivity"] < 3:
    pro = "1"
  if comment_data["Improvement"] < 3:
    imp = "4"
  
  third_sentence = third_sentence_opts[int(pro + imp)]

  fourth_sentence_opts = {0:"Overall, you really need to work on your skills in English 9. Let's have a talk on how best to make that happen.", 1:"Overall, you really need to work on your skills in English 9. Let's have a talk on how best to make that happen.", 2:"Overall, I think you still have a lot of room to improve. Try spend more time reading and writing so you can perform well in the second semester finals. ", 3:"Overall, you have been doing pretty solidly this semester. Keep it up! ", 4:"Overall, you have been performing really well this semester. Keep it up!"}
  fourth_sentence = fourth_sentence_opts[int(comment_data["Test Score"])]

  #Concatenates all the sentences. 
  return(first_sentence + contrast_word + second_sentence + third_sentence + fourth_sentence)

def ending(comment_data):
  '''
  Returns:
  String with concluding sentences (grades and final evaluation, looking forward to...)
  '''
  grades = ["A+","A", "A-", "B+", "B", "B-","C+","C", "C-","D+","D", "D-"]
  grade = final_grade(comment_data)
  try:
    gindex = round((grades.index(grade)+1)/3 + -0.2)
  except:
    gindex = 4
  #Evaluates the grade out of four using the 'gindex' variable. 4 is bad, 0 is good. 
  first_sentence_opts = {4:"English 9 is a hard class, and I think you could have done better in the first semester. ", 3:"English 9 is a difficult class, and I think you could have done better in the first semester. ", 2:"English 9 is a difficult class, and I think you still have some room to improve. ", 1:"English 9 is a difficult class, but I think you handled it well. ", 0:"English 9 is a difficult class, but you really thrived in this class. "}
  first_sentence = first_sentence_opts[gindex]
  second_sentence = "Your final grade for the semester was " + grade + ". I look forward to working with you for the rest of the year."
  return first_sentence + second_sentence


def get_positive_structures(positive_student_attributes):
  positive_sentences = []
  with open('sentencestructure.txt') as file:
    for key, value in positive_student_attributes.items():
      lines = file.readlines()
      for index, line in enumerate(lines):
        if line.startswith('Positive Structures:'):
          positive_line = lines[index + 1].replace('{positive_word_placeholder}', value)
          positive_line = positive_line.replace('{objective_word_placeholder}', key)
          positive_sentences.append(positive_line)
  return positive_sentences

def format_all(intro, p1, p2, end):
  '''
  Returns formatted version of all paragraphs. 
  '''
  return(f"{intro}\n\n{p1}\n\n{p2}\n\n{end}")

def write_to_txt(formatted_text, student_name):
  '''
  Takes in final formatted text and writes to txt. Also prints the formatted text and writes a guide note. 
  '''
  with open(student_name+".txt", "w") as txtfile:
    txtfile.write(formatted_text)
  print(formatted_text + "\n")
  print(f"Your above comment is stored under the file: {student_name}.txt")
  print("\n\n\n")



def write_comment(student_name):
  comment_data = get_data(student_name)
  intro_paragraph = course_description(comment_data)
  first_paragraph = p1(comment_data)
  second_paragraph = p2(comment_data, student_name)
  final_paragraph = ending(comment_data)
  final_comment = format_all(intro_paragraph,first_paragraph,second_paragraph,final_paragraph)
  write_to_txt(final_comment, student_name)

# Writes the comments for the 6 students (puts them into separate files with each students name on them)
write_comment("Al")
write_comment("Bill")
write_comment("Tanner")
write_comment("Tully")
write_comment("Henry")
write_comment('Calvin')
