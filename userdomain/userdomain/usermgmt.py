from dataclasses import dataclass, field
from uuid import UUID, uuid4
from typing import Optional

# Value Objects
@dataclass(frozen=True)
class UserID:
    value: UUID

@dataclass(frozen=True)
class UserStatus:
    value: str

@dataclass(frozen=True)
class Email:
    value: str

@dataclass(frozen=True)
class MobileNumber:
    value: str

@dataclass(frozen=True)
class EmergencyContactNumber:
    value: str

@dataclass(frozen=True)
class BikeType:
    value: str

# Entities
@dataclass
class UserProfile:
    email: Email
    mobile_num: MobileNumber
    emergency_contact_num: EmergencyContactNumber

@dataclass
class UserPreference:
    bike_type: BikeType

# Aggregate Root
@dataclass
class User:
    user_id: UserID
    profile: UserProfile
    status: UserStatus
    preference: Optional[UserPreference] = field(default=None)

    def update_profile(self, new_profile: UserProfile):
        self.profile = new_profile

    def update_preference(self, new_preference: UserPreference):
        self.preference = new_preference

    def activate(self):
        self.status = UserStatus("Active")

    def deactivate(self):
        self.status = UserStatus("Inactive")

# Repository Interface
class IUserRepository:
    def add(self, user: User) -> None:
        raise NotImplementedError

    def get_by_id(self, user_id: UserID) -> Optional[User]:
        raise NotImplementedError

    def update(self, user: User) -> None:
        raise NotImplementedError

    def remove(self, user_id: UserID) -> None:
        raise NotImplementedError

# Mock Repository for demonstration
class MockUserRepository(IUserRepository):
    def __init__(self):
        self.users = {}

    def add(self, user: User) -> None:
        self.users[user.user_id.value] = user

    def get_by_id(self, user_id: UserID) -> Optional[User]:
        return self.users.get(user_id.value)

    def update(self, user: User) -> None:
        self.users[user.user_id.value] = user

    def remove(self, user_id: UserID) -> None:
        self.users.pop(user_id.value, None)

# Example Usage

'''
repo = MockUserRepository()
new_user = User(
    user_id=UserID(uuid4()),
    profile=UserProfile(
        email=Email("john.doe@example.com"),
        mobile_num=MobileNumber("1234567890"),
        emergency_contact_num=EmergencyContactNumber("0987654321")
    ),
    status=UserStatus("Inactive")
)
repo.add(new_user)

# Retrieve and update user
retrieved_user = repo.get_by_id(new_user.user_id)
if retrieved_user:
    retrieved_user.activate()
    new_preference = UserPreference(bike_type=BikeType("Mountain"))
    retrieved_user.update_preference(new_preference)
    repo.update(retrieved_user)
    print(f"{retrieved_user}")
'''
