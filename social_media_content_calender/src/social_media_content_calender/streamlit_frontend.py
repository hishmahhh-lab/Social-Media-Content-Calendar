import streamlit as st
from datetime import datetime

from social_media_content_calender.crew import ( SocialMediaContentCalender )
from social_media_content_calender.tools.custom_tool import HashtagCounterTool

hashtag_counter = HashtagCounterTool()
def main():

    st.set_page_config(
        page_title="Social Media Content Calendar",
        layout="wide"
    )

    st.title(" Social Media Content Calendar")

    st.write(
        "Generate a 2-week social media "
        "content calendar using CrewAI."
    )

    st.sidebar.title("Brand Details")

    brand_name = st.sidebar.text_input(
        "Brand Name"
    )

    product_name = st.sidebar.text_input(
        "Product / Service"
    )

    target_audience = st.sidebar.text_area(
        "Target Audience"
    )

    content_pillars = st.sidebar.multiselect(
        "Content Pillars",

        [
            "Educational",
            "Promotional",
            "Engagement",
            "Behind the Scenes",
            "Trends",
            "Testimonials"
        ]
    )

    platforms = st.sidebar.multiselect(
        "Platforms",

        [
            "Instagram",
            "TikTok",
            "LinkedIn",
            "X",
            "Facebook"
        ]
    )
    if st.sidebar.button(
        "Generate Calendar"
    ):

        if (
            brand_name and
            product_name and
            target_audience and
            content_pillars and
            platforms
        ):

            inputs = {

                "brand_name": brand_name,

                "product_name": product_name,

                "target_audience": target_audience,

                "content_pillars": (
                    ", ".join(content_pillars)
                ),

                "platforms": (
                    ", ".join(platforms)
                ),

                "current_year": str(
                    datetime.now().year
                )
            }
            with st.spinner(
                "Generating content calendar..."
            ):
                try:
                    result = (
                        SocialMediaContentCalender()
                        .crew()
                        .kickoff(inputs=inputs)
                    )
                    tool = HashtagCounterTool()

                    hashtag_counter = tool.run(
                        argument=str(result)
)

                    st.success(" Content calendar generated!")
                    st.subheader(
                        " Generated Content Calendar"
                    )

                    st.markdown(str(result))
                    st.subheader("Hashtag Analysis")
                    st.info(hashtag_counter)
                
                    st.download_button(
                        label="Download Calendar",

                        data=str(result),

                        file_name=(
                            "content_calendar.md"
                        ),

                        mime="text/markdown"
                    )

                except Exception as error:

                    st.error(
                        f" Error: {error}"
                    )

        else:

            st.sidebar.error(
                "Please fill all fields."
            )
if __name__ == "__main__":
    main()


                    
