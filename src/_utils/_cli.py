SECTION_ID_TO_NAME = {
    "4": "primitive_types",
    "5": "arrays",
    "6": "strings",
    "7": "linked_lists",
    "8": "stacks_queues",
    "9": "binary_trees",
}


def get_section(problem_id: str) -> str:
    # problem_id is in format SECTION_NUMBER
    return SECTION_ID_TO_NAME[problem_id.split("_")[0]]
