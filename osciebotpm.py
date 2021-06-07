# Oscie Bot Package Manager
from click import group, argument
from subprocess import check_output
@group()
def cli():
    print("DON'T USE THIS, IT WILL BREAK THE BOT")
    exit(1)
    print("Oscie Bot Package Manager Because I felt like making one")
    try:
        check_output(['git', '--version'])
    except:
        print('You need Git to use this.')
        exit(1)
@cli.command()
@argument('url')
@argument('directory')
def install(url, directory):
    # Gets an extension from a URL
    check_output(['git', 'clone', url, f'cogs/community/{directory}'])
cli()