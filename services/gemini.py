import os
import time
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv(
        "GEMINI_API_KEY"
    )
)



def generate(prompt):

    for attempt in range(3):

        try:

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            return response.text

        except Exception as e:

            print(
                f"ERROR (Attempt {attempt+1}/3):",
                e
            )

            time.sleep(5)

    return """
{
    "status": "generation_failed"
}
"""