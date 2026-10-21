# PET SHOP SEARCH
# ---------- SETUP (given to you) ----------
PETS = ["hamster", "rabbit", "parrot", "goldfish", "turtle", "puppy", "kitten", "guinea pig"]
MAX_FIXES = 2

TEST_SEARCHES = [
    ("hamstr", "hamster"),
    ("rabit", "rabbit"),
    ("parott", "parrot"),
    ("gold fish", "goldfish"),
    ("puppee", "puppy"),
    ("pig", "guinea pig"),
]

# ---------- PART 1: edit distance ----------
def edit_distance(a, b):
    # Using dynamic programming table
    table = [[i + j for j in range(len(b) + 1)] for i in range(len(a) + 1)]
    for i in range(len(a) + 1):
        table[i][0] = i
    for j in range(len(b) + 1):
        table[0][j] = j
        
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            cost = 0 if a[i - 1] == b[j - 1] else 1
            table[i][j] = min(table[i - 1][j] + 1, table[i][j - 1] + 1, table[i - 1][j - 1] + cost)
            
    return table[len(a)][len(b)]

print("PART 1: Edit distance")
print(edit_distance("cat", "cut"), edit_distance("rabit", "rabbit"))

# ---------- PART 2: find the closest pet ----------
def closest(search):
    # min() can find the pet with the smallest edit distance automatically
    return min(PETS, key=lambda pet: edit_distance(search, pet))

print("\nPART 2: Closest pet")
print(closest("parott"))

# ---------- PART 3: did you mean? ----------
def did_you_mean(search):
    match = closest(search)
    return match if edit_distance(search, match) <= MAX_FIXES else "no match"

print("\nPART 3: Did you mean?")
print(did_you_mean("hamstr"), "|", did_you_mean("elephant"))

# ---------- PART 4: check every test search ----------
print("\nPART 4: Test all searches")
mistakes = 0

for search, wanted in TEST_SEARCHES:
    answer = did_you_mean(search)
    if answer != wanted:
        mistakes += 1
    print(f"Answer: {answer} | Search: {search}")

print(f"Mistakes: {mistakes} out of {len(TEST_SEARCHES)}")