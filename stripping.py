# ask user for their name
name = input("What's your name? ").strip().title()

# Split user's name into first name and last name
first, last = name.split(" ")

# remove whitespace from str and capitalize (.strip delete spaces both left and right)
#name = name.strip().title()

#capitalize user's name (First Letter .capitalize) (All letters in the beginning .title)
#name = name.title()

#say hello to user
print(f"Hello, {first}")