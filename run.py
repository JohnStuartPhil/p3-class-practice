class Countries:
    """Lists the countries"""
    def __init__(self, country, capital, incorrect_1, incorrect_2, a, b, c):
        self.country = country
        self.capital = capital
        self.incorrect_1 = incorrect_1
        self.incorrect_2 = incorrect_2 
        self.a = a
        self.b = b
        self.c = c
    
    def question(self):
        """the question"""
        return f"What is the capital of {self.country}?\nIs it; {self.a}: {self.incorrect_1}, {self.b}: {self.incorrect_2} or {self.c}: {self.capital}"

question_1 = Countries("the United States", "New York", "Los Angeles", "Washington DC", "A", "B", "C")
print()
print(question_1.question())
print()
def determine_if_b_is_the_corrrect_answer():
    """
    determines the output once the user has input A/a, B/b, C/c or something else
    """
    answer = input("Please select an option of A, B or C: ")
    print()
    print(f"You selected {answer}")
    print()

    if answer.upper() == "B":
        print(f"Well done, {answer} is the correct answer")
        print()
    elif answer.upper() == "A":
        print(f"{answer} is not the correct answer")
        print()
    elif answer.upper() == "C":
        print(f"{answer} is not the correct answer")    
        print()
    else:
        print(f"{answer} is not an option, please try again and choose an option of A, B or C")
        print()
        the_question()
        print()
        the_options()
        print()
determine_if_b_is_the_corrrect_answer()

question_2 = Countries("China", "Beijing", "Hong Kong", "Shanghai", "A", "B", "C")
print(question_2.question())
print()
def determine_if_c_is_the_corrrect_answer():
    """
    determines the output once the user has input A/a, B/b, C/c or something else
    """
    answer = input("Please select an option of A, B or C: ")
    print()
    print(f"You selected {answer}")
    print()

    if answer.upper() == "C":
        print(f"Well done, {answer} is the correct answer")
        print()
    elif answer.upper() == "A":
        print(f"{answer} is not the correct answer")
        print()
    elif answer.upper() == "B":
        print(f"{answer} is not the correct answer")    
        print()
    else:
        print(f"{answer} is not an option, please try again and choose an option of A, B or C")
        print()
        the_question()
        print()
        the_options()
        print()
determine_if_c_is_the_corrrect_answer()

question_3 = Countries("the United Kingdom", "Birmingham", "London", "Manchester", "A", "B", "C")
print(question_3.question())
print()
def determine_if_b_is_the_corrrect_answer():
    """
    determines the output once the user has input A/a, B/b, C/c or something else
    """
    answer = input("Please select an option of A, B or C: ")
    print()
    print(f"You selected {answer}")
    print()

    if answer.upper() == "B":
        print(f"Well done, {answer} is the correct answer")
        print()
    elif answer.upper() == "A":
        print(f"{answer} is not the correct answer")
        print()
    elif answer.upper() == "C":
        print(f"{answer} is not the correct answer")    
        print()
    else:
        print(f"{answer} is not an option, please try again and choose an option of A, B or C")
        print()
        the_question()
        print()
        the_options()
        print()
determine_if_b_is_the_corrrect_answer()
