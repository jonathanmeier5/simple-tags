import click

from simple_tagger import WebpageBinaryTrainingSet

from .workflow import Workflow


@click.group()
def entrypoint():
    """
    Workflow entrypoint to for CLI
    """
    import os
    print(os.listdir())
    pass


@entrypoint.command()
@click.argument('classification_method')
@click.option('--file', help='filepath to training set csv')
def webpage(classification_method, **kwargs):
    click.echo('booo')
    click.echo([classification_method, kwargs])

    filename = kwargs.get('file')
    training_set = WebpageBinaryTrainingSet(filename=filename)

    callable_mapping = {
        'j': training_set.tag_positive,
        'k': training_set.tag_negative,
    }
    workflow = Workflow(
        training_set=training_set,
        callable_mapping=callable_mapping,
    )

    workflow.init_loop()

