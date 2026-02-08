from engineio.payload import Payload
Payload.max_decode_packets = 500  # Increase the limit from the default 16

import chainlit as cl
from core import init_router, TravelLLM
from config import Config
from tools.travel_tools import search_travel
from langchain_core.prompts import PromptTemplate

router = init_router()
smart_llm = TravelLLM(router=router, group="smart-tier")
fast_llm = TravelLLM(router=router, group="fast-tier")


import chainlit as cl

import chainlit as cl

@cl.author_rename
def rename(orig_author: str):
    # This force-renames 'Assistant', 'Chainlit', and your LLM name
    rename_dict = {
        "Assistant": "Multi-Modal Travel Agent",
        "Chainlit": "Multi-Modal Travel Agent",
        "TravelLLM": "Multi-Modal Travel Agent"
    }
    return rename_dict.get(orig_author, "Multi-Modal Travel Agent")

async def run_sandwich(user_query):
    # STEP 1: BRAIN (Planner)
    async with cl.Step(name="Travel Planner", type="run") as step:
        # Load and format the template
        planner_tmpl = PromptTemplate.from_template(Config.load_prompt("planner.txt"))
        # Using a dictionary to fill the template variables
        planner_input = planner_tmpl.format(input=user_query)
        
        plan = await cl.make_async(smart_llm.invoke)(planner_input)
        step.output = plan.content

    # STEP 2: EXECUTOR (Tool Use)
    async with cl.Step(name="Researching Flights & Hotels", type="tool") as step:
        # The search logic is correct
        search_data = await cl.make_async(search_travel)(f"Best travel options for {user_query}")
        step.output = str(search_data)

    # STEP 3: REFINER (Final Consultant)
    async with cl.Step(name="Travel Consultant", type="run") as step:
        # Load the refiner template
        refiner_tmpl = PromptTemplate.from_template(Config.load_prompt("refiner.txt"))
        # Format it with both the research and the original query
        refiner_input = refiner_tmpl.format(context=search_data, user_query=user_query)
        
        final_output = await cl.make_async(smart_llm.invoke)(refiner_input)
        step.output = "Itinerary synthesized successfully."
        
    return final_output.content

@cl.on_message
async def main(message: cl.Message):
    # The 'run_sandwich' function now contains steps that will automatically 
    # appear in the UI while this function is running.
    response_text = await run_sandwich(message.content)
    
    # Send the final response as a normal message
    await cl.Message(content=response_text).send()