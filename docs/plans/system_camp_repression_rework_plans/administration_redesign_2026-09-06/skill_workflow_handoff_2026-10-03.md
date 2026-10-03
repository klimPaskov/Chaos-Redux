# Skill workflow handoff

Disposition: implemented.
Acceptance basis: the parent explicitly requested narrow reusable guidance for production action contract tests and MCP client/server identity and task observation.
This handoff covers skill maintenance only and does not establish gameplay or MCP runtime completion.

## Changed files and exact additions

`.agents\skills\chaos-redux-decisions-missions\SKILL.md`, under `19. Balance review`, adds this subsection after the test-scenario reporting instruction:

```markdown
### Production action contract tests

When source contract tests cover a paid action, execute the real selector, action mapper, debit, refund, receipt, and cooldown helpers that belong to the tested path.
Restrict mocks to native primitives or explicitly out-of-scope consumers, and record those boundaries in the evidence.
Assert the actual native flag identifier, requested cooldown duration, and write count on success, rejection, refund, and repeated invocation where applicable; a mocked success counter does not prove that the production mapper has the required branch.
Do not replace a required production helper with a no-op solely to pass a loader error; fix the test loader or report the uncovered path.
These source tests do not establish native engine execution or timed expiry.
```

Existing guidance defined shared affordability, debit, refund, release receipts, and success-only cooldown behavior, but did not constrain test mocks or require assertions against the actual production mapper's native writes.
The added rule prevents a substitute mapper or success counter from hiding an absent production branch.

`.agents\skills\chaos-redux-subagents\SKILL.md`, under `MCP evidence in handoffs`, adds these sentences immediately after the connected-server capability verification paragraph:

```markdown
Resolve each client's actual configured transport and server process before attributing capabilities to a local checkout, global binary, or exposed tool list; their versions and supported routes can differ.
Keep configuration identity, server version, live schemas, and task negotiation in task evidence.
A failure to observe a native task result does not establish that the server task failed.
Preserve configuration, task IDs, and source/scenario hashes, then query existing handles through confirmed routes before retrying; if observation remains unavailable, report the task outcome unresolved.
Do not change external tool source or dependencies to mask startup or domain failures.
Keep package paths, concrete versions, and current errors in task evidence rather than reusable skill rules.
```

Existing guidance already required connected-server health, live schemas, client negotiation, opaque handle preservation, and final-result inspection.
It did not explicitly resolve the configured transport against competing local installations, distinguish failed result observation from server task failure, or require handle queries before retrying.
The added rule makes those recovery boundaries explicit and keeps external tooling mutations outside this gameplay validation workaround.

## Scope preservation and validation

Both skills were already modified before this task.
The existing fractional-quote and finite-registry receipt additions in the decisions skill and probability-schema revision in the subagents skill were preserved.
No skills were created, and other skills, AGENTS.md, gameplay files, tool source, dependencies, and configuration were left unchanged.
Neither addition changes subagent routing or ownership, so no AGENTS.md or agent-definition routing update is required.

Both updated skill folders passed the official `skill-creator` quick validator.
The decisions validator initially used Windows cp1252 and could not decode an existing UTF-8 character; rerunning it with `python -X utf8` passed without changing the validator or skill encoding.
Review confirmed the additions contain reusable rules without event identifiers, concrete package paths, versions, or current runtime errors.
No runtime task was executed or retried for this prose-only patch, and production contract tests were not rerun by this maintenance worker.

## Parent follow-up and limits

Changes are unstaged and uncommitted as requested.
The parent should review and include these additions with the owning completed plan while preserving other agents' work in the same files.
There are no skill-maintenance blockers or simplifications.
Gameplay behavior, native timed expiry, tool startup health, and the outcome of existing native tasks remain outside this handoff's evidence.
