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
        return f"What is the capital of {self.country}?\nIs it {self.a}: {self.incorrect_1}, {self.b}: {self.incorrect_2} or {self.c}: {self.capital}"

question_1 = Countries("United States", "New York", "Los Angeles", "Washington DC", "A", "B", "C")
print()
print(question_1.question())
question_2 = Countries("China", "Beijing", "Hong Kong", "Shanghai", "A", "B", "C")
print()
print(question_2.question())
question_3 = Countries("Germany", "Berlin", "Hamburg", "Munich", "A", "B", "C")
print()
print(question_3.question())
print()