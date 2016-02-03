import json

import click

filters = [
    lambda line: '=' in line  # we only care about lines that set variable with '='
]


def _get_lines(filename):
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
    return lines


@click.command()
@click.option('--env_file', prompt='path to env file', help='path to env file')
def cli(env_file):
    # environment file goes in
    lines = _get_lines(env_file)
    filtered = filter(lambda line: all(filter_func(line) for filter_func in filters), lines)
    split = [line.split('=') for line in filtered]
    env_dict = [{'name': pair[0], 'value': pair[1]} for pair in split]
    json_string = json.dumps(env_dict)
    # jq-compatible filter goes to stdout
    print('.environment=' + json_string)

if __name__ == '__main__':
    cli()
