import os
import subprocess

# Set the path to your local repository
REPO_PATH = r"C:\Users\hp\Desktop\leetcode-solutions"

def git_push():
    try:
        os.chdir(REPO_PATH)  # Navigate to the repository folder

        # Check for changes
        status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
        if not status.stdout.strip():
            print("✅ No new changes to push.")
            return

        # Add all changes
        subprocess.run(["git", "add", "."], check=True)

        # Commit the changes with a message
        commit_message = "📌 Auto-update: Added new LeetCode solution"
        subprocess.run(["git", "commit", "-m", commit_message], check=True)

        # Push to GitHub
        subprocess.run(["git", "push"], check=True)

        print("🚀 Changes successfully pushed to GitHub!")

    except subprocess.CalledProcessError as e:
        print(f"❌ Git error: {e}")

if __name__ == "__main__":
    git_push()
