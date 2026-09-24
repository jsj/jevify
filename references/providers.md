# Jev inference routes

Read the entry for the chosen route. Read the linked documentation before you give request examples, prices, or limits. Do not put API keys in Jevify's preference file.

| Saved value | Start with | Integration distinction |
| --- | --- | --- |
| `typesafe` | [TypeSafe API](https://docs.typesafe.ai/api) | Native System One API and SDKs. |
| `cloudflare` | [Cloudflare Jev model](https://developers.cloudflare.com/ai/models/typesafe/jev/), [AI Gateway REST API](https://developers.cloudflare.com/ai-gateway/usage/rest-api/) | Use model `typesafe/jev` through `/ai/run`. Put `state` and `questions` in `input`. Read the project's gateway settings. If you must select a gateway, use `cf-aig-gateway-id`. |
| `vercel` | [Vercel Jev integration](https://vercel.com/changelog/ai-gateway-now-supports-typesafe-clients-and-http-api-for-jev), [model page](https://vercel.com/ai-gateway/models/jev) | Vercel documents AI SDK evaluation, a TypeSafe-compatible client, and an HTTP API. Read the request and answer shapes for the chosen method. |
| `openrouter` | [OpenRouter Jev guide](https://openrouter.ai/blog/tutorials/how-to-use-jev/), [model page](https://openrouter.ai/typesafe/jev-1.13/api) | Use the Decisions API for typed judgments. Read the current model ID and endpoint. |
| `other` | The saved documentation URL or the provider's official docs | Make sure that the route supports Jev's typed decision interface before you propose code. |
