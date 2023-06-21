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

def find_path_of_occurrence(nested_dict: dict, search_path: str):
    search_path_list = keylist_from_pattern(search_path)
    return tree_search_recursive(nested_dict, search_path_list)

def tree_search_recursive(nestedDict: dict, pattern: str, path=[], result=[]):
    check_occurrence(nestedDict, pattern, 0)

    for (key, value) in nestedDict.items():
        if key == pattern[0]:
            if check_occurrence(nestedDict, pattern, 0):
                result.append(path + pattern)

        if isinstance(value, dict):
            tree_search_recursive(value, pattern, path + [key], result)
    
    return result


def check_occurrence(nestedDict: dict, pattern: list, startIdx: int):
    if startIdx > len(pattern) - 1:
        return True

    if isinstance(nestedDict, dict) and pattern[startIdx] in nestedDict:
        return check_occurrence(nestedDict[pattern[startIdx]], pattern, startIdx + 1)
    else:
        return False


def keylist_from_pattern(pattern: str):
    key_list = pattern.strip("[]").split("][")
    key_list = \
        [int(item) if item.isdecimal() else float(item) if item.replace('.', '', 1).isdecimal() else item.replace('"',
                                                                                                                  '').replace(
            "'", "") for item in key_list]
    return key_list


####################################################################################

if __name__ == '__main__':
    # search_path = '[3.0]["c31"]["7"][\'test\'][5.0]["7.5"]'

    search_path = "['3']['c31']"
    # expected: root -> b ->
    # expected: root -> d ->

    #search_path = "['d']['3']['c31']"
    # expected: root ->

    res = find_path_of_occurrence(test_dict, search_path)
    print(res)