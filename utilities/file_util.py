from utilities.errors import WrongInputFormat

class FileUtil:
    """ Utility class which has member functions that will be used for parsing inputPS4.txt, outputting to outputPS4.txt and has some exception handling. """
    def __init__(self):
        super().__init__()
    
    def _is_integer(self, number):
        """ Private utility method to check whether a string is an integer or not """
        try: 
            int(number)
            return True
        except ValueError:
            return False

    def _parse(self, line):
        """ Private utiltiy method to parse through a line from the input file and return an array of integers 
            Throws error for the following reasons:-
              1.) Wrong input format
              2.) Type casting errors
        """
        data = line.split(' ')
        data = list(filter(lambda x: x != ' ', data))
        for i in range(len(data)):
            data[i] = data[i].rstrip("\n")
            if(self._is_integer(data[i])):
                data[i] = int(data[i]) # Assuming the input is only integer and not float
            else:
                raise WrongInputFormat(f"Wrong input format as it is not an integer for {data[i]} in the input list: {data}")
        return data

    def readAndParseInput(self, file_name):
        """ Method that reads the input file and parses the input and if all ok it returns an array of each input case """
        final_list = []
        try:
            file = open(file_name, "r")
            lines = file.readlines()
            for line in lines:
                if line.strip() == '':
                    continue
                val = self._parse(line)
                final_list.append(val)
        except WrongInputFormat as e:
            print(f"ERROR: {e.args[0]} at file:- {file_name}")
            final_list = None
        except IOError:
            print(f"Error while reading/opening into the file :- {file_name}")
            final_list = None
        except ValueError:
            print(f"ERROR: Could not parse the file {file_name} because of type casting")
            final_list = None
        finally:
            file.close()
            return final_list
    
    def writeOutput(self, file_name, out_list):
        """ Utility method to write the string into the output file """
        try:
            file = open(file_name, "w")
            out_string = ""
            for data in out_list:
                out_string += f"{data[0]} {data[1]}\n"
            file.write(out_string)
        except IOError:
            print("ERROR: Outputting into the file failed")
        finally:
            file.close()
