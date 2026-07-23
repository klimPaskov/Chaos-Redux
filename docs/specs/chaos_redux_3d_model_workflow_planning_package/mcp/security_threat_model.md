# MCP Security Threat Model

## Protected assets

- Meshy API key and account credits
- unpublished Chaos Redux source art and models
- repository source files
- local vanilla game files
- user Blender preferences and normal work
- machine filesystem and network access
- approved dependency archives and scripts

## Threats and controls

| Threat | Control | Detection |
| --- | --- | --- |
| API key printed or committed | Environment/secret store, redaction, repository secret scan | Config and log audit |
| Agent spends credits without approval | Job and budget gate | Credit ledger and task IDs |
| Provider URL expires before capture | Immediate local download | Artifact ledger requires local checksum |
| Blender MCP executes malicious code | Production allowlist, no arbitrary Python | Tool-schema test and operation log |
| Blender listener exposed to LAN | Loopback binding and firewall review | Environment verification |
| Extension supply-chain substitution | Version and SHA256 lock | Install-time hash check |
| Path traversal writes outside job | Canonical path confinement | Adapter rejects call and logs incident |
| Untrusted `.blend` executes handlers | Import GLB/FBX into clean scene, disable auto-run | Profile and startup verification |
| Model source silently changes | Protected source collection and checksums | Checkpoint comparison |
| Runtime asset wired to wrong consumer | Exact crosswalk and parent review | In-game validation |

## Trust levels

1. approved repository scripts and templates
2. approved local vanilla references, read-only
3. user-provided or sourced reference after preflight
4. provider outputs, untrusted until imported and audited
5. external Blender extensions, privileged and checksum-locked
6. unrestricted MCP tools, development-only and isolated

## Incident threshold

Any secret exposure, non-loopback listener, arbitrary production code execution, unapproved dependency change, or path escape is a blocking security incident. Stop the active pipeline and follow the incident response in `09_failure_recovery_cost_and_security.md`.
