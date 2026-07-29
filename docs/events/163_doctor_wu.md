# Event 163: Doctor Wu

## Overview

Event 163 is a fire-once host event and a narrow cross-event clinical API. The shared random-event dispatcher performs one weighted country scan immediately before firing. It favors countries already facing severe disease pressure, countries with field-hospital technology, and countries with enough industry to support a traveling clinical network.

The chosen country can grant Doctor Wu a public mandate, place the network under protected clinical authority, or refuse him. Acceptance creates exactly one persistent global host. Refusal resolves the event without manufacturing a replacement.

## Runtime contract

- `doctor_wu_active` is the global active-state flag.
- `doctor_wu_current_host` is both the host country flag and the persistent global event target.
- `doctor_wu_is_current_host` and `doctor_wu_has_current_host` are the public validation triggers.
- `doctor_wu_initialize_host`, `doctor_wu_transfer_host_atomically`, and `doctor_wu_clear_active_host` own lifecycle mutation and cleanup.
- Host selection is a single explicit fire-once scan, never a daily, weekly, or monthly world iteration.

Event 20 consumes this API. A committed host receives the Black Plague response hook, but Doctor Wu does not grant progress merely by arriving and does not bypass the selected-state, phase, material, time, or response-capacity requirements of Doctor Wu's Protocol.

## Event log and dispatcher

Event 163 is registered as a fire-once event. Its opening history entry uses the weighted host as the actor. The event-detail text documents its host contract and Black Plague limits. Because Event 163 is a sparse high id, the shared weight and cap arrays are sized from the highest registered event id plus one rather than from the number of registered events.

## Visual assets

The core-stabilization package uses the final Black Plague report image and its registered sprite for Doctor Wu's report events. This keeps the live event consumer resolved without introducing a placeholder or an unregistered sprite. A unique period clinical still life or documentary ward scene remains a later content asset; it must not use a generated real-person likeness.

## Future extensions

- Additional disease events may consume the same validated host API.
- A later Event 163 source specification may add transfers or departure conditions without changing the public host identifiers.
- Any transfer route must validate the recipient before clearing the old host and must notify active disease systems after the new host is committed.
