import os
import random
import datetime

# Generate a random commit message
messages = [
    "update done 🚀",
    "small tweaks ✨",
    "fixed stuff 🛠️",
    "random push 😅",
    "made it better ✅",
    "minor update 🔧",
    "push and pray 🙏",
    "autopilot mode 🤖",
    "ninja commit 🥷",
    "routine update 🔁"
]

# Optional: include timestamp to avoid duplicate commit messages
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
commit_message = f"{random.choice(messages)} - {timestamp}"

# Run Git commands
os.system("git add .")
os.system(f'git commit -m "{commit_message}"')
os.system("git push")

print(f"\n✅ Pushed with message: {commit_message}")
