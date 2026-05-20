#!/usr/bin/env python
from itertools import count
import sys
import warnings

from datetime import datetime

try:
    from social_media_content_calender.crew import SocialMediaContentCalender
except ImportError:
    from crew import SocialMediaContentCalender

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information
def save_output(result):

    with open("content_calendar.md", "w", encoding="utf-8") as file:
        file.write(str(result))

    print("File saved as: content_calendar.md")
    


def run_social_media_project():
    """
    Run the crew.
    """
    brand_name = "GlowSkin"

    product_name = "Organic Skincare"

    target_audience = (
        "Young adults interested in skincare"
    )

    content_pillars = [
        "Educational",
        "Promotional",
        "Engagement",
        "Behind the Scenes"
    ]

    platforms = [
        "Instagram",
        "TikTok",
        "LinkedIn",
        "X"
    ]

    
    inputs = {

        "topic": "Social Media Marketing",

        "brand_name": brand_name,

        "product_name": product_name,

        "target_audience": target_audience,

        "content_pillars": (
            ", ".join(content_pillars)
        ),

        "platforms": (
            ", ".join(platforms)
        )
    }



    result = (
        SocialMediaContentCalender()
        .crew()
        .kickoff(inputs=inputs)
        
    )

    save_output(result)

    print(
        "\n Content calendar generated successfully!"
    )

  

def main():
    run_social_media_project()


if __name__ == "__main__":
    main()

def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs",
        'current_year': str(datetime.now().year)
    }
    try:
        SocialMediaContentCalender().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        SocialMediaContentCalender().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }

    try:
        SocialMediaContentCalender().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

def run_with_trigger():
    """
    Run the crew with trigger payload.
    """
    import json

    if len(sys.argv) < 2:
        raise Exception("No trigger payload provided. Please provide JSON payload as argument.")

    try:
        trigger_payload = json.loads(sys.argv[1])
    except json.JSONDecodeError:
        raise Exception("Invalid JSON payload provided as argument")

    inputs = {
        "crewai_trigger_payload": trigger_payload,
        "topic": "",
        "current_year": ""
    }

    try:
        result = SocialMediaContentCalender().crew().kickoff(inputs=inputs)
        return result
    except Exception as e:
        raise Exception(f"An error occurred while running the crew with trigger: {e}")
