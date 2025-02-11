import os
import git
from datetime import datetime

# Set your GitHub repo path (where your solutions are stored)
REPO_PATH = "C:/Users/hp/Desktop/leetcode-solutions"  # Change this to your actual repo path

def git_push():
    try:
        # Open the Git repository
        repo = git.Repo(REPO_PATH)
        
        # Add all new/modified files
        repo.git.add('--all')

        # Commit with a timestamp message
        commit_message = f"Auto-commit: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        repo.index.commit(commit_message)

        # Push changes to GitHub
        origin = repo.remote(name='origin')
        origin.push()

        print("✅ Successfully pushed to GitHub!")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    git_push()
