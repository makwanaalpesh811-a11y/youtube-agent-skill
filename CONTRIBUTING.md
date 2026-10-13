# Contributing

## Adding a Skill

1. Create a new folder under `skills/<skill-name>/`
2. Add `SKILL.md` with YAML frontmatter:
   ```yaml
   ---
   name: skill-name
   description: "One-line description"
   version: 1.0.0
   author: Your Name
   license: MIT
   platforms: [linux, macos, windows]
   ---
   ```
3. Add executable scripts in `scripts/` folder.
4. Add references in `references/` folder.
5. Add examples in `examples/` folder.
6. Add tests in `tests/` folder.

## Required Sections in SKILL.md

- **When to use** — triggers and conditions
- **Prerequisites** — dependencies, environment
- **Usage** — how to run
- **Examples** — input/output samples
- **Troubleshooting** — common errors
- **Limitations** — what it doesn't do
- **Safety** — what it won't touch

## Local Testing

```bash
python3 -m py_compile $(find . -name '*.py')
```

## License

MIT — see LICENSE.
