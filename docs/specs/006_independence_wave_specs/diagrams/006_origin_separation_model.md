# Origin separation model

```mermaid
flowchart TD
    A[Tag is requested by a release system] --> B{Does the tag already exist?}
    B -- Yes --> C[Do not overwrite origin, focus tree, or mechanics]
    C --> D[Skip, reroll, or apply only a designed reaction package]
    B -- No --> E{Which event or action creates it?}
    E -- Event 6 --> F[Set Independence Wave origin]
    E -- Event 5 --> G[Set Soviet Collapse origin]
    E -- Other source --> H[Set that source's origin or ordinary state]
    F --> I[Load Event 6 values, ideas, decisions, focus framework or overlay, AI, league and formables]
    G --> J[Load Event 5 content only]
    H --> K[Load ordinary or source-specific content]
    I --> L{Country later ceases to exist?}
    J --> L
    K --> L
    L -- Yes --> M[End active origin package, retain historical event log]
    M --> N{Country is released again?}
    N -- Yes --> E
```

## Cluster collision rule

When Events 5 and 6 are in one Liberations cluster firing, both plans reserve tags and anchors before execution. One tag receives one origin. The losing plan selects another candidate.
