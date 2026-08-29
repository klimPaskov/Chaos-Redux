# Agent synchronizers

This directory contains the maintained one-way generators that project canonical `.codex/agents/*.toml` definitions into the Qoder, Cursor, and opencode runtime formats.

Run all generators after changing a Codex subagent definition:

```powershell
python .tools/sync/sync_qoder_agents.py
python .tools/sync/sync_cursor_agents.py
python .tools/sync/sync_opencode_agents.py
```

The Codex TOML files remain authoritative. Never hand-edit generated Qoder, Cursor, or opencode agent definitions.
