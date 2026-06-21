# Function to print dictionary values given the keys
def print_values_of(dictionary, keys):
    for key in keys:
        print(dictionary[key])

# Print dictionary values from simpson_catch_phrases
simpson_catch_phrases = {"lisa": "BAAAAAART!",
                         "bart": "Eat My Shorts!",
                         "marge": "Mmm~mmmmm",
                         "homer": "d'oh!",
                         "maggie": "(Pacifier Suck)"
                         }

# BUG FIX: 'lisa', 'bart', 'homer' were passed as three separate string
# arguments instead of a single list. Wrapped them in a list [] so the
# function receives one 'keys' argument and can iterate over it correctly.
print_values_of(simpson_catch_phrases, ['lisa', 'bart', 'homer'])

'''
    Expected console output:

    BAAAAAART!
    Eat My Shorts!
    d'oh!

'''
