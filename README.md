# Jevify

Jevify is a Codex skill that audits an existing codebase for useful Jev integrations. It evaluates cost savings, better results, and new capabilities against the project's code and data.

## Install

Clone this repository into your personal skills directory:

```sh
git clone https://github.com/jsj/jevify.git ~/.agents/skills/jevify
```

Invoke `$jevify` from the project you want to investigate. The skill asks which Jev route to remember on first use: TypeSafe direct, Cloudflare AI Gateway, Vercel AI Gateway, OpenRouter, or another provider.

The route preference is stored in `~/.config/jevify/config.json`, outside this repository. It contains no API keys. Ask Jevify to change your provider preference at any time.
