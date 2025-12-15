import os

# 1. Ask for the key
print("Let's set up your API Key safely.")
key = input("Paste your Groq API Key (starts with gsk_): ").strip()

# 2. Check if it looks valid
if not key.startswith("gsk_"):
    print("Warning: That doesn't look like a Groq key (should start with 'gsk_').")
    confirm = input("Are you sure? (y/n): ")
    if confirm.lower() != 'y':
        exit()

# 3. Write the .env file programmatically
file_path = os.path.join(os.getcwd(), ".env")
with open(file_path, "w") as f:
    f.write(f'GROQ_API_KEY="{key}"')

print(f"\n✅ Success! Created correct .env file at: {file_path}")
print("Now try running 'uv run logic.py' again.")