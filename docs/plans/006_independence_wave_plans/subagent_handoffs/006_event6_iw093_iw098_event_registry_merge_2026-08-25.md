# Event 006 IW-093/IW-098 event registry merge

Date: 2026-08-25.

This source-layout merge moves the eight IW-093/IW-098 former-host negotiation events from `events/006_independence_wave_iw093_iw098.txt` into `events/006_independence_wave_support_events.txt`, which already owns the `chaosx.nr6` support-event namespace.

The removed parser file was 9,168 UTF-8 bytes, the receiver grew from 46,765 to 55,260 bytes, and the combined source tree saves 673 bytes while removing one parser file.

The moved event identifiers are `chaosx.nr006.9301`, `chaosx.nr006.9302`, `chaosx.nr006.9303`, `chaosx.nr006.9304`, `chaosx.nr006.9801`, `chaosx.nr006.9802`, `chaosx.nr006.9803`, and `chaosx.nr006.9804`.

The two file-scoped constants used by the moved bodies remain declared once at the receiver top: `CR_SC_INDEPENDENCE_WAVE_DECISION_GATE_DIPLOMATIC_ACCEPTANCE_OPINION = 25` and `CR_SC_INDEPENDENCE_WAVE_VALUE_MINIMUM = 0`.

Static comparison against the pre-merge `HEAD` blob reports `executable_body_equivalent=True`, and the Event 006 event-ID scan reports no duplicate IDs.

No event identifier, trigger, option, event target, localisation key, picture, namespace, package gate, admission row, or runtime callback was changed.

This is source-layout evidence only and makes no live parser, save/load, or in-game completion claim.
