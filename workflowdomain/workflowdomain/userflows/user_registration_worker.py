'''


'''


import asyncio

from temporalio.client import Client
from temporalio.worker import Worker

from workflowdomain.userflows.user_registration_workflow import RegisterUserWorkflow
from workflowdomain.userflows.user_registration_activity import register_user

async def main():
    client = await Client.connect("localhost:7233")

    worker = Worker(
        client,
        task_queue="user_registration_queue",
        workflows=[RegisterUserWorkflow],
        activities=[register_user],
    )
    await worker.run()


if __name__ == "__main__":
    asyncio.run(main())
