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
    
    def question_if_a_is_the_correct_answer(self):
        """the question when option A is the correct answer"""
        return f"What is the capital of {self.country}?\nIs it; {self.a}: {self.capital}, {self.b}: {self.incorrect_1} or {self.c}: {self.incorrect_2}"
    
    def question_if_b_is_the_correct_answer(self):
        """the question when option B is the correct answer"""
        return f"What is the capital of {self.country}?\nIs it; {self.a}: {self.incorrect_1}, {self.b}: {self.capital} or {self.c}: {self.incorrect_2}"
    
    def question_if_c_is_the_correct_answer(self):
        """the question when option C is the correct answer"""
        return f"What is the capital of {self.country}?\nIs it; {self.a}: {self.incorrect_1}, {self.b}: {self.incorrect_2} or {self.c}: {self.capital}"

question_1 = Countries("the United States", "Washington DC", "Los Angeles", "New York", "A", "B", "C")
question_2 = Countries("China", "Beijing", "Hong Kong", "Shanghai", "A", "B", "C")
question_3 = Countries("Germany", "Berlin", "Hamburg", "Munich", "A", "B", "C")
question_4 = Countries("Japan", "Hiroshima", "Osaka", "Toyko", "A", "B", "C")
question_5 = Countries("India", "Chennai", "Mumbai", "New Deheli", "A", "B", "C")
question_6 = Countries("the United Kingdom", "Birmingham", "London", "Manchester", "A", "B", "C")
question_7 = Countries("France", "Lyon", "Nice", "Paris", "A", "B", "C")
question_8 = Countries("Italy", "Milan", "Naples", "Rome", "A", "B", "C")
question_9 = Countries("Canada", "Montreal", "Ottawa", "Toronto", "A", "B", "C")
question_10 = Countries("Brazil", "Brasilia", "Rio de Janerio", "Sao Paulo", "A", "B", "C")

print()
print(question_1.question_if_c_is_the_correct_answer())
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
determine_if_c_is_the_corrrect_answer()


print(question_2.question_if_a_is_the_correct_answer())
print()
def determine_if_a_is_the_corrrect_answer():
    """
    determines the output once the user has input A/a, B/b, C/c or something else
    """
    answer = input("Please select an option of A, B or C: ")
    print()
    print(f"You selected {answer}")
    print()

    if answer.upper() == "A":
        print(f"Well done, {answer} is the correct answer")
        print()
    elif answer.upper() == "B":
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
determine_if_c_is_the_corrrect_answer()

print(question_3.question_if_c_is_the_correct_answer())
print()


def determine_if_b_is_the_corrrect_answer():
    """
    determines the output once the user has input A/a, B/b, C/c or something else
    """
    answer = input("Please select an option of A, B or C: ")
    print()
    print(f"You selected {answer}")
    print()

    if answer.upper() == "A":
        print(f"Well done, {answer} is the correct answer")
        print()
    elif answer.upper() == "B":
        print(f"{answer} is not the correct answer")
        print()
    elif answer.upper() == "C":
        print(f"{answer} is not the correct answer")    
        print()
    else:
        print(f"{answer} is not an option, please try again and choose an option of A, B or C")
        print()
determine_if_b_is_the_corrrect_answer()

print()
print