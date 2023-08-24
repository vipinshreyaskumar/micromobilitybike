'''

'''


from dataclasses import dataclass

from userdomain.usermgmt import User

from temporalio import activity


@activity.defn
async def register_user(details:str) -> str:
    print(f"registering user {details}")
    return "success"



