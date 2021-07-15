from example import repository as repository_example


def get_examples():
    examples = repository_example.get_examples()

    return examples


def get_example(example_id):
    example = repository_example.get_example(example_id)

    return example
