# Lutugino

This is an experiment, and is probably not useful to you.

It's intended to handle a very specific data transformation that arises when using [container-transform][container-transform].

AWS ECS task definitions don't support docker-compose's env_file option, but environment files are nice to keep separate from docker-compose files. Lutugino parses an env file into ECS-compatible json, that we can then patch into a task definition document using a tool like [jq][jq].

Installation:

```
pip install git+https://github.com/cmac1000/lutugino.git#egg=lutugino
```

Example usage:
```
PATH_TO_ENV_FILTER = "./env.filter"

echo "(.containerDefinitions[] | select(.name == \"app\") | .environment) |= " \
  > $PATH_TO_ENV_FILTER

lutugino --env_file=staging.env >> $PATH_TO_ENV_FILTER

cat docker-compose.yml | container-transform \
                       | jq --file $PATH_TO_ENV_FILTER \
                       > task_def.json
```

[container-transform]: https://github.com/micahhausler/container-transform  "container-transform"
[jq]: https://stedolan.github.io/jq/                                        "jq"
