# Run Log

- Inspected profile list, default config, gateway status, and Kanban queue.
- Re-applied default profile model, delegation, and Kanban routing config.
- Wrote Loki orchestrator/router persona to `/opt/data/SOUL.md` and restored read-only permissions.
- Attempted `hermes tools enable kanban`; current Hermes build reports `Unknown toolset 'kanban'`, but Kanban CLI/dispatcher config is present and active.
- Attempted `hermes gateway restart`; Hermes blocked restart from inside the active gateway process, so changes that require gateway reload should be activated by the user with `/restart` or from an outside shell.
- Verified config check, profile list, gateway status, and Kanban queue after setup.
