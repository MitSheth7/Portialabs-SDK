import os
import time
import json
from dotenv import load_dotenv
from portia import Portia, default_config, example_tool_registry, LLMProvider, LLMModel, StorageClass
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_environment():
    """Load environment variables and check for the presence of necessary keys."""
    load_dotenv()
    if not os.getenv("PORTIA_API_KEY"):
        print("Error: PORTIA_API_KEY not found in environment variables.")
        exit(1)

def wait_with_message(seconds, message):
    """Wait for specified seconds while showing a countdown message."""
    for i in range(seconds, 0, -1):
        print(f"\r{message} {i} seconds...", end="", flush=True)
        time.sleep(1)
    print("\r" + " " * 50 + "\r", end="", flush=True)  # Clear the line

def display_plan_results(plan_run):
    """Display the results of plan execution in a user-friendly way."""
    try:
        if hasattr(plan_run, 'state'):
            print(f"\nPlan State: {plan_run.state}")
        
        if hasattr(plan_run, 'outputs'):
            print("\nResults:")
            for output in plan_run.outputs:
                if hasattr(output, 'value'):
                    print(f"- {output.value}")
                else:
                    print(f"- {output}")
        else:
            print("\nResults:")
            print(plan_run)
    except Exception as e:
        print(f"\nError displaying results: {e}")
        print("\nRaw output:")
        print(plan_run)

def is_rate_limit_error(error_msg):
    """Check if the error is a rate limit error."""
    rate_limit_indicators = [
        "rate limit",
        "429",
        "too many requests",
        "requests rate limit exceeded"
    ]
    return any(indicator in error_msg.lower() for indicator in rate_limit_indicators)

def main():
    load_environment()  # Ensure environment variables are loaded
    try:
        config = default_config(
            llm_provider=LLMProvider.MISTRALAI,
            llm_model_name=LLMModel.MISTRAL_LARGE,
            storage_class=StorageClass.MEMORY
        )

        portia = Portia(config=config, tools=example_tool_registry)
        print("Successfully initialized Portia client with Mistral AI")

        print("\nTesting with a simple calculation...")
        test_query = "What is 5 plus 3?"
        print(f"Query: {test_query}")
        plan = portia.plan(test_query)
        print("\nGenerated Plan:")
        print(plan.model_dump_json(indent=2))

        print("\nExecuting plan...")
        plan_run = portia.run_plan(plan)
        display_plan_results(plan_run)

        print("\nIf the test was successful, you can now enter your own questions.")
        print("Type 'quit' to exit.")
        print("\nNote: There is a 10-second delay between requests to avoid rate limits.")
        print("\nAvailable operations:")
        print("1. Simple calculations (e.g., 'What is 5 plus 3?', 'Calculate 10 times 4')")
        print("2. Basic arithmetic (e.g., 'What is 20 minus 7?', 'Calculate 15 divided by 3')")
        
        while True:
            user_input = input("\nEnter your calculation (or 'quit' to exit): ")
            if user_input.lower() == 'quit':
                break

            max_retries = 3
            retry_count = 0
            base_wait_time = 10
            
            while retry_count < max_retries:
                try:
                    print("\nGenerating plan...")
                    plan = portia.plan(user_input)
                    print("\nGenerated Plan:")
                    print(plan.model_dump_json(indent=2))

                    print("\nExecuting plan...")
                    plan_run = portia.run_plan(plan)
                    display_plan_results(plan_run)
                    break
                except Exception as e:
                    error_msg = str(e)
                    logger.error(f"Error occurred: {error_msg}")
                    
                    if is_rate_limit_error(error_msg):
                        retry_count += 1
                        wait_time = base_wait_time * retry_count
                        print(f"\nRate limit reached. Attempt {retry_count} of {max_retries}")
                        print(f"Waiting {wait_time} seconds before retrying...")
                        wait_with_message(wait_time, "Waiting")
                        continue
                    else:
                        print(f"\nError: {error_msg}")
                        print("\nTip: Try rephrasing your question to use basic arithmetic operations.")
                        print("For example, instead of 'cube root of 27', try 'What is 27 divided by 3?'")
                        break
            
            if retry_count >= max_retries:
                print("\nMaximum retries reached. Please try again later.")
            
            print("\nWaiting 10 seconds before next request...")
            wait_with_message(10, "Waiting")

    except Exception as e:
        print(f"Error: {e}")
        print("\nDetailed error information:")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
