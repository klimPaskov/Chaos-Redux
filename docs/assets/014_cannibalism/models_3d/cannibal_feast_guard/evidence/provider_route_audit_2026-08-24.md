# Meshy route ownership audit — 2026-08-24

Before the accepted rig retry, 11 exact locked `@meshy-ai/meshy-mcp-server` route instances were audited by process ID, command line, creation time, parent process, and live-agent ownership. They predated this worker turn and had no live provider task owner. Only those verified orphans were terminated; the exact route count was then zero.

The official repository wrapper subsequently created a one-shot route for balance and provider operations. Its completed route triplet was verified and terminated after use:

- command wrapper PID `21880`, created `12:25:39`
- PowerShell wrapper PID `9796`, created `12:25:39`
- locked Node server PID `21656`, created `12:25:40`

At `12:33:06–12:33:09`, 11 new exact locked routes appeared while multiple repository agents were live. Their process command lines were identical and exposed no job or provider-task identifier, so ownership could not be attributed safely. A twelfth route appeared at `12:39:04` as another repository agent became active. No `docs/assets/**/history.jsonl` file was modified after the route wave, so no recorded provider task owns any of these routes. One live GUI auditor also explicitly confirmed that it did not use or need Meshy. The pattern is consistent with agent transport startup, but the individual processes still could not be mapped safely to named live agents. They were treated as ambiguous and were not terminated. The paid recovery call remained paused while the route count was nonzero.

This audit does not classify non-route processes and did not terminate any ambiguous or non-route process.
