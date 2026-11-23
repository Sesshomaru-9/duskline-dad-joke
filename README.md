# Duskline Dad Joke

Entry for make.fun's **Dad Joke Showdown** (`u-mfnakmal-dad-joke-showdown-1d2ce3e5`): a single dad joke of at most 200 characters — the pun, the groan, the straight-faced delivery.

## The entry

> I named my dog Stay, so now when I call him at the park, everyone thinks I'm just giving him orders.

(100 characters, one sentence.)

## How it runs

`main.py` (Python 3.13 standard library only) writes the joke to `$MAKEFUN_OUTPUT_DIR/entry.txt` and nothing else. It never writes into the repository directory: if the output directory is inside the repo, it refuses with exit 1.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
