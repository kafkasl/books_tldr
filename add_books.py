import os

# Get a list of all files and directories in the root directory
root_dir = os.getcwd()
files_and_dirs = os.listdir(root_dir)

# Filter out the README.md file
books = [f for f in files_and_dirs if f != 'README.md']

# Format the list as a Markdown list
markdown_list = "\n".join([f"- [{book}](./{book})" for book in books])

# Open the README.md file and append the list
with open('README.md', 'a') as readme:
    readme.write("\n## Books in this Repository\n")
    readme.write(markdown_list)
