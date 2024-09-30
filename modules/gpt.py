from openai import OpenAI
from modules.tools import *
import json
import inspect
from dotenv import load_dotenv
import time
load_dotenv()

client = OpenAI()   #for openai

# Function to interact with GPT-4 API
def run_conversation(content):
    function_response = None
    messages = [{"role": "system", "content": """You are Jarvis, Bruno's personal assistant, you can do any task that the user wants. Respond in SHORT messages."""},
                {"role": "user", "content": content}]
    
    # API call
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        tools=tools, # type: ignore
        tool_choice="auto",
        temperature=0.7,
    )
    
    response_message = response.choices[0].message
    tool_calls = response_message.tool_calls
    
    if tool_calls:
        messages.append(response_message)

        # Loop through each tool call and invoke the appropriate function
        for tool_call in tool_calls:
            function_name = tool_call.function.name
            function_to_call = available_functions.get(function_name)

            if function_to_call:
                # Get the arguments from the tool call
                function_args = json.loads(tool_call.function.arguments)
                
                # Get the parameters the function actually accepts
                function_params = inspect.signature(function_to_call).parameters
                
                # Filter only the valid arguments for the function
                valid_args = {k: v for k, v in function_args.items() if k in function_params}
                
                # Call the function with the filtered arguments
                function_response = function_to_call(**valid_args)
                
                print(f"Function: {function_name}")
                print(f"Params: {valid_args}")
            time.sleep(1)
        print(f"API: {function_response}")
        if function_response == None:
            return response
        messages.append(
        {
          "tool_call_id": tool_call.id,
          "role": "tool",
          "name": function_name,
          "content": function_response,
        }
        )

        second_response = client.chat.completions.create(
            model="gpt-4o-mini",
            tools=tools, # type: ignore
            messages=messages,
            temperature=0.7,
            )
        return second_response
    return response
                
    


      
