from groq import Groq
import os
import time
import logging
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

MAX_RETRIES = 3
RETRY_DELAY = 2


def call_llm(messages):

    for attempt in range(MAX_RETRIES):

        try:

            logging.info("Sending request to LLM")

            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=messages,
                temperature=0
            )

            logging.info("LLM response received")

            return response.choices[0].message.content

        except Exception as e:

            logging.error(f"LLM error: {e}")

            if attempt < MAX_RETRIES - 1:

                time.sleep(RETRY_DELAY)

            else:

                return "AI service unavailable."

def stream_llm(messages):

    try:

        logging.info("Streaming request started")

        stream = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=messages,
            temperature=0.7,
            stream=True
        )

        full_response = ""
        tokencount=0
        for chunk in stream:
            tokencount= tokencount+1
            print(tokencount)
            token = chunk.choices[0].delta.content

            if token:
                
                print(token, end="", flush=True)
                full_response += token

        print()

        logging.info("Streaming completed")

        return full_response

    except Exception as e:

        logging.error(f"Streaming failed: {e}")
        return "Streaming error occurred."
    
def call_llm_with_tools(messages, tools):

    response = client.chat.completions.create(

        model="llama-3.1-8b-instant",

        messages=messages,

        tools=tools,

        tool_choice="auto"

    )

    return response