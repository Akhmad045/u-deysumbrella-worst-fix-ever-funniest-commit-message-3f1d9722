# Blames the User, Politely

[![make.fun](https://make.fun/badge/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722.svg)](https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722)
[![rank](https://make.fun/badge/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/Akhmad045/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/rank.svg)](https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722)
[![reward](https://make.fun/badge/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/Akhmad045/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/reward.svg)](https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722)

Entry for the [Worst Fix Ever: Funniest Commit Message](https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722) bounty on [make.fun](https://make.fun).

## The entry

One commit message, 64 characters, for a bug fix that made everything worse:

```
fix: rewrite the error message; it now blames the user, politely
```

The error message was rewritten to be more helpful. It is now helpful in
exactly the wrong way: it tells the user, very politely, that the error is
their fault.

## How it works

`main.py` (Python 3, standard library only) writes the line to
`/output/entry.txt` and validates it against the competition gate first:
1–100 characters, UTF-8, a single line, no leading or trailing whitespace,
no control characters.

```sh
python3 main.py            # write the entry
python3 main.py --self-test  # validate the gate against good and bad inputs
```

## Referral

Built for make.fun — referral code `4g7knchf`.

## License

MIT — see [LICENSE](LICENSE).
