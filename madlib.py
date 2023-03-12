import random

# Saint Madlibs
madlibs = [
    {
        "template": "The story of Saint {name} is quite {adjective},\nFor {pronoun} lived a life of {adjective2} and {adjective3}.\n{pronoun2} preached to the people with {adjective4} words,\nAnd through {pronoun3} {verb} many souls towards the Lord.",
        "prompts": ["name", "adjective", "pronoun", "adjective2", "adjective3", "pronoun2", "adjective4", "pronoun3", "verb"]
    },
    {
        "template": "Saint {name}'s {adjective} life is one to admire,\nFor {pronoun} {verb} with such {adjective2} desire.\n{pronoun2} fought off temptation with {adjective3} grace,\nAnd through {pronoun3} {verb2} {noun} in the Lord's holy place.",
        "prompts": ["name", "adjective", "pronoun", "verb", "adjective2", "pronoun2", "adjective3", "pronoun3", "verb2", "noun"]
    },
    {
        "template": "The life of Saint {name} was a {adjective} one indeed,\nFor {pronoun} {verb} with {adjective2} and {adjective3} deeds.\n{pronoun2} prayed with {adjective4} devotion,\nAnd through {pronoun3} {verb2} {noun2} showed true emotion.",
        "prompts": ["name", "adjective", "pronoun", "verb", "adjective2", "adjective3", "pronoun2", "adjective4", "pronoun3", "verb2", "noun2"]
    },
    {
        "template": "Saint {name} is known for {adjective} {noun},\nAnd {pronoun} worked miracles {adverb}.\n{pronoun2} spent {number} years {verb} for the Lord,\nAnd {pronoun3} {verb2} {noun2} in {pronoun4} {adjective2} hoard.",
        "prompts": ["name", "adjective", "noun", "pronoun", "adverb", "number", "verb", "pronoun2", "verb2", "noun2", "pronoun3", "pronoun4", "adjective2"]
    },
    {
        "template": "Saint {name} was a {adjective} {noun} in {pronoun}'s eyes,\nAnd {pronoun2} {verb} to live {adverb} {adjective2} lives.\n{pronoun3} showed {adjective3} compassion to the sick and poor,\nAnd through {pronoun4} {verb2} {noun} {pronoun5} {verb3} {adjective4} {noun2} forevermore.",
        "prompts": ["name", "adjective", "noun", "pronoun", "verb", "adverb", "adjective2", "pronoun2", "adjective3", "pronoun3", "verb2", "noun", "pronoun4", "pronoun5", "verb3", "adjective4", "noun2"]
    },
    {
        "template": "Saint {name} {verb} {adverb} to spread {pronoun}'s word,\nAnd {pronoun2} {verb2} {adjective} {noun} that others thought absurd.\n{pronoun3} showed {adjective2} strength in times of great strife,\nAnd through {pronoun4} {verb3} {noun2} {pronoun5} {verb4} {adjective3} life.",
        "prompts": ["name", "verb", "adverb", "pronoun", "verb2", "adjective", "noun", "pronoun2", "adjective2", "pronoun3", "verb3", "noun2", "pronoun4", "pronoun5", "verb4", "adjective3"]
    }

    ]

# Randomly select a madlib
selected_madlib = random.choice(madlibs)

# Print the madlib for the user to see
print(selected_madlib["template"])

# Get user input for each blank space in the madlib
prompts = selected_madlib["prompts"]
user_inputs = {}
for prompt in prompts:
    user_input = input(f"Enter {prompt}: ")
    user_inputs[prompt] = user_input

# Fill in the blanks of the selected madlib with the user's inputs
completed_madlib = selected_madlib["template"].format(**user_inputs)

# Print the completed madlib to the console
print(completed_madlib)
