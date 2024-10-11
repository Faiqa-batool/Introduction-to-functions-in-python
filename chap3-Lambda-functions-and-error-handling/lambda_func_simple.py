# Define echo_word as a lambda function: echo_word
echo_word = lambda word1, echo : word1 * echo

# Call echo_word: result
result = echo_word('hey', 5)

# Print result
print(result)

# lambda funstion with map() function

# Create a list of strings: spells
spells = ["protego", "accio", "expecto patronum", "legilimens"]

# Use map() to apply a lambda function over spells: shout_spells
shout_spells = map(lambda item: item+'!!!', spells)

# Convert shout_spells to a list: shout_spells_list
shout_spells_list=list(shout_spells)

# Print the result
print(shout_spells_list)