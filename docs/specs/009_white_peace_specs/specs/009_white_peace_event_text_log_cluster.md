# Event 009 — Event Text, Details, Cluster, and Localisation Handoff

## Key naming direction

Recommended script namespace stays with the existing event pattern:

- entry event: `chaosx.nr9.1`
- base report variant: `chaosx.nr9.1`
- multi-settlement variant: `chaosx.nr9.2`
- major-country settlement variant: `chaosx.nr9.3`
- broad settlement variant: `chaosx.nr9.4`
- hidden runtime/cleanup events may use later IDs only if needed.

If the existing repo has a different file naming pattern for Event 009, preserve the existing file and IDs.

## Suggested localisation keys

Use the existing Chaos Redux localisation file split. The implementation agent should map these names to the actual repo pattern.

| Key | Direction |
| --- | --- |
| `chaosx_event_name_9` | `White Peace` |
| `chaosx_event_debug_name_9` | `Event 009 — White Peace` |
| `chaosx.nr9.1.t` | `A Note Without Demands` |
| `chaosx.nr9.1.d` | Base single-pair description with `[white_peace_primary.GetName]` and `[white_peace_partner.GetName]` if safe. |
| `chaosx.nr9.1.a` | `Let the guns fall silent.` |
| `chaosx.nr9.2.t` | `Tables in Several Rooms` |
| `chaosx.nr9.2.d` | Multi-pair description, with pair count if supported. |
| `chaosx.nr9.2.a` | `No one claims victory.` |
| `chaosx.nr9.3.t` | `A Major Power Steps Back` |
| `chaosx.nr9.3.d` | Major-country settlement description. |
| `chaosx.nr9.3.a` | `The order has already been given.` |
| `chaosx.nr9.4.t` | `The Armistice Circular` |
| `chaosx.nr9.4.d` | Broad-settlement description. |
| `chaosx.nr9.4.a` | `The line goes quiet.` |

## Base event text draft

### `chaosx.nr9.1.t`

A Note Without Demands

### `chaosx.nr9.1.d`

A neutral channel has delivered the same paper to both governments. It names no victor, no indemnity, and no border to be redrawn. The soldiers are ordered to stop where they stand, under the same flags and in the same towns that began the matter.

The war between [?white_peace_primary.GetName] and [?white_peace_partner.GetName] ends without spoils.

### `chaosx.nr9.1.a`

Let the guns fall silent.

Implementation note: Replace the exact country-name syntax with the existing event-target localisation pattern. If saved event targets cannot be used safely in the displayed event, use ordinary scope names from the event recipient and target.

## Multi-settlement text draft

### `chaosx.nr9.2.t`

Tables in Several Rooms

### `chaosx.nr9.2.d`

The first note was copied, then copied again. Several minor governments receive the same thin formula: no claims, no reparations, no procession, no speech from a balcony. Staff officers fold maps they had not been allowed to win.

Across several fronts, the fighting stops without a declared victor.

### `chaosx.nr9.2.a`

No one claims victory.

## Major-country settlement text draft

### `chaosx.nr9.3.t`

A Major Power Steps Back

### `chaosx.nr9.3.d`

A major government signs away one part of its war without ceremony. Diplomats call it prudence. Officers call it an order. Along the border, the men who expected victory or ruin receive neither.

The settlement grants no spoils and demands no surrender.

### `chaosx.nr9.3.a`

The order has already been given.

## Broad-settlement text draft

### `chaosx.nr9.4.t`

The Armistice Circular

### `chaosx.nr9.4.d`

A diplomatic circular moves through several capitals, carrying the same exhausted formula from front to front. Not friendship. Not surrender. Not forgiveness. Just enough ink to make rifles lower and artillery crews wait for orders that never come.

The world is not calm, but several wars have gone quiet.

### `chaosx.nr9.4.a`

The line goes quiet.

## Event detail window text

### Short detail

