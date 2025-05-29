def get_num_chars_dict(text):
  try:
    chars = {}
    for c in text:
      lowered = c.lower()
      if lowered in chars:
        chars[lowered] += 1
      else:
        chars[lowered] = 1
    return chars
  except Exception as e:
    print(e)

def sort_on(dict):
  return dict["num"]

def char_dict_to_sorted_list(char_dict):
  try:
  
      sorted_list = []
      for ch in char_dict:
        sorted_list.append({"char": ch, "num": char_dict[ch]})
      sorted_list.sort(reverse=True, key=sort_on)
      return sorted_list
      
  except Exception as e:
    print(f"An error occurred: {e}")
    return []


def get_num_words(text):
  try:
    words_count = len(text.split())
    return words_count
  except Exception as e:
    print(e)
