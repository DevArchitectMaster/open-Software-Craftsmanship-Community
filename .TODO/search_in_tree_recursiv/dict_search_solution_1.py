test_dict_ = {
    "a" : "1",
    "b" : {
        "1" : 2,
        "2" : 4711,
        "3" : {
            "b31" : 31
        },
        "4" : 4
    },
    "c" : "3",
    "d" : {
        "1" : 5,
        "2" : 9,
        "3" : {
            "c31" : 55
        }
    }
}

test_dict = {
    1 : {
      "a": "1",
      "b": {
          "1": 2,
          "2": 4711,
          "3": {
              "c31": 31
          },
          "4": 4
      },
      "c": "3",
      "d": {
          "1": 5,
          "2": 9,
          "3": {
              "c31": 55
          }
      },
      "e": {
          "3": {
              "c31": {
                  "55": {
                      "3": {
                          "c31": 31
                      },
                      "7": 5
                  },
                  9: 123
              }
          },
          5: 7
      }
    }
}

####################################################################################

def convert_dictkeys_to_list(dict_keys: str):
    key_list = dict_keys.strip("[]").split("][")
    key_list = [int(item) if item.isdecimal() else float(item) if item.replace('.', '', 1).isdecimal() else item.replace('"', '').replace("'", "") for item in key_list]
    return key_list

####################################################################################

def find_path_of_occurrence(nested_dict: dict, search_path: str):
    search_path_list = convert_dictkeys_to_list(search_path)
    return recursive_tree_search(nested_dict, search_path_list)


def recursive_tree_search(nested_dict: dict, pattern: list, result_list=[], current_path=[]):
    for [key, value] in nested_dict.items(): 
        if key == pattern[0]:
            current_result = check_occurrence(nested_dict=value, pattern=pattern, index=1, result_path=current_path + [key])
            if current_result != None:
                result_list.append(current_result)
        
        if isinstance(value, dict):
            recursive_tree_search(nested_dict=value, pattern=pattern, result_list=result_list, current_path=current_path + [key])
    return result_list


def check_occurrence(nested_dict: dict, pattern: list, index=0, result_path=[]):
    if index > len(pattern) - 1:
        return result_path

    if isinstance(nested_dict, dict) and pattern[index] in nested_dict:
        result_path.append(list(nested_dict.keys())[0])
        return check_occurrence(nested_dict=nested_dict[pattern[index]], pattern=pattern, index=index+1, result_path=result_path)
    else:
        return None

####################################################################################

if __name__ == '__main__':
    print("#########################")
    #search_path = '[3]["c31"]["7"][\'test\'][5.0]["7.5"]'
    search_path = "['3']['c31']"
    #search_path = "['d']['3']['c31']"
    print(search_path)
    print(convert_dictkeys_to_list(search_path))
    print("#########################")
    print("\nRESULT:\n")

    #######################            

    result = find_path_of_occurrence(test_dict, search_path)
    print(result)
    print("\n")