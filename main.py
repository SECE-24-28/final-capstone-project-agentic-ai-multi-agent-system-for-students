from services.vector_store import store_documents
from agents.agent1 import startup_discovery_agent

store_documents()

user_profile = {
    "skills": "Python, React",
    "interests": "AI Education",
    "experience": "Student",
    "budget": "Low",
    "goal": "Build SaaS Startup"
}

result = startup_discovery_agent(
    user_profile
)

print(result["blueprint"])

