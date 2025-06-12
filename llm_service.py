"""
LLM service layer for processing hotel queries
"""
import os

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.schema import HumanMessage
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
from hotel_tools import TOOLS, search_hotels, get_hotel_details, calculate_booking_cost, get_available_locations
load_dotenv()

def get_llm():
    """Initialize and return LLM instance"""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise EnvironmentError("OPENAI_API_KEY not set.")
    return init_chat_model("openai:gpt-4.1")


def process_hotel_query(query: str) -> str:
    """
    Process a hotel-related query and return a string response.

    Args:
        query: The hotel-related question or request

    Returns:
        String response with hotel information
    """
    try:
        llm = get_llm()
        llm_with_tools = llm.bind_tools(TOOLS)

        messages = [HumanMessage(query)]
        ai_msg = llm_with_tools.invoke(messages)

        # Process tool calls if any
        if hasattr(ai_msg, 'tool_calls') and ai_msg.tool_calls:
            # Add the AI message with tool calls to the conversation
            messages.append(ai_msg)

            # Tool mapping
            tool_map = {
                "search_hotels": search_hotels,
                "get_hotel_details": get_hotel_details,
                "calculate_booking_cost": calculate_booking_cost,
                "get_available_locations": get_available_locations
            }

            # Execute each tool call and add results to messages
            for tool_call in ai_msg.tool_calls:
                tool_name = tool_call["name"]
                tool_args = tool_call["args"]
                tool_id = tool_call["id"]

                # Find and execute the tool
                selected_tool = tool_map.get(tool_name.lower())
                if selected_tool:
                    try:
                        # Try invoke method first, fallback to direct call
                        if hasattr(selected_tool, 'invoke'):
                            tool_output = selected_tool.invoke(tool_args)
                        else:
                            # If tool is a direct function, call it with unpacked args
                            tool_output = selected_tool(**tool_args)

                        # Add tool result to messages
                        messages.append(ToolMessage(
                            content=str(tool_output),
                            tool_call_id=tool_id
                        ))
                    except Exception as tool_error:
                        # Handle tool execution errors
                        error_msg = f"Error executing {tool_name}: {str(tool_error)}"
                        messages.append(ToolMessage(
                            content=error_msg,
                            tool_call_id=tool_id
                        ))
                else:
                    # Handle unknown tools
                    error_msg = f"Unknown tool: {tool_name}"
                    messages.append(ToolMessage(
                        content=error_msg,
                        tool_call_id=tool_id
                    ))

            # Get final AI response after tool execution
            final_response = llm_with_tools.invoke(messages)
            return final_response.content if hasattr(final_response, 'content') else str(final_response)

        else:
            # Return direct AI response if no tools were called
            return ai_msg.content if hasattr(ai_msg, 'content') else str(ai_msg)

    except Exception as e:
        return f"Error processing query: {str(e)}"