from utilities.file_util import FileUtil

#          0                 1         2         3    
enum = ["increasing", "decreasing", "minima", "maxima"]
INPUT_FILE_PATH = './inputPS4.txt'
OUTPUT_FILE_PATH = './outputPS4.txt'

def Merge(arr, l, m, r, final_state):
    """ Conquer method that just compares the middle and next to middle element
        and decides the state based on the previous persisted state.
        Cases:-
        1.) For increasing & decreasing case it picks up the least value.
        2.) For Maxima & Minima case it picks up the corresponding maxima and minima.
    """
    temp_state = final_state
    [ en, val ] = final_state
    if(arr[m] > arr[m+1]):
        if(en == enum[0]):
            temp_state = [enum[3], arr[m]] # Maxima
        elif(en == enum[1] or en == None):
            temp_state = [enum[1], arr[r]] # Decreasing
        elif(en == enum[2]): # Specific Minima
            temp_state = [en, arr[m + 1]]
        else: # Add elif for maxima and minima case
            temp_state = [en, arr[m]]
    elif (arr[m] < arr[m+1]):
        if(en == enum[1]):
            temp_state = [enum[2], arr[m]] # Minima
        elif(en == enum[0] or en == None):
            temp_state = [enum[0], arr[l]] # Increasing
        elif(en == enum[3]): # Specific Maxima case
            temp_state = [en, arr[m + 1]]
        else:
            temp_state = [en, arr[m]]
    return temp_state

def final(arr):
    final_state = [ None, None ]
    # Here MaxMin function is a closure which maintains a state variable for recursive calls
    def MaxMin(arr, l, r):
        """ MaxMin is a divide and conquer based alogrithm. 
            It uses a state variable for each of the recursive call.
            During the conquering step it compares the previous state and
            the current state and decides on every merge.
        """
        if(l < r):
            nonlocal final_state # Emulating something like javascript's closure to access / reference outer function's variable
            m = (l + (r-1)) // 2 # Floor division
            MaxMin(arr, l, m)
            MaxMin(arr, m + 1, r)
            final_state = Merge(arr, l, m, r, final_state)
    MaxMin(arr, 0, len(arr) - 1)
    return final_state

if __name__ == '__main__':

    fileutil = FileUtil()
    input_lines = fileutil.readAndParseInput(   )

    if(input_lines == None):
        print("Some error occured while parsing the files or there might be type error in the files")
        print("So, exiting ...")
        exit()
    
    out_list = []
    for test_case in input_lines:
        output_to_be_written = final(test_case)
        out_list.append(output_to_be_written)

    fileutil.writeOutput(OUTPUT_FILE_PATH, out_list)