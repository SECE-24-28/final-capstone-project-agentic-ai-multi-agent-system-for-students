from services.gemini import generate
from services.vector_store import retrieve_startups


def retrieve_yc_context(startup_context):

    query = f"""
    {startup_context['problem']}
    {startup_context['solution']}
    {startup_context['target_users']}
    """

    return retrieve_startups(
        query=query,
        n_results=10
    )


def startup_feature_agent(
    startup_context,
    yc_docs
):

    docs_text = "\n\n".join(yc_docs)

    prompt = f"""
You are an elite startup CTO.

Startup:
{startup_context}

Similar YC Startups:
{docs_text}

Generate:

1. MVP Features
2. Premium Features
3. Differentiators
4. Competitive Advantages

Return ONLY valid JSON.
"""

    return generate(prompt)


def tech_stack_agent(
    startup_context,
    yc_docs
):

    docs_text = "\n\n".join(yc_docs)

    prompt = f"""
Startup:
{startup_context}

Similar YC Startups:
{docs_text}

Design best production-ready stack.

Prefer:
- Python
- FastAPI
- PostgreSQL
- ChromaDB

Return ONLY valid JSON.
"""

    return generate(prompt)


def database_agent(
    startup_context,
    features
):

    prompt = f"""
Startup:
{startup_context}

Features:
{features}

Design database schema.

Return ONLY valid JSON.
"""

    return generate(prompt)


def api_agent(
    startup_context,
    features
):

    prompt = f"""
Startup:
{startup_context}

Features:
{features}

Generate REST APIs.

Return ONLY valid JSON.
"""

    return generate(prompt)


def ui_agent(
    startup_context,
    features
):

    prompt = f"""
Startup:
{startup_context}

Features:
{features}

Design UI.

Return ONLY valid JSON.
"""

    return generate(prompt)


def roadmap_agent(
    startup_context,
    features
):

    prompt = f"""
Startup:
{startup_context}

Features:
{features}

Create 4 week roadmap.

Return ONLY valid JSON.
"""

    return generate(prompt)


def cost_agent(
    startup_context,
    tech_stack
):

    prompt = f"""
Startup:
{startup_context}

Tech Stack:
{tech_stack}

Estimate:

1. Development Cost
2. Monthly Cost
3. AI Cost
4. Hosting Cost

Return ONLY valid JSON.
"""

    return generate(prompt)


def risk_agent(
    startup_context,
    features,
    roadmap
):

    prompt = f"""
Startup:
{startup_context}

Features:
{features}

Roadmap:
{roadmap}

Analyze:

1. Technical Risks
2. Product Risks
3. Market Risks
4. Scaling Risks

Return ONLY valid JSON.
"""

    return generate(prompt)


def founder_fit_agent(
    startup_context
):

    prompt = f"""
Startup:
{startup_context}

Evaluate:

1. Founder Market Fit Score
2. Strengths
3. Weaknesses
4. Recommendations

Return ONLY valid JSON.
"""

    return generate(prompt)


def buildability_agent(
    startup_context,
    features,
    tech_stack
):

    prompt = f"""
Startup:
{startup_context}

Features:
{features}

Tech Stack:
{tech_stack}

Evaluate:

1. Buildability Score
2. Time To MVP
3. Team Size
4. Technical Difficulty

Return ONLY valid JSON.
"""

    return generate(prompt)


def investor_readiness_agent(
    startup_context,
    risks
):

    prompt = f"""
Startup:
{startup_context}

Risks:
{risks}

Evaluate:

1. Investor Readiness Score
2. Strengths
3. Weaknesses
4. Funding Potential

Return ONLY valid JSON.
"""

    return generate(prompt)


def revenue_strategy_agent(
    startup_context
):

    prompt = f"""
Startup:
{startup_context}

Generate:

1. Revenue Model
2. Pricing
3. Monetization Strategy

Return ONLY valid JSON.
"""

    return generate(prompt)


def launch_strategy_agent(
    startup_context
):

    prompt = f"""
Startup:
{startup_context}

Generate:

1. First 100 Users Plan
2. Marketing Channels
3. Growth Strategy

Return ONLY valid JSON.
"""

    return generate(prompt)


def mvp_planner_agent(
    startup_idea
):

    print("Retrieving YC Startups...")
    yc_docs = retrieve_yc_context(startup_idea)

    print("Generating Features...")
    features = startup_feature_agent(
        startup_idea,
        yc_docs
    )

    print("Designing Tech Stack...")
    tech_stack = tech_stack_agent(
        startup_idea,
        yc_docs
    )

    print("Designing Database...")
    database = database_agent(
        startup_idea,
        features
    )

    print("Generating APIs...")
    apis = api_agent(
        startup_idea,
        features
    )

    print("Designing UI...")
    ui = ui_agent(
        startup_idea,
        features
    )

    print("Creating Roadmap...")
    roadmap = roadmap_agent(
        startup_idea,
        features
    )

    print("Estimating Costs...")
    costs = cost_agent(
        startup_idea,
        tech_stack
    )

    print("Analyzing Risks...")
    risks = risk_agent(
        startup_idea,
        features,
        roadmap
    )

    print("Founder Fit...")
    founder_fit = founder_fit_agent(
        startup_idea
    )

    print("Buildability...")
    buildability = buildability_agent(
        startup_idea,
        features,
        tech_stack
    )

    print("Investor Readiness...")
    investor_readiness = investor_readiness_agent(
        startup_idea,
        risks
    )

    print("Revenue Strategy...")
    revenue_strategy = revenue_strategy_agent(
        startup_idea
    )

    print("Launch Strategy...")
    launch_strategy = launch_strategy_agent(
        startup_idea
    )

    return {
        "yc_startups": yc_docs,
        "features": features,
        "tech_stack": tech_stack,
        "database": database,
        "apis": apis,
        "ui": ui,
        "roadmap": roadmap,
        "costs": costs,
        "risks": risks,
        "founder_fit": founder_fit,
        "buildability": buildability,
        "investor_readiness": investor_readiness,
        "revenue_strategy": revenue_strategy,
        "launch_strategy": launch_strategy
    }


if __name__ == "__main__":

    startup = {
        "startup_name": "AdaptaLearn",
        "problem": "Students receive generic learning experiences",
        "solution": "AI powered adaptive learning",
        "target_users": "Students and Teachers"
    }

    result = mvp_planner_agent(
        startup
    )

    for key, value in result.items():

        print("\n")
        print("=" * 80)
        print(key.upper())
        print("=" * 80)

        print(value)