# 🤖 AutoInfraOp: The AI DevOps Agent

This project is a powerful demonstration of a modern, tool-based AI agent built with CrewAI and LangChain. The agent acts as an autonomous DevOps assistant, capable of analyzing a public GitHub repository's infrastructure configuration, identifying best-practice violations, and automatically creating detailed issues with AI-generated suggestions for fixes.

This project showcases a practical application of Large Language Models (LLMs) to solve a real-world software engineering problem, bridging the gap between AI and DevOps.


---


## 📊 Project in Action

The application features a simple Streamlit UI where a user can input a GitHub repository URL. The agent then begins its analysis, and its final report and actions (the created GitHub issues) can be seen in the target repository.

![AutoInfraOp UI](https://github.com/Axikop/AutoInfraOperator/blob/main/Screenshot%202025-08-05%20223712.png?raw=true)

---

---

## 🚀 How to Run This Project

### Prerequisites
* Python 3.10+
* A **Groq API Key**.
* A **GitHub Personal Access Token (PAT)** with `repo` scope.

### Step 1: Clone and Configure
1.  Clone this repository to your local machine.
2.  Create a file named `.env` in the root of the project.
3.  Add your secret keys to the `.env` file like this:
    ```
    GROQ_API_KEY="gsk_..."
    GITHUB_PAT="ghp_..."
    ```

### Step 2: Install Dependencies
From the project's root directory, install all the required Python libraries.
```
pip install -r requirements.txt
```

Step 3: Launch the Application
Run the Streamlit app from your terminal.
```
streamlit run app.py

```
A new browser tab will open with the AutoInfraOp dashboard, ready for you to use!
