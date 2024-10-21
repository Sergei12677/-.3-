calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    return (len(string), string.upeer(), string.lower())
def is_contans(string,search_list):
    count_calls()
    string = string.lower()
    for elem in search_list:
        if elem.lower() == string:
            return True
        return False











