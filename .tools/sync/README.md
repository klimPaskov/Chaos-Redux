# Agent synchronizers

This directory contains the maintained one-way generators that project canonical `.codex/agents/*.toml` definitions into the Qoder, Cursor, and opencode runtime formats.

The available generator commands are:

```powershell
python .tools/sync/sync_qoder_agents.py
python .tools/sync/sync_cursor_agents.py
python .tools/sync/sync_opencode_agents.py
```

The Codex TOML files remain authoritative. Never hand-edit generated Qoder, Cursor, or opencode agent definitions.

Before running a generator, check the active runtime's destination-write rules in [AGENTS.md](../../AGENTS.md).
A listed command does not authorize writing another runtime's files.
If the synchronization requirement conflicts with a rule to leave the destination untouched, preserve both requirements, record blocked synchronization, and request a specific ownership decision through the handoff.
Keep canonical instruction changes and unresolved generated-file consistency visible in the same handoff.
