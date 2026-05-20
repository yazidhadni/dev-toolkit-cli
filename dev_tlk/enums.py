from enum import Enum


class Version(str, Enum):
    MAJOR = "major"
    MINOR = "minor"
    PATCH = "patch"
