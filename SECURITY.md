# Security Policy

## Reporting a Vulnerability

Please do NOT report security issues via public GitHub Issues.

Email security reports to: security@makwanaalpesh811-a11y.invalid

## Credential Policy

- **No credentials are committed** to any repository.
- All skills read credentials from local filesystem paths like `~/.<name>_env` or `~/.<name>_token.json`.
- All API keys referenced in documentation are examples or placeholders (`your_key_here`, `TEST_API_KEY`).

## Dangerous Command Review

- Official installers (e.g., `curl | bash`) are documented with source URLs.
- `rm -rf` commands only reference specific project directories.
- `chmod` is never used with 777.
- No `eval` of untrusted input.

## Safe by Design

- Delta Exchange MCP is in **read-only** mode.
- Signal bots are **paper-trade only** (no live orders).
- Trading agent requires explicit approval for live execution.
- All external API calls require real credentials the user provides.

## License

MIT — see LICENSE file.
