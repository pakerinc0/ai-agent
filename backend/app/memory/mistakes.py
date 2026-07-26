class MistakeMemory:


    def __init__(self):

        self.errors = []



    def add(self,error,solution):

        self.errors.append({

            "error":error,

            "solution":solution

        })



    def get_all(self):

        return self.errors
