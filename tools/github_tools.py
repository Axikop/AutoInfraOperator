import os
from langchain.tools import tool
from github import Github

@tool("GitHub Issue Creation Tool")
def github_issue_creation_tool(repo_url: str, title: str, body: str) -> str:

    try:

        # using an environment variable so apikey is not hardcoded in the script.
        github_token = os.getenv('GITHUB_PAT')
        if not github_token:
            return "Error: I can't create an issue because the GITHUB_PAT is not set in my environment."

        github_api = Github(github_token)
        
        repo_path = "/".join(repo_url.split('/')[-2:])
        
        target_repo = github_api.get_repo(repo_path)
        
        target_repo.create_issue(title=title, body=body)
        
        success_msg = f"I successfully created the issue '{title}' in the {repo_path} repository."
        print(success_msg)
        return success_msg
        
    except Exception as e:
        error_msg = f"Something went wrong when I tried to create a GitHub issue: {e}"
        print(error_msg)
        return error_msg
