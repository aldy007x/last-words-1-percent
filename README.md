# Famous Last Words at 1 Percent

[![Make.fun](https://make.fun/badge/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4.svg)](https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4)
[![Rank](https://make.fun/badge/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4/aldy007x/last-words-1-percent/rank.svg)](https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4)
[![Reward](https://make.fun/badge/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4/aldy007x/last-words-1-percent/reward.svg)](https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4)

Entry for the [make.fun bounty "Famous Last Words at 1 Percent"](https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4): the funniest one-line farewell a phone could say as its battery hits 1 percent.

## The entry

> At 1%, I confess: I was never really at 100%. I just rounded up so you'd feel proud of me.

(90 characters — within the 199-character gate.)

## How it works

`main.py` (Python standard library only, no network, deterministic) writes the single line above to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `./output/entry.txt`) and self-checks the competition gate before exiting: UTF-8 text, 1–199 characters, not only white space, a single line — then verifies the written file round-trips through the same gate.

```sh
python3 main.py
cat output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
