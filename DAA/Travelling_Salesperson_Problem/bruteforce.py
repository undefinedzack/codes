class bruteforcez:

    def calculate(self, matrix : list, starting_vertex : int):
        paths = []

        temp_path = [0] * ( len(matrix)+1 )
        
