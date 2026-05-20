from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field


class HashtagCounterInput(BaseModel):
    """Input schema for HashtagCounterTool."""
    
    argument: str = Field(
        ...,
        description="Social media caption containing hashtags."
    )


class HashtagCounterTool(BaseTool):
    name: str = "Hashtag Counter Tool"

    description: str = (
        "Counts hashtags in a social media caption "
        "and checks whether the hashtag count "
        "is valid for Instagram posting."
    )

    args_schema: Type[BaseModel] = HashtagCounterInput

    def _run(self, argument: str) -> str:
        try:

            hashtags = [
                word for word in argument.split()
                if word.startswith("#")
            ]

            count = len(hashtags)

            print(f"Hashtag count: {count}")

            if count > 30:
                return (
                    f"Too many hashtags: {count}\n"
                    f"Instagram limit exceeded."
                )

            elif count < 3:
                return (
                    f"Too few hashtags: {count}\n"
                    f"Add more hashtags for better reach."
                )

            else:
                return (
                    f"Perfect hashtag count: {count}"
                )

        except Exception as error:
            return f"Tool error: {error}"