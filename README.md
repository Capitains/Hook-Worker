Hook-Worker
====

Lightweight API to deploy on the machine distributing the test on a redis connection


- [Deployment](deployment.md)

# Commands

`hookworker-api [-h] [-p PORT] [-d DOMAIN] [-g DEBUG] [-s SECRET] [-n] [-o PATH] [-e LEVEL] [-r REDIS] [-w]`

| Parameter / Syntax   | Description                                         | Concerns |
| -------------------- | --------------------------------------------------- | -------- |
| -p PORT, --port      | PORT  Port to use to run the API                    | Redis    |
| -d DOMAIN, --domain  | DOMAIN Host for the API                             | API      |
| -g DEBUG, --debug    | DEBUG Debug mode for the API                        | API      |
| -s SECRET, --secret  | SECRET Secret used to secure data exchanges in Hook | API      |
| -o PATH, --path      | PATH  Path to use for storing logs                  | API      |
| -e LEVEL, --level    | LEVEL Level of logging                              | API      |
| -r REDIS, --redis    | REDIS Redis address                                 | Redis    |
| -w WORKER, --worker  | Number of worker to use for HookTest                | API      |
| -g GIT, --git        | Path where you would like to do the cloning         | API      |
| -h, --help           | show this help message and exit                     |          |
| -q, --rq             |  Run the worker                                     | Redis    |
| -a, --api            |  Run the api                                        | API      |