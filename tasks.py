from crewai import Task

# This is where I define the specific task I want my agent to perform.

def create_analysis_task(agent, repo_url):
    analysis_and_reporting_task = Task(
        description=(
            f"Your main goal is to analyze the GitHub repository located at this URL: {repo_url}.\n"
            "Here's your step-by-step plan:\n"
            "1. Start by using the 'Repository Analysis Tool' to get the content of the important files.\n"
            "2. Read through all the file content you get back. Look for common mistakes or things that could be better. For example:\n"
            "   - In a Dockerfile: Are they using an old base image? Are there a bunch of RUN commands that could be combined into one?\n"
            "   - In a requirements.txt: Are the packages pinned to specific versions? (e.g., 'requests==2.28.1' is good, 'requests' is bad).\n"
            "   - In GitHub Actions workflows: Are they using actions that are known to be slow or outdated?\n"
            "3. For every single problem you find, you absolutely MUST use the 'GitHub Issue Creation Tool'. Don't just report one problem, report them all.\n"
            "4. When you use the tool to create an issue, make sure the title is clear and the body is helpful. The body should explain the problem and give a code snippet showing how to fix it.\n"
            "5. If you look through all the files and don't find any problems at all, that's fine. Just finish by saying that the repository looks good."
        ),
        expected_output=(
            "A final summary confirming the actions taken. For example, 'I have created 3 issues in the repository detailing the problems I found.' "
            "Or, if no issues were found, 'I have analyzed the repository and found no issues to report.'"
        ),
        agent=agent
    )
    return analysis_and_reporting_task
