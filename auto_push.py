import os
import random
import time

MIN_DELAY = 3
MAX_DELAY = 4
repeat = 20

tracked_files = os.popen("git ls-files").read().splitlines()

valid_files = [f for f in tracked_files if f.endswith((
    ".js", ".py", ".php", ".java", ".cpp", ".ts"
))]

if not valid_files:
    print("No valid tracked code files found.")
    exit()

def get_comment_symbol(filename):
    if filename.endswith(".py"):
        return "#"
    else:
        return "//"

for i in range(1, repeat + 1):

    file_to_edit = random.choice(valid_files)
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

    comment_symbol = get_comment_symbol(file_to_edit)

    with open(file_to_edit, "a") as f:
        f.write(f"\n{comment_symbol} minor update at {timestamp} - iteration {i}\n")

    commit_message = f"Update {file_to_edit} at {timestamp}"

    os.system("git add .")
    os.system(f'git commit -m "{commit_message}"')
    os.system("git push")

    print(f"✅ {commit_message}")

    delay = random.uniform(MIN_DELAY, MAX_DELAY)
    time.sleep(delay)

print("🎉 Done safely!")