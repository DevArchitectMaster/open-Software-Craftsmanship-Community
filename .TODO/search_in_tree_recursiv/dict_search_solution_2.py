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


def tree_search_rec(nestedDict: dict, pattern: str, path: list):
    key_list = keylist_from_pattern(pattern)

    check_occurrence(nestedDict, key_list, 0)

    for (key, value) in nestedDict.items():
        # print(key, value)
        if key == key_list[0]:
            # print("Match first element at ", path)
            if check_occurrence(nestedDict, key_list, 0):
                # found an occurrence
                print(path)

        if isinstance(value, dict):
            tree_search_rec(value, pattern, path + [key])


def check_occurrence(nestedDict: dict, key_list: list, startIdx: int):
    if startIdx > len(key_list) - 1:
        return True

    if isinstance(nestedDict, dict) and key_list[startIdx] in nestedDict:
        return check_occurrence(nestedDict[key_list[startIdx]], key_list, startIdx + 1)
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
    
    search_path = "['3']['c31']"
    # expected: root -> b ->
    # expected: root -> d ->

    #search_path = "['d']['3']['c31']"
    # expected: root ->


    # print(search_path)

    tree_search_rec(test_dict, search_path, [])