# CLI tool that automates my dev workflow

CLI tool (using `click`) that automates my dev workflow:
- `init` command: scaffolds a new Python project (creates folders, virtualenv, .gitignore, pyproject.toml)
- `check` command: runs linter + type checker + tests in sequence
- `release` command: bumps version, creates a git tag, generates a changelog from commit messages
- Host it on GitHub with a proper README
- Practice the full Git workflow: branches, PRs (even to my own repo), meaningful commits