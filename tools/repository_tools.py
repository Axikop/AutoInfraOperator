import os
from langchain.tools import tool
from git import Repo
import tempfile
import shutil

# I'm using the @tool decorator from langchain to make it a tool.
@tool("Repository Analysis Tool")
def repository_analysis_tool(repo_url: str) -> str:

    try:
        temp_folder = tempfile.mkdtemp()
        print(f"Cloning the repo from {repo_url} into a temporary folder...")
        
        # This command actually clones the repo.
        Repo.clone_from(repo_url, temp_folder)
        
        all_file_contents = {}
        files_to_look_for = ['Dockerfile', 'requirements.txt']
        
        for file in files_to_look_for:
            path_to_file = os.path.join(temp_folder, file)
            if os.path.exists(path_to_file):
                with open(path_to_file, 'r') as f:
                    all_file_contents[file] = f.read()
                print(f"Successfully read the file: {file}")

        workflows_folder = os.path.join(temp_folder, '.github', 'workflows')
        if os.path.exists(workflows_folder):
            for workflow_filename in os.listdir(workflows_folder):
                # Make sure it's a yml or yaml file.
                if workflow_filename.endswith(('.yml', '.yaml')):
                    path_to_workflow_file = os.path.join(workflows_folder, workflow_filename)
                    with open(path_to_workflow_file, 'r') as f:
                        all_file_contents[f'workflow:{workflow_filename}'] = f.read()
                    print(f"Successfully read the workflow file: {workflow_filename}")

        shutil.rmtree(temp_folder)
        
        if not all_file_contents:
            return "I couldn't find any Dockerfile, requirements.txt, or GitHub workflow files in this repository."
            
        # I'll combine everything into one big string for the agent to analyze.
        combined_text = ""
        for file_name, content in all_file_contents.items():
            combined_text += f"--- Content of {file_name} ---\n{content}\n\n"
            
        return combined_text

    except Exception as e:
        # If anything goes wrong, make sure to still delete the temp folder.
        if 'temp_folder' in locals() and os.path.exists(temp_folder):
            shutil.rmtree(temp_folder)
        print(f"Something went wrong in the repository analysis tool: {e}")
        return f"Error: I couldn't analyze the repository. Maybe the URL is wrong? Error details: {str(e)}"
