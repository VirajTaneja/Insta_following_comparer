from bs4 import BeautifulSoup

# Function for username extraction from the files
def extract_usernames(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'lxml')

    usernames = [a.get_text() for a in soup.find_all('a') if a.get_text()]
    return set(usernames)

# Paths to the HTML files form instagram
following_file = 'following.html'
followers_file = 'followers_1.html'

# Extract usernames
following = extract_usernames(following_file)
followers = extract_usernames(followers_file)

# Compare sets
not_following_back = following - followers
not_followed_by_you = followers - following

# Output results
print(" People you follow but who don't follow you back:")
print(f"Total: {len(not_following_back)}\n")
for user in sorted(not_following_back):
    print(user)

print("\n People who follow you but you don't follow back:")
print(f"Total: {len(not_followed_by_you)}\n")
for user in sorted(not_followed_by_you):
    print(user)
