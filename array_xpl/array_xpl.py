import click

@click.group()
def array_xpl():
    """
    Base command for array_xpl package
    """
    pass

@array_xpl.command()
@click.argument("view", type=click.Path(exists=True))
def view(file_path):
    """
    View the data in a .npy or .npz file
    """
    pass


@array_xpl.command()
@click.argument("plot", type=click.Path(exists=True))
def plot(file_path):
    """
    Plot the data in a .npy or .npz file
    """
    pass


@array_xpl.command()
@click.argument("metrics", type=click.Path(exists=True))
def metrics(file_path):
    """
    Calculate metrics on the data in a .npy or .npz file
    """
    pass
