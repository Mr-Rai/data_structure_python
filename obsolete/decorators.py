def lower_case_str(func):
    def wrapper(word1, word2):
        word1 = word1.lower()
        word2 = word2.lower()
        return func(word1, word2)

    return wrapper


# def split_string(func):
#     def wrapper():
#         return func().split()

#     return wrapper


# @split_string
@lower_case_str
def something(word1: str, word2: str):
    return f"Word1: {word1}\nWord2: {word2}"


# print(something(word1="Hi", word2="Shubham"))


##-----------------------------------
class GrandFather:
    def __init__(self, grandfather) -> None:
        self.born_in = 1942
        self.grandfather = grandfather


class Son(GrandFather):
    def __init__(self, son, grandfather) -> None:
        self.son = son
        GrandFather.__init__(self, grandfather)


class GrandSon(Son):
    def __init__(self, grandfather, son, grandson) -> None:
        self.grandson = grandson
        Son.__init__(self, son, grandfather)

    def print_family_heirirchy(self):
        return f"{self.grandfather} --> {self.son} --> {self.grandson}"


print(GrandSon("Jagdish", "Shekhar", "Shubham").print_family_heirirchy())