White Peace searches for safe wars that can end without conquest, indemnity, or scripted-story damage. At first it settles one minor-country pair. Later evolutions can settle several minor pairs, rarely include a major country, or issue broader settlements when the world has too many wars. Its selection weight rises with active wars and valid minor-war candidates, but repeatable decay and higher-stage penalties keep it from becoming common.

### Long detail direction

The event is a cleanup valve for war clutter. It should list these player-facing facts:

- it needs at least one active war;
- it also needs at least one safe candidate pair;
- it favors minor-versus-minor settlements;
- it avoids protected scripted wars;
- it has no decline option;
- it uses dynamic weight below ordinary event prominence most of the time;
- it grows more likely as war clutter grows;
- it becomes less likely as its evolved branches become stronger.

Do not show the exact safety trigger list unless the event-detail UI already has a compact custom tooltip pattern for it.

## Evolution display text

| Evolution | Title direction | Detail direction |
| --- | --- | --- |
| Stage I | `Repeated Minor Settlements` | White Peace can resolve several safe minor-country pairs from one firing. |
| Stage II | `Major-Country Settlement` | A rare branch can involve a major country when the war segment is safe. |
| Stage III | `Broad Diplomatic Settlement` | When active wars are excessive, one firing can quiet several safe conflicts or a larger safe segment. |

Evolution history rows should use the existing event-evolution logging pattern with Event ID `9`, evolution stage, tier, and actor only when the current milestone belongs to a country. These stages are global; they normally do not need a country actor.

## History row direction

Preferred history formats:

- `White Peace: [Primary] and [Partner] ended their war without spoils.`
- `White Peace: [Primary] signed a no-gain settlement.`
- `White Peace: several minor fronts went quiet.`
- `White Peace: a major power stepped back from one war.`

If the existing history row only supports one actor, use the primary actor and keep partner details in the event popup or selected history detail.

## Peace cluster detail direction

Cluster ID `4`, cluster name `Peace`.

Cluster description direction:

> Peace events reduce conflict through settlements, ceasefires, exhaustion, negotiations, and other de-escalation incidents. White Peace is the low-impact member: it looks for safe wars that can end without territorial gain.

White Peace member row:

- event ID: `9`;
- role: low-impact member;
- danger/severity display: low;
- availability reason: valid safe settlement candidate exists;
- skip reasons: no active wars, no safe candidates, protected conflicts only, major branch not unlocked, recent settlement memory.

## Dynamic tooltip directions

Use scripted localisation for a compact status line:

| State | Text direction |
| --- | --- |
| Available, low pressure | `Safe settlement candidate found. Current war pressure is low.` |
| Available, high pressure | `Several safe settlement candidates found. War pressure is high.` |
| Unavailable, no wars | `No active wars.` |
| Unavailable, unsafe wars | `Active wars exist, but none are safe for White Peace.` |
| Stage II major candidate | `A major-country settlement candidate exists, but the branch remains rare.` |
| Stage III broad candidate | `A broad settlement candidate exists, but protected wars are still excluded.` |

## Localisation audit requirements

Before the implementation is called complete, run a localisation audit for:

- missing keys in event names, event texts, details, cluster detail, and evolution detail;
- broken actor/partner dynamic localisation;
- raw trigger exposure in event list or cluster skip reasons;
- mismatch between event detail text and catalog detail;
- update-history wording;
- duplicate keys;
- UTF-8 BOM preservation in edited localisation files.

## Spreadsheet/catalog alignment direction

After implementation, the event catalog row for Event ID `9` should use player-facing wording equivalent to:

**Details:** White Peace looks for safe wars that can end without conquest or scripted-story damage. The base version settles one minor-country pair. Its selection weight rises when many active wars and valid minor-war candidates exist, but repeatable recovery, firing decay, and evolution penalties keep it rare.

**Evolution detail:** Repeated Minor Settlements can settle several minor pairs from one firing. Major-Country Settlement rarely involves a major country. Broad Diplomatic Settlement can quiet several safe conflicts or a larger safe war segment when the world has too many wars.

The spreadsheet worker should mirror final in-game localisation rather than this draft if implementation wording changes.
