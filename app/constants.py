from enum import Enum, unique


@unique
class TaskStatus(Enum):
    running = 1
    completed = 2
