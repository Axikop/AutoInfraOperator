import streamlit as st
from crewai import Crew, Process
from agents import create_devops_analyst
from tasks import create_analysis_task


st.title("🤖 AutoInfraOp: AI DevOps Agent")

st.markdown("Enter a public GitHub repository URL and the AI agent will analyze its infrastructure and create issues for any problems it finds.")

repo_url = st.text_input(
    "GitHub Repository URL", 
    placeholder="e.g., https://github.com/Axikop/ProjectX"
)

if st.button("Analyze Repository"):
    if repo_url:
        with st.spinner("Agent is analyzing the repository... This might take a minute..."):
            try:
                # This is where I should set up and run my CrewAI

                devops_agent = create_devops_analyst()

                analysis_task = create_analysis_task(devops_agent, repo_url)

                autoinfra_crew = Crew(
                    agents=[devops_agent],
                    tasks=[analysis_task],
                    process=Process.sequential, 
                    verbose=2 
                )

                result = autoinfra_crew.kickoff()

                st.success("Analysis complete!")
                st.markdown("### Final Result from the Agent:")
                st.write(result)
                st.info("Check the 'Issues' tab of the target repository to see the agent's work!")

            except Exception as e:
                st.error(f"An error occurred while running the agent: {e}")
    else:
        st.warning("Please enter a GitHub repository URL to start the analysis.")
