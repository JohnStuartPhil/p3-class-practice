# print()
# print("Welcome to the Capital cities Quiz, press Enter to continue")
# input()
# print()
# print("You shall be asked for the capital of 10 countries")
# print("You shall be given a choice of 3 cities in that country, listed as A, B and C")
# print("Please select either A, B or C")
# print("You shall be advised if that is the correct answer or not")
# print("If you select anything other than A, B or C, you shall be asked to make a choice again until you select A, B or C")
# print("Press Enter to continue")
# input()

class Countries:
    """Defines the options"""
    def __init__(self, number, country, capital, incorrect_1, incorrect_2, a, b, c):
        self.number = number
        self.country = country
        self.capital = capital
        self.incorrect_1 = incorrect_1
        self.incorrect_2 = incorrect_2 
        self.a = a
        self.b = b
        self.c = c
    
    def question_if_a_is_the_correct_answer(self):
        """the question when option A is the correct answer"""
        return f"Question {self.number}: What is the capital of {self.country}?\n\nIs it; {self.a}: {self.capital}, {self.b}: {self.incorrect_1} or {self.c}: {self.incorrect_2}"
    
    def question_if_b_is_the_correct_answer(self):
        """the question when option B is the correct answer"""
        return f"Question {self.number}: What is the capital of {self.country}?\n\nIs it; {self.a}: {self.incorrect_1}, {self.b}: {self.capital} or {self.c}: {self.incorrect_2}"
    
    def question_if_c_is_the_correct_answer(self):
        """the question when option C is the correct answer"""
        return f"Question {self.number}: What is the capital of {self.country}?\n\nIs it; {self.a}: {self.incorrect_1}, {self.b}: {self.incorrect_2} or {self.c}: {self.capital}"

question_1 = Countries(1, "the United States", "Washington DC", "Los Angeles", "New York", "A", "B", "C")
question_2 = Countries(2, "China", "Beijing", "Hong Kong", "Shanghai", "A", "B", "C")
question_3 = Countries(3, "Germany", "Berlin", "Hamburg", "Munich", "A", "B", "C")
question_4 = Countries(4, "Japan", "Toyko", "Hiroshima", "Osaka", "A", "B", "C")
question_5 = Countries(5, "India", "New Dheli", "Chennai", "Mumbai", "A", "B", "C")
question_6 = Countries(6, "the United Kingdom", "London", "Birmingham", "Manchester", "A", "B", "C")
question_7 = Countries(7, "France", "Paris", "Lyon", "Nice", "A", "B", "C")
question_8 = Countries(8, "Italy", "Rome", "Milan", "Naples", "A", "B", "C")
question_9 = Countries(9, "Canada", "Ottawa", "Montreal", "Toronto", "A", "B", "C")
question_10 = Countries(10, "Brazil", "Brasilia", "Rio de Janerio", "Sao Paulo", "A", "B", "C")

score = 0

def determine_if_a_is_the_corrrect_answer():
    """
    determines the output once the user has input A/a, B/b, C/c or something else
    """
   
    while True:
        answer = input("Please select an option of A, B or C, then press Enter:\n")
        print()
        if answer.upper() == "A" or answer.upper() == "B" or answer.upper() == "C":
            print()
            print(f"You selected {answer.capitalize()}")
            print()
            break
        else:
            print()
            print(f"You selected {answer}")
            print()
            print(f"{answer} is not an option, please try again and choose an option of A, B or C")
            print()

    
    if answer.upper() == "A":
        print()
        print(f"Well done, {answer.capitalize()} is the correct answer")
        print()
        global score
        score += 1
        print("score:", score)
    elif answer.upper() == "B" or answer.upper() == "C":
        print()
        print(f"{answer.capitalize()} is not the correct answer")
        print()

def determine_if_b_is_the_corrrect_answer():
    """
    determines the output once the user has input A/a, B/b, C/c or something else
    """
    
    while True:
        answer = input("Please select an option of A, B or C, then press Enter:\n")
        print()
        if answer.upper() == "A" or answer.upper() == "B" or answer.upper() == "C":
            print()
            print(f"You selected {answer.capitalize()}")
            print()
            break
        else:
            print()
            print(f"You selected {answer}")
            print()
            print(f"{answer} is not an option, please try again and choose an option of A, B or C")
            print()
    
    if answer.upper() == "B":
        print()
        print(f"Well done, {answer.capitalize()} is the correct answer")
        print()
        global score
        score += 1
        print("score:", score)
    elif answer.upper() == "A" or answer.upper() == "C":
        print()
        print(f"{answer.capitalize()} is not the correct answer")
        print()

def determine_if_c_is_the_corrrect_answer():
    """
    determines the output once the user has input A/a, B/b, C/c or something else
    """
    
    while True:
        answer = input("Please select an option of A, B or C, then press Enter:\n")
        print()
        if answer.upper() == "A" or answer.upper() == "B" or answer.upper() == "C":
            print()
            print(f"You selected {answer.capitalize()}")
            print()
            break
        else:
            print()
            print(f"You selected {answer}")
            print()
            print(f"{answer} is not an option, please try again and choose an option of A, B or C")
            print()

    
    if answer.upper() == "C":
        print()
        print(f"Well done, {answer.capitalize()} is the correct answer")
        print()
        global score
        score += 1
        print("score:", score)
    elif answer.upper() == "A" or answer.upper() == "B":
        print()
        print(f"{answer.capitalize()} is not the correct answer")
        print()

print()
print(question_1.question_if_c_is_the_correct_answer())
print()
determine_if_c_is_the_corrrect_answer()

print()
print(question_2.question_if_a_is_the_correct_answer())
print()
determine_if_a_is_the_corrrect_answer()

print()
print(question_3.question_if_a_is_the_correct_answer())
print()
determine_if_a_is_the_corrrect_answer()

print()
print(question_4.question_if_c_is_the_correct_answer())
print()
determine_if_c_is_the_corrrect_answer()

print()
print(question_5.question_if_c_is_the_correct_answer())
print()
determine_if_c_is_the_corrrect_answer()

print()
print(question_6.question_if_b_is_the_correct_answer())
print()
determine_if_b_is_the_corrrect_answer()

print()
print(question_7.question_if_c_is_the_correct_answer())
print()
determine_if_c_is_the_corrrect_answer()

print()
print(question_8.question_if_c_is_the_correct_answer())
print()
determine_if_c_is_the_corrrect_answer()

print()
print(question_9.question_if_b_is_the_correct_answer())
print()
determine_if_b_is_the_corrrect_answer()

print()
print(question_10.question_if_a_is_the_correct_answer())
print()
determine_if_a_is_the_corrrect_answer()

print("That is the end of the quiz")