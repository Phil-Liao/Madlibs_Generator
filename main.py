# Open the file "story.txt" in read mode
with open("story.txt", 'r') as file:
    lines = file.readlines()

# Initialize an empty list to store new paragraphs
new_paragraph = []

# Iterate over each line in the file
for line in lines:
    # Initialize an empty list to store the indices of underscores
    underscore_indices = []

    # Iterate over each character in the line
    for index in range(len(line)):
        # If the character is an underscore, add its index to the list
        if line[index] == '_':
            underscore_indices.append(index)

    # Calculate the number of groups of underscores
    num_groups = int(len(underscore_indices) / 6)

    # For each group of underscores
    for group in range(1, num_groups + 1):
        # Calculate the start and end indices of the group
        start = underscore_indices[(3 * (group * 2) - 1) - 1] + 2
        end = underscore_indices[(3 * (group * 2) - 1)] - 2
        # The code doesn't currently do anything with these start and end indices
        # You might want to add code here to use them