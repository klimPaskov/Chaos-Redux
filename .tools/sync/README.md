# Agent synchronizers

This directory contains the maintained one-way generators that project canonical `.codex/agents/*.toml` definitions into the Qoder and Cursor runtime formats.

Run both generators after changing a Codex subagent definition:

```powershell
python .tools/sync/sync_qoder_agents.py
python .tools/sync/sync_cursor_agents.py
```

The Codex TOML files remain authoritative. Never hand-edit generated Qoder or Cursor agent definitions.
