import os

REPO_PATH = r"C:\Users\hp\Desktop\leetcode-solutions"  # Update this with your actual repo path

def auto_push():
    try:
        os.chdir(REPO_PATH)  # Navigate to the repo directory

        # Step 1: Pull latest changes to avoid conflicts
        os.system("git pull --rebase origin main")

        # Step 2: Add all new files
        os.system("git add .")

        # Step 3: Commit changes
        os.system('git commit -m "📌 Auto-update: Added new LeetCode solution"')

        # Step 4: Push to GitHub
        os.system("git push origin main")

        print("✅ Successfully pushed to GitHub!")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    auto_push()
