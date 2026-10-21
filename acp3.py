# CANTEEN COMMENT BOX
# ---------- SETUP (given to you) ----------
LEXICON = {
    "delicious": 3, "great": 3, "tasty": 2, "kind": 2, "fresh": 2, "good": 2,
    "cold": -1, "slow": -1, "bad": -2, "rude": -2, "burnt": -2, "awful": -3,
}
NEGATIONS = {"not", "never", "no"}
PUNCTUATION = ".,!?:;\"'()"

TEST_COMMENTS = [
    ("The pasta was delicious and the staff were kind", "HAPPY"),
    ("The queue was slow and the juice was awful", "UNHAPPY"),
    ("Not good, the rice was cold", "UNHAPPY"),
    ("Not bad at all, I will come again", "HAPPY"),
    ("Lunch is at 1 pm on Fridays", "OK"),
    ("Great, they ran out of food again", "UNHAPPY"),
]

# ---------- PART 1: clean the words ----------
def clean_words(comment):
    # Split the comment, make each word lowercase, strip PUNCTUATION from both ends,
    # collect the words in a list and return the list.
    cleaned = []
    for word in comment.split():
        w = word.lower().strip(PUNCTUATION)
        if w:
            cleaned.append(w)
    return cleaned

print("PART 1: Clean words")
print(clean_words("Not GOOD, the rice was cold!"))

# ---------- PART 2: score the comment ----------
def comment_score(comment):
    # Go through clean_words(comment). A word in NEGATIONS turns on a flip.
    # A word in LEXICON adds its points (the opposite sign if the flip is on),
    # and then turns the flip off. Return the total score.
    total = 0
    flip = False
    
    for word in clean_words(comment):
        if word in NEGATIONS:
            flip = True
        elif word in LEXICON:
            points = LEXICON[word]
            if flip:
                total -= points
                flip = False
            else:
                total += points
                
    return total

print("\nPART 2: Score")
print(comment_score("Not good, the rice was cold"))

# ---------- PART 3: decide the mood ----------
def mood(comment):
    # Return "HAPPY" if the score is 1 or more, "UNHAPPY" if it is -1 or less, otherwise "OK".
    score = comment_score(comment)
    if score >= 1:
        return "HAPPY"
    elif score <= -1:
        return "UNHAPPY"
    else:
        return "OK"

print("\nPART 3: Mood")
print(mood("The pasta was delicious and the staff were kind"))

# ---------- PART 4: check every test comment ----------
print("\nPART 4: Test all comments")
mistakes = 0

for comment, expected in TEST_COMMENTS:
    m = mood(comment)
    score = comment_score(comment)
    if m != expected:
        mistakes += 1
    print(f"{m} (Score: {score}): {comment}")

print(f"Mistakes: {mistakes} out of {len(TEST_COMMENTS)}")