# AGENTS.md

Scope: Entire repository

- Keep changes minimal and focused; avoid unrelated refactors.
- Use clear, descriptive filenames; prefer `snake_case` for Python.
- Do not add license headers unless requested.
- Do not introduce new dependencies without justification.
- Update README when changing user-facing behavior or commands.
- Prefer deterministic behavior where feasible; document randomness.
- Secrets live in `.env`; never hardcode API keys.
- Timezone defaults to `Europe/Paris` unless the user specifies otherwise.
- When generating files, write to the project root unless documented.

Coding style (Python):
- Python 3.10+
- Use standard library where possible
- Avoid one-letter variable names
- No inline code comments unless requested; keep code self-explanatory

Workflow:
- If adding features, propose a short plan first.
- Validate by running the script end-to-end when practical.
- Keep README concise with setup, config, and usage.