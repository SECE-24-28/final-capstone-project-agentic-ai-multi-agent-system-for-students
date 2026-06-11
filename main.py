
from agents.agent1 import startup_discovery_agent
from agents.market_research_agent import market_research_agent


def main():

    user_profile = {

        "skills":
        "Python, React",

        "interests":
        "AI Education",

        "experience":
        "Student",

        "budget":
        "Low",

        "goal":
        "Build SaaS Startup"
    }

    print("\n" + "=" * 80)
    print("RUNNING AGENT 1")
    print("=" * 80)

    agent1_result = startup_discovery_agent(
        user_profile
    )

    blueprint = agent1_result.get(
        "blueprint"
    )
    print("\nBLUEPRINT TYPE:")
    print(type(blueprint))

    print("\nBLUEPRINT:")
    print(blueprint)

    print("\n" + "=" * 80)
    print("RUNNING AGENT 2")
    print("=" * 80)

    if blueprint:

        agent2_result = market_research_agent(
            blueprint=blueprint
        )

    else:

        print(
            "\nAgent 1 failed. Using fallback startup.\n"
        )

        fallback_startup = {

            "startup_name":
            "CurricuLabs AI",

            "problem":
            "Teachers spend too much time creating personalized content",

            "solution":
            "AI powered content generation",

            "target_users":
            "Teachers",

            "skills":
            "Python, React",

            "experience":
            "Student",

            "budget":
            "Low",

            "goal":
            "Build SaaS Startup"
        }
        
        agent2_result = market_research_agent(
            startup_idea=fallback_startup
        )

    print("\n" + "=" * 80)
    print("FINAL VALIDATED STARTUP")
    print("=" * 80)

    print("\nSTARTUP BLUEPRINT:\n")
    print(
        blueprint
    )

    print("\n" + "=" * 80)

    print("\nMARKET VALIDATION:\n")
    print(
        agent2_result.get(
            "validation",
            "No validation available"
        )
    )

    print("\n" + "=" * 80)

    print("\nINVESTOR FEEDBACK:\n")
    print(
        agent2_result.get(
            "investor_feedback",
            "No investor feedback available"
        )
    )

    print("\n" + "=" * 80)


if __name__ == "__main__":
    main()

