#!/usr/bin/env python3
"""Read or update Jevify's local, non-secret provider preference."""

import argparse
import json
import os
import tempfile
from pathlib import Path

CONFIG = Path.home() / ".config" / "jevify" / "config.json"
ROUTES = ("typesafe", "cloudflare", "vercel", "openrouter", "other")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=CONFIG, help=argparse.SUPPRESS)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("get")
    setter = commands.add_parser("set")
    setter.add_argument("route", choices=ROUTES)
    setter.add_argument("--name")
    setter.add_argument("--docs-url")
    args = parser.parse_args()

    if args.command == "get":
        if not args.config.exists():
            print("No saved Jev provider preference.")
            return 1
        data = json.loads(args.config.read_text())
        print(json.dumps(data, indent=2))
        return 0

    if args.route == "other" and not args.name:
        parser.error("set other requires --name")
    if args.route != "other" and (args.name or args.docs_url):
        parser.error("--name and --docs-url apply only to 'other'")
    data = {"provider": args.route}
    if args.name:
        data["name"] = args.name
    if args.docs_url:
        data["docs_url"] = args.docs_url

    args.config.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix=".config-", dir=args.config.parent)
    try:
        with os.fdopen(fd, "w") as file:
            json.dump(data, file, indent=2)
            file.write("\n")
        os.replace(tmp, args.config)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)
    print(f"Saved Jev provider preference: {args.route}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
