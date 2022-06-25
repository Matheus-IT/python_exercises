from abc import ABC
from typing import Dict, List


# Roles ----------------------------------------------------------------------


class Role(ABC):
    @property
    def name(self) -> str:
        raise NotImplementedError


class AdminRole(Role):
    @property
    def name(self):
        return 'Admin'


class ReaderRole(Role):
    @property
    def name(self):
        return 'Reader'


# Actions --------------------------------------------------------------------


class Action(ABC):
    @property
    def name(self) -> str:
        raise NotImplementedError

    def perform(self):
        raise NotImplementedError


def InvoiceAction(Action):
    @property
    def name(self):
        return 'Invoicing'

    def perform(self):
        print('Invoicing someone...')


# ----------------------------------------------------------------------------


class RoleValidation:
    def __init__(self):
        self.role_map: Dict[Role, List[Action]] = []

    def assign_action_to_role(self, action: Action, role: Role):
        self.role_map[role].append(action)

    def get_actions_of_role(self, role: Role):
        return self.role_map[role]


class User:
    def __init__(self):
        self.roles: List[Role] = []

    def add_role(self, role: Role):
        if role not in self.roles:
            self.roles.append(role)

    def revoke_role(self, role: Role):
        if self.has_role(role):
            self.roles.remove(role)

    def has_role(self, role: Role):
        return role in self.roles

    def can_perform(self, action: Action, role_validation: RoleValidation):
        for r in self.roles:
            role_actions = role_validation.get_actions_of_role(r)
            return action in role_actions


def main():
    pass


if __name__ == '__main__':
    main()
