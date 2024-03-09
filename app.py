import os
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_google_genai import ChatGoogleGenerativeAI
from crewai import Agent, Task, Crew
import streamlit as st
import dotenv

import PIL.Image
import google.generativeai as genai
dotenv.load_dotenv()

# Load the Google API key from the environment variables
GOOGLE_API_KEY = os.environ['GOOGLE_API_KEY']

# Configure the generative AI with the Google API key
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize the DuckDuckGo search tool
search_tool = DuckDuckGoSearchRun()

# Initialize the ChatGoogleGenerativeAI model
llm = ChatGoogleGenerativeAI(model="gemini-pro",
               verbose=True,
               temperature=0.1,
               convert_system_message_to_human=True,
               google_api_key=GOOGLE_API_KEY)

def key(path):
  """
  Extracts keywords from an image using generative AI.
  """
  image = PIL.Image.open(path)
  vision_model = genai.GenerativeModel('gemini-pro-vision')
  response = vision_model.generate_content(["Describe all details about this image. generate 5 best keywords related to image example keyword1 : car , keyword2 : snow,..... Remmeber only return Keywords, Strictly o other text ", image])
  return response.text

def crew_run(Topic):
  """
  Runs the hashtag generation crew for a given topic.
  """
  try:
    Hashtag_Generator = Agent(
      role='The Best Hashtag Generator',
      goal=f"""Being the best at creating most innovative and finding
      latest trending hashtags that resonate with the {Topic} in 2024.
      Ask question one by one for every keyword on website - https://best-hashtags.com/hashtag/[keyword1] ? ,
      example - What are some trending hashtags on website [keyword1] ...
      Use Most popular hastags in final output.""",
      backstory="""Known as the BEST hashtag generator, Finder and researcher, you're
      adept at crafting and Fining hashtags that not only trend but also
      drive engagement and reach. Now you're working on a super
      important campaign""",
      llm=llm,
      tools=[search_tool],
      verbose=True,
      allow_delegation=False
    )

    write_task = Task(
      description=(
        f"""\Generate a list of 5 innovative and 5 trending hashtags for the {Topic} that are likely to trend and are already trending on social media platforms in 2024.
        and engage the target audience. Utilize tools and resources to create a list of
        potential hashtags that resonate with the audience's interests and the current
        trends in social media."""
      ),
      expected_output=f"""
        A report that includes a list of suggested hashtags, along with an short explanation of why each
        hashtag is likely to be effective for the {Topic}.""",
      tools=[search_tool],
      agent=Hashtag_Generator,
    )

    crew = Crew(
      agents=[Hashtag_Generator],
      tasks=[write_task],
    )
    result = crew.kickoff()
    return result
  except Exception as e:
    return str(e)

def main():
  """
  Main function to run the hashtag research and generation app.
  """
  st.title("Hashtag Research and Generation App")
  st.write("This app helps you conduct hashtag research and generate hashtags for your topic.")
  path = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"]) # Upload an image
  if path is not None:
    try:
      image = PIL.Image.open(path) # Open the image
      st.image(image, width=300) # Display the image
      if st.button("Run"):
        with st.spinner('Running...'):
          keywords = key(path) # Extract keywords from the image
          if keywords:
            result = crew_run(keywords) # Run the hashtag generation crew
            st.write(result) # Display the result
            st.balloons()
          else:
            st.write("No keywords found in the image.") # If no keywords are found
    except Exception as e:
      st.write(f"Error: {str(e)}")
  else:
    st.write("Please upload an image.") # If no image is uploaded

if __name__ == "__main__":
  main()
