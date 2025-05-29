from stats import *
import sys

def get_book_path():
  if len(sys.argv) != 2:
    print(f"Usage: python3 {sys.argv[0]} <path_to_book>")
    sys.exit(1)
  return sys.argv[1]


def get_book_text(file_path):
  try:
    with open(file_path, "r") as file:
      text = file.read()
      return text
  except Exception as e:
      print(f"an {e} had occured")
      
def main():

  book_path = get_book_path()
  text = get_book_text(book_path)

  #call func
  words_count = get_num_words(text)
  chars_count = get_num_chars_dict(text)
  sorted_list = char_dict_to_sorted_list(chars_count)

  #print output
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {book_path}...")
  print("----------- Word Count ----------")
  print(f"Found {words_count} total words")
  print("--------- Character Count -------")
  for item in sorted_list:
    if item["char"].isalpha():
      print(f"{item["char"]}: {item["num"]}")
  print("============= END ===============")
  


main()
