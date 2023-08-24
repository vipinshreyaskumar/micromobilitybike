'''

'''


import asyncio
from workflowdomain.userflows.user_registration_worker import RegisterUserWorkflow
from temporalio.client import Client

async def main():
    # Create client connected to server at the given address
    client = await Client.connect("localhost:7233")

    # Execute a workflow
    result = await client.execute_workflow(
        RegisterUserWorkflow.run, "user-reg-reg", id="user-registration-workflow", task_queue="user_registration_queue"
    )

    print(f"Result: {result}")


if __name__ == "__main__":
    asyncio.run(main())
