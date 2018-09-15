class Datreader:

    def __init__(self, file_path):
        self.file_path = file_path
              
    def get_the_data_dictionary(self):   
        data_dictionary = {}
        with open(self.file_path, 'r') as f:
            lines = f.readlines()
            iterlines = iter(lines)
            next(iterlines)
            for line in iterlines:
                fields = line.split()
                data_dictionary[fields[0]] = fields[1:]
        return data_dictionary
       
class Report:

    def __init__(self, file_path, column1, column2):
        self.file_path = file_path
        self.column1 = column1
        self.column2 = column2

    def get_the_answer(self):

        file_reader = Datreader(self.file_path)
        data_list = file_reader.get_the_data_dictionary()

        minimum = 999
        key_with_minimum_spread = int()
        for ids in data_list:
            difference = abs(float(data_list[ids][self.column1]) - float(data_list[ids][self.column2]))
            if difference < minimum:
                minimum = difference
                key_with_minimum_spread= ids
        if(self.column1 == 0):      
            return(key_with_minimum_spread)
        else:
            return (data_list[key_with_minimum_spread][0])