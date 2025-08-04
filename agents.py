import os
from crewai import Agent
from langchain_groq import ChatGroq
from tools.repository_tools import repository_analysis_tool
from tools.github_tools import github_issue_creation_tool



# It's super fast!
llm = ChatGroq(
    api_key=os.environ.get("GROQ_API_KEY"),
    model="llama3-70b-8192"
)

def create_devops_analyst():
    devops_agent = Agent(
        role='Senior DevOps Analyst',
        goal='Analyze the infrastructure files of a GitHub repository to find problems and suggest improvements.',
        backstory=(
            "You are a very experienced DevOps engineer. You're great at looking at files like Dockerfiles, "
            "requirements.txt, and CI/CD pipelines and spotting where things can be improved. "
            "Your main job is to help other developers by finding these issues and giving them clear, "
            "easy-to-understand advice on how to fix them."
        ),
        tools=[repository_analysis_tool, github_issue_creation_tool],
        llm=llm,
        verbose=True,
        #Setting allow_delegation to False because I want this one agent to do all the work.
        allow_delegation=False
    )
    return devops_agent
