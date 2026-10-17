import requests


def main():
  print("Welcome to Trivia!")

  while True:
    if input("Press Enter for trivia (or type 'q' to quit): ").strip().lower() == "q":
      print("Goodbye!")
      break

    
    data = requests.get(
        "https://opentdb.com/api.php?amount=1&type=multiple"
    ).json()
    item = data["results"][0]

    print(f"\nQuestion: {item['question']}")
    print(f"Answer: {item['correct_answer']}\n")


if __name__ == "__main__":
  main()