# Awesome Jev [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of TypeSafe Jev resources, SDKs, gateways, agents, MCP servers, applications, benchmarks, examples, and independent System One implementations.

Jev returns typed probabilistic decisions for predefined questions. This list favors resources with a working canonical URL, public evidence, meaningful code or documentation, and a specific explanation of Jev's role.

**Last verified:** 2026-09-20 · **Resources:** 70 · **Categories:** 10

<!-- BEGIN GENERATED README RESOURCES -->
## Contents

- [Official Jev resources](#official-jev-resources)
- [SDKs and API clients](#sdks-and-api-clients)
- [Gateways and integrations](#gateways-and-integrations)
- [Agent tools and MCP servers](#agent-tools-and-mcp-servers)
- [Browser and computer-use agents](#browser-and-computer-use-agents)
- [Applications and developer tools](#applications-and-developer-tools)
- [Open System One implementations](#open-system-one-implementations)
- [Benchmarks and evaluations](#benchmarks-and-evaluations)
- [Examples and learning resources](#examples-and-learning-resources)
- [Community resources](#community-resources)

## Official Jev resources

- [Introducing System One Models and Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev) - TypeSafe's launch announcement for System One Models and Jev.
- [TypeSafe AI](https://typesafe.ai/) - Official home for TypeSafe AI, System One Models, and Jev.
- [TypeSafe System One API Reference](https://docs.typesafe.ai/api) - Official HTTP API reference for System One requests and responses.

## SDKs and API clients

- [jevclient](https://github.com/AboveColin/jevclient) - Independent asynchronous Python client for TypeSafe Jev with typed questions and probabilities.
- [System One Adapter for Python](https://github.com/typesafe-ai/system-one-adapter-python) - Official adapter for comparing System One decisions with LLM-backed implementations.
- [TypeSafe for Elixir](https://github.com/hfiguera/typesafe_ai) - Independent Elixir client for TypeSafe's System One API with typed answers and bounded concurrency.
- [TypeSafe JavaScript and TypeScript SDK](https://github.com/typesafe-ai/typesafe-sdk-js) - Official JavaScript and TypeScript client for the TypeSafe API.
- [TypeSafe Python SDK](https://github.com/typesafe-ai/typesafe-sdk-python) - Official synchronous and asynchronous Python client for TypeSafe.

## Gateways and integrations

- [Jev on Cloudflare Workers AI](https://developers.cloudflare.com/ai/models/typesafe/jev/) - Cloudflare Workers AI model documentation for TypeSafe Jev.
- [Jev on Netlify AI Gateway](https://docs.netlify.com/build/ai-gateway/overview/) - Netlify AI Gateway access for Jev from Netlify Functions.
- [Jev on Vercel AI Gateway](https://vercel.com/ai-gateway/models/jev) - Vercel AI Gateway model access for TypeSafe Jev.
- [LangChain.js TypeSafe integration](https://github.com/langchain-ai/langchainjs/tree/main/libs/providers/langchain-typesafe) - LangChain.js provider for calling TypeSafe System One models through typed classifiers.
- [Pydantic AI TypeSafeModel](https://pydantic.dev/docs/ai/models/typesafe/) - Pydantic AI adapter for running Jev inside typed agent workflows.
- [TypeSafe Jev on OpenRouter](https://openrouter.ai/typesafe) - OpenRouter model listings and API access for TypeSafe Jev.

## Agent tools and MCP servers

- [fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) - Claude Code plugin and library for Jev-directed transcript compaction.
- [Jev-cu](https://github.com/Sac-Y/Jev-cu) - Codex computer-use skill that delegates text-only action selection to Jev with local safety gates.
- [jev-guard](https://github.com/leepokai/jev-guard) - Security hook for coding-agent tools and permission checks.
- [jev-mcp by jkudish](https://github.com/jkudish/jev-mcp) - MCP server with Jev tools for verification, screening, ranking, and classification.
- [jev-router](https://github.com/gargpratyush/jev-router) - Per-turn model router for Claude Code and OpenAI Codex.
- [jevwire](https://github.com/Brainwires/jevwire) - Jev decision layer with an MCP server, library, and Claude Code plugin.
- [pi-jev](https://github.com/y0usaf/pi-jev) - Pi coding-agent extension that uses Jev for tool-call and output decisions.
- [TypeSafe Agent Skills](https://github.com/typesafe-ai/skills) - Official agent skills for building with the TypeSafe System One API.
- [typesafe-mcp](https://github.com/itsmostafa/typesafe-mcp) - Go MCP server and CLI for TypeSafe decisions in agent workflows.
- [VexJoy Agent](https://github.com/notque/vexjoy-agent) - Agent toolkit that uses Jev to route requests to specialist agents and gate context compaction.

## Browser and computer-use agents

- [Jev Browser](https://github.com/jkudish/jev-browser) - Headless browser agent and MCP client driven by Jev decisions.
- [Jev Browser Use](https://github.com/wy-coliney/jev-browser-use) - Codex browser skill that uses Jev for bounded navigation, clicks, toggles, and scrolling.
- [Jev Ultrafast](https://github.com/browser-use/jev-ultrafast) - Browser agent that uses Jev for fast operation and element selection.
- [Jev Voice Browser](https://github.com/moritzkremb/jev-voice-browser) - Voice-controlled Chromium demonstration using Playwright and Jev.
- [Mobile Jev](https://github.com/droidrun/mobile-jev) - Mobile agent for Mobilerun that uses Jev to choose actions on a real Android device.
- [TipTour](https://github.com/milind-soni/tiptour-macos) - macOS menu-bar computer-use app that lets Jev choose click targets from local controls.

## Applications and developer tools

- [Distill](https://github.com/samuelfaj/distill) - Terminal coding-agent harness with a Jev decision layer for routing and context selection.
- [Foreman](https://github.com/thruwire/foreman) - Software factory coordinator built around TypeSafe Jev decisions.
- [Jev Logs](https://jevlogs.com) - OpenTelemetry log exporter that classifies and routes records with Jev.
- [Jev Review](https://github.com/devagrawal09/jev-review) - Local code-review workflow that combines staged file judgments, severity scoring, and a review dashboard.
- [Jev Search](https://github.com/superagents-lab/jev-search) - Web search application with Jev query analysis, source selection, and reranking.
- [Jev Social](https://github.com/socai-io/jev-social) - Local-first social-media research demo with Jev routing and browser evidence.
- [jev-trader](https://github.com/jarrodwatts/jev-trader) - Monad trading bot that uses Jev to choose buy or sell actions from an order book.
- [jgrep](https://github.com/keltokhy/jgrep) - Semantic grep CLI that filters lines by meaning with TypeSafe Jev decisions.
- [pg-jev](https://github.com/realZachi/pg-jev) - PostgreSQL extension for semantic filtering, ranking, and classification with Jev.
- [quackd](https://github.com/rokbenko/quackd) - Robot-control CLI with an optional Jev stepper for choosing among predefined robot actions.
- [QuantDinger](https://github.com/OpenByteInc/QuantDinger) - AI trading platform with a Jev-backed pre-trade decision gate.
- [skillranker](https://github.com/Dicklesworthstone/skillranker) - Rust CLI that ranks agent skills against live session context.
- [sqlite-jev](https://github.com/mgaitan/sqlite-jev) - SQLite extension for batched natural-language judgments powered by TypeSafe Jev.
- [Stanley](https://github.com/devagrawal09/stanley-code) - Experimental coding agent for bounded implementation and review workflows.
- [Tax Document Classifier](https://github.com/kyotofin/tax-doc-classifier) - Tax-document page classifier built on typed Jev decisions.
- [TypeSafe Mario](https://github.com/fhshaik/typesafe-mario) - Experimental Super Mario Bros. controller driven by Jev choices over emulator telemetry.

## Open System One implementations

- [Jeff](https://github.com/logan-markewich/jeff) - Self-hosted Jev-compatible API replacement powered by the GLiFormer encoder.
- [Jevlike](https://github.com/vinnylarouge/jevlike) - Experimental model for selecting among dynamically supplied text options.
- [jevmlx](https://github.com/bnsd55/jevmlx) - Local typed-decision runtime for MLX models on Apple Silicon.
- [Kev](https://github.com/jaredpalmer/kev) - Small trainable Jev-like decision model based on Qwen2.5-0.5B.
- [LocalJev](https://github.com/githubnext/localjev) - Local Jev-compatible API server backed by DiffusionGemma.
- [NanoJev](https://github.com/TianyuCodings/NanoJev) - Small parallel decision model with a public training pipeline.
- [OpenJev](https://github.com/razorback16/openjev) - Open System One server with a Jev-compatible typed decision API.
- [openjev-sglang](https://github.com/ekzhang/openjev-sglang) - Jev-compatible API server backed by Qwen and SGLang.
- [SemIf](https://github.com/TheoLeeCJ/SemIf) - Independent typed probability system for open models on local hardware.
- [Simple Jev](https://github.com/featherless-ai/simple-jev) - Open classifier server that exposes supported models through typed decision endpoints.

## Benchmarks and evaluations

- [jev-agent-failure-benchmark](https://github.com/TokenTrim/jev-agent-failure-benchmark) - Agent-failure evaluation using 6,257 traces from the Who and When Pro dataset.
- [jev-benchmarks](https://github.com/AbdelStark/jev-benchmarks) - Reproducible classification and calibration evaluation for Jev and GLiNER2.5.
- [jev-rerank-bench](https://github.com/anessbelbati/jev-rerank-bench) - Search reranking comparison across Jev and dedicated rerankers.
- [TypeSafe Workflow Evals](https://evals.typesafe.ai/) - Official workflow evaluations for Jev decision tasks.

## Examples and learning resources

- [Jev Experiments](https://github.com/dabit3/jev-experiments) - Collection of latency-focused TypeSafe Jev demos with separate app documentation and tests.
- [Jev for Engineers](https://github.com/Foadsf/jev-for-engineers) - Minimal Jev examples for mechanical and electrical engineering scenarios.
- [TypeSafe Documentation and Cookbooks](https://docs.typesafe.ai/introduction/quickstart) - Official quickstarts, primitive guides, patterns, and Jev cookbooks.
- [TypeSafe Jev Examples](https://github.com/rajivkuriakose/typesafe-jev-examples) - Worked Jev examples for ticket triage and reranking.
- [TypeSafe Playground](https://github.com/TypeSafeAI/typesafe-playground) - Interactive playground for Jev patterns, workflows, agents, games, and code review.

## Community resources

- [Awesome Jev by TypeSafe](https://github.com/valentynkit/awesome-jev-typesafe) - Source-linked community directory for Jev projects, integrations, and articles.
- [Awesome Jev by yibie](https://github.com/yibie/awesome-jev) - Maintained community directory of Jev projects, integrations, and practical patterns.
- [Awesome TypeSafe](https://github.com/AbdelStark/awesome-typesafe) - Community directory of TypeSafe, System One, and Jev documentation and projects.
- [Jevify](https://github.com/altryne/jevify) - Agent skill for identifying Jev opportunities and planning decision experiments.
- [Learn Jev Tutorials](https://learnjev.com/tutorials) - Independent tutorials for Jev concepts, patterns, confidence, and reliability.
<!-- END GENERATED README RESOURCES -->

## Contributing

Contributions are welcome through pull requests. A submission must explain exactly how Jev is used and link to primary evidence.

This list is released under [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/).
