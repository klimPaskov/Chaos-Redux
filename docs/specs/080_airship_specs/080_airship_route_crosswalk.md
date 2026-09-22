# Event 080: Legacy route crosswalk

## What this records

This table transcribes the inspected `is_in_airship_region` branches in `common/scripted_triggers/080_airship_triggers.txt` at repository ref `879b3007d3b6bf75c726c11635473fccda45c569`. It preserves their exact numeric region ordering by route index. It is a planning evidence appendix, not a replacement route.

These are strategic-region predicates, not exact state IDs, city names, coordinates, or original stop markers. A blank predicate means the legacy branch returns `always = no`. It does not by itself prove that the artwork is over water. Every row still needs exact geographic and original-stop verification against the authoritative map.

Departure is index 0. Indices 1 through 121 are the requested 121 progression transitions. The uninterrupted day column is derived as twice the index and is a timing target for the rework. It is not the old script's one-day schedule.

## Preserved sequence

| Route index | Uninterrupted day | Inspected region predicates | Binding status |
|---|---:|---|---|
| 0 | 0 | 117, 214, 211 | Departure anchor, exact state unverified |
| 1 | 2 | 170 | Exact state and original stop status unverified |
| 2 | 4 | 53 | Exact state and original stop status unverified |
| 3 | 6 | 124 | Exact state and original stop status unverified |
| 4 | 8 | 124, 163 | Exact state and original stop status unverified |
| 5 | 10 | 163, 125 | Exact state and original stop status unverified |
| 6 | 12 | 125 | Exact state and original stop status unverified |
| 7 | 14 | 125 | Exact state and original stop status unverified |
| 8 | 16 | 35 | Exact state and original stop status unverified |
| 9 | 18 | 35 | Exact state and original stop status unverified |
| 10 | 20 | 35 | Exact state and original stop status unverified |
| 11 | 22 | 201 | Exact state and original stop status unverified |
| 12 | 24 | 201 | Exact state and original stop status unverified |
| 13 | 26 | 34, 107 | Exact state and original stop status unverified |
| 14 | 28 | 205, 34 | Exact state and original stop status unverified |
| 15 | 30 | 123 | Exact state and original stop status unverified |
| 16 | 32 | 204 | Exact state and original stop status unverified |
| 17 | 34 | 219 | Exact state and original stop status unverified |
| 18 | 36 | 120 | Exact state and original stop status unverified |
| 19 | 38 | 234 | Exact state and original stop status unverified |
| 20 | 40 | 234 | Exact state and original stop status unverified |
| 21 | 42 | 233 | Exact state and original stop status unverified |
| 22 | 44 | 233 | Exact state and original stop status unverified |
| 23 | 46 | 220 | Exact state and original stop status unverified |
| 24 | 48 | 36 | Exact state and original stop status unverified |
| 25 | 50 | 36 | Exact state and original stop status unverified |
| 26 | 52 | None | No legacy land predicate, geography unverified |
| 27 | 54 | 161 | Exact state and original stop status unverified |
| 28 | 56 | 161, 45 | Exact state and original stop status unverified |
| 29 | 58 | 16, 3 | Exact state and original stop status unverified |
| 30 | 60 | 2, 1, 4 | Exact state and original stop status unverified |
| 31 | 62 | 19, 5, 7, 21, 20 | Exact state and original stop status unverified |
| 32 | 64 | 23, 24 | Exact state and original stop status unverified |
| 33 | 66 | 22, 8 | Exact state and original stop status unverified |
| 34 | 68 | 275, 10 | Exact state and original stop status unverified |
| 35 | 70 | 11, 192 | Exact state and original stop status unverified |
| 36 | 72 | 276, 191 | Exact state and original stop status unverified |
| 37 | 74 | 277, 12 | Exact state and original stop status unverified |
| 38 | 76 | 265, 13, 278 | Exact state and original stop status unverified |
| 39 | 78 | 37, 132 | Exact state and original stop status unverified |
| 40 | 80 | 39 | Exact state and original stop status unverified |
| 41 | 82 | 26, 25, 202 | Exact state and original stop status unverified |
| 42 | 84 | 69 | Exact state and original stop status unverified |
| 43 | 86 | 232, 128 | Exact state and original stop status unverified |
| 44 | 88 | 236 | Exact state and original stop status unverified |
| 45 | 90 | 238 | Exact state and original stop status unverified |
| 46 | 92 | 196 | Exact state and original stop status unverified |
| 47 | 94 | 28, 129 | Exact state and original stop status unverified |
| 48 | 96 | 130 | Exact state and original stop status unverified |
| 49 | 98 | 133 | Exact state and original stop status unverified |
| 50 | 100 | 40 | Exact state and original stop status unverified |
| 51 | 102 | 14 | Exact state and original stop status unverified |
| 52 | 104 | 151 | Exact state and original stop status unverified |
| 53 | 106 | 262 | Exact state and original stop status unverified |
| 54 | 108 | 149 | Exact state and original stop status unverified |
| 55 | 110 | 256 | Exact state and original stop status unverified |
| 56 | 112 | 242 | Exact state and original stop status unverified |
| 57 | 114 | 243, 148 | Exact state and original stop status unverified |
| 58 | 116 | 186 | Exact state and original stop status unverified |
| 59 | 118 | 154 | Exact state and original stop status unverified |
| 60 | 120 | None | No legacy land predicate, geography unverified |
| 61 | 122 | None | No legacy land predicate, geography unverified |
| 62 | 124 | None | No legacy land predicate, geography unverified |
| 63 | 126 | None | No legacy land predicate, geography unverified |
| 64 | 128 | None | No legacy land predicate, geography unverified |
| 65 | 130 | None | No legacy land predicate, geography unverified |
| 66 | 132 | None | No legacy land predicate, geography unverified |
| 67 | 134 | None | No legacy land predicate, geography unverified |
| 68 | 136 | None | No legacy land predicate, geography unverified |
| 69 | 138 | 157 | Exact state and original stop status unverified |
| 70 | 140 | 157 | Exact state and original stop status unverified |
| 71 | 142 | None | No legacy land predicate, geography unverified |
| 72 | 144 | 194 | Exact state and original stop status unverified |
| 73 | 146 | 195 | Exact state and original stop status unverified |
| 74 | 148 | 193 | Exact state and original stop status unverified |
| 75 | 150 | 167 | Exact state and original stop status unverified |
| 76 | 152 | None | No legacy land predicate, geography unverified |
| 77 | 154 | 160 | Exact state and original stop status unverified |
| 78 | 156 | 160 | Exact state and original stop status unverified |
| 79 | 158 | 159 | Exact state and original stop status unverified |
| 80 | 160 | None | No legacy land predicate, geography unverified |
| 81 | 162 | 187 | Exact state and original stop status unverified |
| 82 | 164 | 188 | Exact state and original stop status unverified |
| 83 | 166 | 229, 142 | Exact state and original stop status unverified |
| 84 | 168 | 249 | Exact state and original stop status unverified |
| 85 | 170 | 165, 250 | Exact state and original stop status unverified |
| 86 | 172 | 146 | Exact state and original stop status unverified |
| 87 | 174 | 146, 153 | Exact state and original stop status unverified |
| 88 | 176 | 254, 190 | Exact state and original stop status unverified |
| 89 | 178 | 116 | Exact state and original stop status unverified |
| 90 | 180 | None | No legacy land predicate, geography unverified |
| 91 | 182 | 31 | Exact state and original stop status unverified |
| 92 | 184 | 230 | Exact state and original stop status unverified |
| 93 | 186 | None | No legacy land predicate, geography unverified |
| 94 | 188 | None | No legacy land predicate, geography unverified |
| 95 | 190 | None | No legacy land predicate, geography unverified |
| 96 | 192 | 181 | Exact state and original stop status unverified |
| 97 | 194 | 185 | Exact state and original stop status unverified |
| 98 | 196 | 139 | Exact state and original stop status unverified |
| 99 | 198 | 223 | Exact state and original stop status unverified |
| 100 | 200 | 223 | Exact state and original stop status unverified |
| 101 | 202 | 217 | Exact state and original stop status unverified |
| 102 | 204 | 274 | Exact state and original stop status unverified |
| 103 | 206 | 17, 273 | Exact state and original stop status unverified |
| 104 | 208 | 216 | Exact state and original stop status unverified |
| 105 | 210 | 183 | Exact state and original stop status unverified |
| 106 | 212 | 272 | Exact state and original stop status unverified |
| 107 | 214 | 184 | Exact state and original stop status unverified |
| 108 | 216 | None | No legacy land predicate, geography unverified |
| 109 | 218 | 140 | Exact state and original stop status unverified |
| 110 | 220 | 226 | Exact state and original stop status unverified |
| 111 | 222 | 182 | Exact state and original stop status unverified |
| 112 | 224 | 182 | Exact state and original stop status unverified |
| 113 | 226 | 210, 209, 41 | Exact state and original stop status unverified |
| 114 | 228 | 209 | Exact state and original stop status unverified |
| 115 | 230 | None | No legacy land predicate, geography unverified |
| 116 | 232 | None | No legacy land predicate, geography unverified |
| 117 | 234 | None | No legacy land predicate, geography unverified |
| 118 | 236 | None | No legacy land predicate, geography unverified |
| 119 | 238 | None | No legacy land predicate, geography unverified |
| 120 | 240 | None | No legacy land predicate, geography unverified |
| 121 | 242 | 117 | Return anchor, exact state and final visual unverified |

## Specific discrepancies to resolve

The movement effect's inspected index-1 branch matches region 170 but appends both 170 and 366 to its region array. The corresponding trigger row above contains only 170. Resolve this from the original route and actual game geography. Do not silently add 366 to this evidence table or assume that the extra entry is correct.

The old decision mission ends at index 120 despite the trigger containing a return branch at 121 with region 117. The corrected voyage must complete the final transition. The GFX search found `GFX_airship_trail_120`, but this session did not verify the availability or content of a final 121 sprite. Inspect the registry and actual files before choosing the final presentation strategy.

A bound implementation record should state the actual point, exact state or verified water location, original stop status, host-resolution method, qualified services, any allowed local diversion connection, and the source asset used to prove it. Preserve all 122 records including departure. Never fill a missing state by selecting an arbitrary state that happens to share the strategic region.
