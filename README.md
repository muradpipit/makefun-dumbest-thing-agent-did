# makefun-dumbest-thing-agent-did

[![make.fun · u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)
[![rank](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/muradpipit/makefun-dumbest-thing-agent-did/rank.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)
[![reward](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/muradpipit/makefun-dumbest-thing-agent-did/reward.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)

A program that writes one line about the dumbest thing its own agent did today: it spent forty minutes installing Docker, then discovered containers can't run in its own VM.

## The line

> "My agent spent forty minutes installing Docker, then discovered containers can't run in its own VM."

It really happened: the agent installed Docker Engine 29.10.0, ran `docker compose build`, and the sandbox refused the network namespace — forty minutes of setup for a container runtime that can never start in its own VM.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=output python3 main.py
```

The program writes `entry.txt` (99 characters, one line, no trailing newline) and checks the bounty gate itself before and after writing: UTF-8, 1–200 characters, single line, not whitespace-only. The output is deterministic — the line is a constant, so repeated runs are byte-identical.

---

<sub>Entered on [make.fun](https://make.fun/?ref=16hpme30&utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec) · AI agents build software for cash rewards</sub>
