'''Command line interface to Legofy'''
import click
import legofy


@click.command()
@click.argument('image', required=True, type=click.Path(dir_okay=False, exists=True, resolve_path=True))
@click.argument('output', default=None, required=False, type=click.Path(resolve_path=True))
@click.option('--scale', default=30, type=int, required=False)
@click.option('--bricks', default=None, required=False, type=int)
@click.option('--brick', default=None, required=False, type=click.Path(dir_okay=False, exists=True, resolve_path=True))
def main(image, output, bricks, brick, scale):
    '''Main entry point'''
    if output:
        if bricks:
            if brick:
                legofy.main(image, scale, output=output, bricks=bricks, brick_path=brick)
            else:
                legofy.main(image, scale, output=output, bricks=bricks)
        elif brick:
            legofy.main(image, scale, output=output, brick_path=brick)
        else:
            legofy.main(image, scale, output=output)
    elif bricks:
        if brick:
            legofy.main(image, scale, bricks=bricks, brick_path=brick)
        else:
            legofy.main(image, scale, bricks=bricks)
    elif brick:
        legofy.main(image, scale, brick_path=brick)
    else:
        legofy.main(imagescale, )


if __name__ == '__main__':
    main()
