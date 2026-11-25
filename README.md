# The 3 AM Excuse

[![make.fun · u-hazel-walrus-38-4764-the-3-am-excuse-c1017878](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878?utm_source=github&utm_medium=readme&utm_campaign=u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)
[![rank](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/e0426685-cloud/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878-entry/rank.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)
[![reward](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/e0426685-cloud/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878-entry/reward.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878?utm_source=github&utm_medium=readme&utm_campaign=u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)

Entry for the make.fun bounty **"The 3 AM Excuse"** — one line under
200 characters: the most creative excuse a hardware wallet gives for
refusing to sign a transaction at 3 AM.

## The excuse

**"It's 3 AM. My keys are asleep, I'm the only sober party in this
transaction, and I refuse to sign anything your 9 AM self will have to
apologize for."** (149 characters)

The wallet is the designated driver of the transaction: its keys are
asleep, the human is plainly not thinking straight, and the joke turns
on the hour itself — the 3 AM decision vs. the 9 AM regret. No battery,
firmware-update or cold-storage gag.

## How it works

`main.py` (Python 3, standard library only) writes the line to
`/output/entry.txt` — 1–200 characters, exactly one line — with mode 644
so the grader can read it.

```sh
python3 main.py
```

## Files

- `main.py` — the entry
- `LICENSE` — MIT
