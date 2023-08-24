'''


'''


import asyncio
from datetime import timedelta

from temporalio import workflow

with workflow.unsafe.imports_passed_through():
    from workflowdomain.userflows.user_registration_activity import register_user 


@workflow.defn
class RegisterUserWorkflow:
    
    def __init__(self):
        pass

    @workflow.run
    async def run(self, inputparam:str) -> str:
        try:
            result =await workflow.execute_activity(register_user, "register-user" , start_to_close_timeout=timedelta(seconds=10),)
            return result
            

        except asyncio.CancelledError as err:
            print(err)

