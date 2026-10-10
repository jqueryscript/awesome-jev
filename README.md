# Awesome Jev [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of TypeSafe Jev resources, SDKs, gateways, agents, MCP servers, applications, benchmarks, examples, independent System One implementations, and open-source Jev alternatives.

Jev returns typed probabilistic decisions for predefined questions.

**Last verified:** 2026-10-10 · **Resources:** 370 · **Categories:** 11

<!-- BEGIN GENERATED README RESOURCES -->
## Contents

- [Official Jev resources](#official-jev-resources)
- [SDKs and API clients](#sdks-and-api-clients)
- [Gateways and integrations](#gateways-and-integrations)
- [Agent tools and MCP servers](#agent-tools-and-mcp-servers)
- [Browser and computer-use agents](#browser-and-computer-use-agents)
- [Applications and developer tools](#applications-and-developer-tools)
- [Open System One implementations](#open-system-one-implementations)
- [Open-source Jev Alternatives](#open-source-jev-alternatives)
- [Benchmarks and evaluations](#benchmarks-and-evaluations)
- [Examples and learning resources](#examples-and-learning-resources)
- [Community resources](#community-resources)

## Official Jev resources

- [Introducing System One Models and Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev) - TypeSafe's launch announcement for System One Models and Jev.
- [TypeSafe AI](https://typesafe.ai/) - Official home for TypeSafe AI, System One Models, and Jev.
- [TypeSafe System One API Reference](https://docs.typesafe.ai/api) - Official HTTP API reference for System One requests and responses.

## SDKs and API clients

- [Advocaat](https://github.com/pithings/advocaat) - A small, type-safe client for asking AI questions about your data, powered by TypeSafe Jev.
- [askif Jev Backend](https://github.com/asakaxgit/askif) - TypeScript toolkit that uses Jev for conditional branches, candidate selection, and scores, with explicit handling of uncertain answers.
- [daf-jev](https://github.com/docxology/daf-jev) - Composable Python client and decision toolkit for the TypeSafe Jev API.
- [Effective Jev](https://github.com/stoopid-computers/effective-jev) - Independent EffectTS-based fork of the TypeSafe JavaScript and TypeScript SDK.
- [Jev for OTP](https://github.com/dannote/jev) - TypeSafe Jev for OTP: reply to Jev from a GenServer and pattern match on its answer.
- [jev go](https://github.com/stumble/jev-go) - Independent Go SDK for TypeSafe AI's Jev and System One API.
- [Jev Go Client by kataras](https://github.com/kataras/jev) - Community Go client for Jev Choice, Score, and Noul requests, typed response decoding, retries, and rate limiting.
- [Jev Haskell Client](https://github.com/realbogart/jev) - Haskell client with typed Choice, Score, and Noul questions for TypeSafe Jev.
- [Jev Python Function Decorator](https://github.com/aaazzam/jev) - Python decorator that maps Pydantic return fields to Jev Choice, Score, and Noul questions.
- [jevclient](https://github.com/AboveColin/jevclient) - Async Python client for TypeSafe Jev. Typed questions in, probabilities and choices out, no prose to parse.
- [jevfilter](https://github.com/damiensmith1/jevfilter) - Python content filtering with Jev topic checks, classifications, candidate-field selection, scores, and explicit review results.
- [LLMTornado Jev Decisions](https://github.com/lofcz/LLMTornado) - .NET library with typed Jev Choice, Score, and Noul requests through TypeSafe or OpenRouter.
- [Ollama JavaScript System One Client](https://github.com/ollama/ollama-js) - JavaScript and TypeScript client for independent local System One models, with typed decision requests in Node.js and browsers.
- [Ollama Python System One Client](https://github.com/ollama/ollama-python) - Python client for independent local System One models, with synchronous and asynchronous Choice, Score, and Noul requests.
- [OllamaSharp System One Client](https://github.com/awaescher/OllamaSharp) - .NET client for independent local System One models through SystemOneAsync, with typed questions and probability-bearing answers.
- [OpenAI Scala Client TypeSafe Module](https://github.com/cequence-io/openai-scala-client/tree/master/typesafe-client) - Scala client with a native TypeSafe System One module for typed Jev questions and answers.
- [ReqLLM Jev Evaluations](https://github.com/agentjido/req_llm) - Elixir library that evaluates typed Jev questions through TypeSafe or OpenRouter and preserves provider response metadata.
- [Rig TypeSafe AI Integration](https://github.com/0xPlaygrounds/rig/tree/main/crates/rig-typesafeai) - Rust agent framework crate for TypeSafe Jev decisions.
- [ruby decision model](https://github.com/obie/ruby_decision_model) - Ruby client for decision models such as Typesafe Jev.
- [RubyLLM TypeSafe](https://github.com/kieranklaassen/ruby_llm-typesafe) - TypeSafe structured-output provider for RubyLLM 2.
- [swift typesafe](https://github.com/ainame/swift-typesafe) - Unofficial Swift SDK for TypeSafe.
- [System One](https://github.com/iamaamir/system-one) - Provider-neutral TypeScript runtime with a tested TypeSafe Jev adapter and a Pi extension.
- [System One Adapter for Python](https://github.com/typesafe-ai/system-one-adapter-python) - Drop-in TypeSafeClient replacement backed by LLM APIs.
- [TypeSafe AI Java SDK](https://github.com/jamilxt/typesafe-ai-java) - Community-maintained Java SDK for Jev with a Kotlin DSL, Spring Boot starter, and Spring AI integration.
- [TypeSafe AI Rust](https://github.com/gilljon/typesafe-ai-rs) - Independent async and blocking Rust SDK for the TypeSafe AI System One API.
- [TypeSafe for Elixir](https://github.com/hfiguera/typesafe_ai) - An Elixir client for TypeSafe AI with typed responses and bounded concurrency.
- [TypeSafe JavaScript and TypeScript SDK](https://github.com/typesafe-ai/typesafe-sdk-js) - The official TypeScript/JavaScript library for the TypeSafe API.
- [TypeSafe Python SDK](https://github.com/typesafe-ai/typesafe-sdk-python) - The official Python library for the TypeSafe API.
- [typesafe rs](https://github.com/abdelstark/typesafe-rs) - Latency-first Rust SDK for TypeSafe System One.
- [TypeSafe Rust SDK](https://github.com/codeitlikemiley/typesafe-sdk-rust) - Community Rust client for the TypeSafe AI API with typed System One request and response support.
- [typesafe sdk](https://github.com/joshmn/typesafe-sdk) - Ruby client for typesafe.ai.
- [TypeSafe SDK for Elixir](https://github.com/nshkrdotcom/typesafe_sdk) - An idiomatic, type-safe Elixir port of the official TypeScript AI SDK (ai / ai-sdk) providing unified LLM integrations, streaming text and structured outputs, tool calling, and agentic workflows. Jev is their current flagship model and is the first System One model.
- [TypeSafe SDK for PHP](https://github.com/butochnikov/typesafe-sdk-php) - PHP client for the TypeSafe AI System One API.
- [typesafe sdk swift](https://github.com/alterhq/typesafe-sdk-swift) - Unofficial Swift library for the TypeSafe API.
- [typesafe-go](https://github.com/cole-gillespie/typesafe-go) - Unofficial Go SDK for the TypeSafe AI API with typed System One requests and responses.
- [vibecheck](https://github.com/jlowin/vibecheck) - Python library for Jev's typed judgments through simple check, classify, label, and score functions.
- [ZIO TypeSafe AI](https://github.com/jamesward/zio-typesafe-ai) - Scala 3 and ZIO library for TypeSafe AI's Jev and System One API.

## Gateways and integrations

- [Agent Squad Jev Classifier](https://github.com/2FastLabs/agent-squad) - Multi-agent framework with TypeScript and Python classifiers that use Jev to route requests.
- [AgentScope](https://github.com/agentscope-ai/agentscope) - AgentScope exposes TypeSafe Jev as a classifier model for structured decisions in agent workflows.
- [AI SDK TypeSafe provider](https://ai-sdk.dev/providers/ai-sdk-providers/typesafe-ai) - Vercel's TypeSafe provider adds Jev evaluation models to AI SDK's typed decision API.
- [Atmosphere TypeSafe Decision Adapter](https://github.com/Atmosphere/atmosphere/tree/main/modules/ai-decision-typesafe) - Java decision-model adapter that maps typed questions and answers to the TypeSafe Jev System One API.
- [Ax TypeSafe Jev Support](https://github.com/ax-llm/ax) - Multi-language AI framework with TypeSafe Jev support in TypeScript, Python, Java, C++, Go, and Rust.
- [Bifrost TypeSafe Provider](https://github.com/maximhq/bifrost/tree/main/core/providers/typesafe) - AI gateway exposing TypeSafe model access through its `/typesafe` integration.
- [Codex Router OpenRouter Decisions](https://github.com/duolahypercho/codex-router) - Codex gateway with a separate OpenRouter Decisions endpoint for structured Jev requests from explicitly configured clients.
- [Composio TypeSafe Providers](https://github.com/ComposioHQ/composio) - TypeScript and Python providers that use Jev to select Composio tools, bind closed-set arguments, and abstain on uncertain requests.
- [GoModel](https://github.com/ENTERPILOT/GoModel) - Go AI gateway that forwards native System One requests to hosted Jev or a self-hosted Kev server.
- [GPTCache Jev Evaluation](https://github.com/zilliztech/GPTCache/blob/main/gptcache/similarity_evaluation/jev.py) - Semantic cache with a Jev evaluator for checking whether a cached answer fits a query.
- [Hono Jev Router](https://github.com/yusukebe/hono-jev-router) - Route HTTP requests by meaning. A semantic router for Hono powered by Jev.
- [Jev on Cloudflare Workers AI](https://developers.cloudflare.com/ai/models/typesafe/jev/) - Cloudflare Workers AI model documentation for TypeSafe Jev.
- [Jev on Netlify AI Gateway](https://docs.netlify.com/build/ai-gateway/overview/) - Netlify AI Gateway access for Jev from Netlify Functions.
- [Jev on Vercel AI Gateway](https://vercel.com/ai-gateway/models/jev) - Vercel AI Gateway model access for TypeSafe Jev.
- [Jev Tool and Model Router](https://github.com/TypeSafeAI/typesafe-router) - Unofficial TypeScript routing library and Next.js lab that uses Jev to select from predefined tools and models with explicit fallbacks.
- [Jevbridge](https://github.com/gamesonrblx/jevbridge) - ACP and MCP adapter that bridges TypeSafe Jev with any LLM — computer use and typed decisions alongside Codex, Claude, Grok, and OpenCode. - tacticocc/Jevbridge.
- [Jevbridge](https://github.com/tacticocc/Jevbridge) - ACP and MCP adapter that brings TypeSafe Jev typed decisions and computer use to multiple agent hosts.
- [jevframe](https://github.com/ktaletsk/jevframe) - Pandas and Polars integration that evaluates dataframe rows with Jev questions and returns structured results and probability distributions.
- [kedi-typesafe](https://github.com/kedi-lang/kedi-typesafe) - Framework-native TypeSafe Jev integrations for Pydantic AI, LangChain, and Kedi.
- [LangChain TypeSafe integration](https://docs.langchain.com/oss/python/integrations/providers/typesafe) - Pre-release Python integration that exposes Jev's Choice, Score, and Noul answers as a LangChain Runnable.
- [LangChain.js TypeSafe integration](https://github.com/langchain-ai/langchainjs/tree/main/libs/providers/langchain-typesafe) - LangChain.js integration for TypeSafe models, with Jev's typed Choice, Score, and Noul questions.
- [Laravel TypeSafe Jev](https://github.com/butochnikov/laravel-typesafe-jev) - Community Laravel integration for TypeSafe Jev with typed responses, async requests, dependency injection, and testing fakes.
- [LiteLLM Jev integrations](https://docs.litellm.ai/docs/auto_router/) - LiteLLM uses Jev for Auto Router classification and relevance checks during context compaction.
- [LlamaIndex Jev](https://github.com/wiktorb2004/llama-index-jev) - LlamaIndex reranker + router powered by TypeSafe Jev — typed scores/choices, cheaper than LLM-as-judge.
- [LLPhant Jev Classifier](https://github.com/LLPhant/LLPhant) - PHP AI framework with a typed Jev classifier for Choice, Score, and Noul questions.
- [n8n-nodes-typesafe-ai](https://github.com/DomMonte/n8n-nodes-typesafe-ai) - n8n community node for branching workflows on TypeSafe System One typed decisions.
- [neo4jev](https://github.com/jexp/neo4jev) - Typesafe.ai System One Model Jev navigating a Neo4j graph by using a classifier over neighbouring relationships.
- [NeuroLink](https://github.com/juspay/neurolink) - TypeScript AI integration layer whose decide API exposes TypeSafe Jev typed judgments alongside generation and streaming.
- [OpenInference TypeSafe Instrumentation](https://github.com/Arize-ai/openinference/tree/main/python/instrumentation/openinference-instrumentation-typesafe) - OpenInference instrumentation for tracing TypeSafe AI SDK calls in OpenTelemetry-compatible systems.
- [OpenRouter AI SDK Decision Provider](https://github.com/OpenRouterTeam/ai-sdk-provider) - AI SDK provider that calls Jev through the OpenRouter Decisions API and maps typed answers to the AI SDK evaluation interface.
- [OpenViking Jev Reranker](https://github.com/volcengine/OpenViking/blob/main/openviking/models/rerank/jev_rerank.py) - Agent context database with a Jev reranker that scores each candidate document against a query.
- [Opik TypeSafe Instrumentation](https://github.com/comet-ml/opik/tree/main/sdks/python/src/opik/integrations/typesafe) - LLM observability platform with instrumentation for TypeSafe calls.
- [pg_typesafe](https://github.com/giuliosmall/pg_typesafe) - Pre-alpha PostgreSQL extension that exposes TypeSafe Jev Choice, Noul, and Score functions in SQL.
- [Pollinations Decisions](https://github.com/pollinations/pollinations) - AI gateway with a typed decision endpoint and SDK calls for Jev Choice, Score, and Noul requests.
- [Pydantic AI TypeSafeModel](https://pydantic.dev/docs/ai/models/typesafe/) - Pydantic AI's TypeSafeModel uses Jev for typed agent outputs and supported tool arguments.
- [RubyLLM](https://github.com/crmne/ruby_llm) - Ruby AI framework whose provider list includes TypeSafe for structured Jev decisions.
- [Spring AI TypeSafe](https://github.com/spring-ai-community/spring-ai-typesafe) - Spring AI TypeSafe provides a Java client and framework integrations for Jev classification, confidence gates, retrieval, and tool search.
- [Sub2API](https://github.com/Wei-Shaw/sub2api) - AI gateway that forwards native Jev System One requests and uses Jev for text moderation.
- [switchboard](https://github.com/aniruddh-krovvidi/switchboard) - Guardrail and model router for LLM gateways built on Jev with an independent calibration evaluation.
- [TanStack AI TypeSafe adapter](https://tanstack.com/ai/latest/docs/adapters/typesafe) - TanStack AI's TypeSafe adapter sends typed Choice, Score, and Boolean questions to Jev through decide().
- [typesafe ai rails](https://github.com/genierobot/typesafe-ai-rails) - Community Rails integration for TypeSafe AI's System One API.
- [TypeSafe Jev on OpenRouter](https://openrouter.ai/typesafe) - OpenRouter model listings and API access for TypeSafe Jev.
- [typesafeify](https://github.com/typesafeainate/dspy-typesafeify) - Add a decorator for dspy Signatures that automatically uses TypeSafe where relevant.

## Agent tools and MCP servers

- [Abide](https://github.com/coldteadotai/abide) - Coding-agent hooks that use Jev to check edits and completed turns against project rules and return rule-specific findings.
- [AgentConnect](https://github.com/agentconnect-md/agentconnect) - Agent collaboration platform that uses Jev typed decisions to route conversations, select reviewers, and choose agent runtimes and models.
- [ask-jev-skill](https://github.com/shantanugoel/ask-jev-skill) - Hermes skill that calls TypeSafe Jev as a typed tiebreaker for agent decisions.
- [Caliber Jev Compaction plugin](https://github.com/caliber-ai-org/ai-setup/tree/master/plugin/caliber-jev-compaction) - Claude Code plugin that uses Jev relevance scores to remove stale tool results during context compaction.
- [Claude Code Templates Jev Mods](https://github.com/davila7/claude-code-templates) - Claude Code toolkit with Jev mods for prompt and reply guardrails, model routing, and skill suggestions.
- [commit miner](https://github.com/devanshbatham/commit-miner) - Classify Git commit diffs and messages with Jev. Bug fixes, security fixes/CWEs, and change types.
- [ctx Jev Selector](https://github.com/ctxrs/ctx) - Context compaction toolkit with an optional Jev selector that checks passage relevance before retaining external tool output.
- [DeerFlow Jev Classifier Extension](https://github.com/bytedance/deer-flow/tree/main/examples/deerflow-extension-jev-classify) - Optional DeerFlow extension that adds a tool for classifying short text batches with Jev Choice questions.
- [DeerFlow Jev Context Pruning](https://github.com/bytedance/deer-flow/tree/main/examples/deerflow-extension-jev-context) - Optional DeerFlow extension that uses Jev to shorten old read-only tool results before summarization.
- [fast dev compaction](https://github.com/leonaaardob/fast-dev-compaction) - Codex plugin: verbatim Jev-guided context restoration around session compaction. Port of tamaratran/fast-jev-compaction to Codex lifecycle hooks.
- [fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) - Claude Code plugin that replaces the compaction summary with Jev decisions: every tool call and result is scored in one fast request, stale ones are dropped or truncated, everything kept stays verbatim.
- [grok-bot-jev](https://github.com/Bodila51/grok-bot-jev) - Python decision layer that adds Jev-based usage gates and approval-aware routing to Grok Bot.
- [Hermes Jev Skills](https://github.com/kerpopule/hermes-jev-skills) - Agent skills that use Jev for model routing, memory, compaction, skill selection, and computer-use decisions.
- [Hippo Memory](https://github.com/kitfunso/hippo-memory) - Hippo Memory optionally uses Jev to rerank recalled memories in its agent-memory workflow.
- [jev](https://github.com/okooo5km/jev) - Unofficial CLI and agent skill for TypeSafe Jev judgments with an OpenRouter fallback.
- [jev axi](https://github.com/shiftynick/jev-axi) - Agent-ergonomic CLI for TypeSafe's Jev: fast calibrated judgments (pick, rate, check, rank, triage, guard) from the shell.
- [Jev Codex Router](https://github.com/0xNatoshi/jev-codex-router) - Per-turn model & reasoning routing for Codex, driven by Jev (TypeSafe System One): picks the model, thinking depth and speed mode for every turn.
- [Jev Curate](https://github.com/AkashPriyadarshii/jev-curate) - High-throughput synthetic & pretraining dataset sifter powered by TypeSafe AI Jev (api.typesafe.ai). Stream, filter, and score Parquet & JSONL datasets at 1,500+ rows/sec using System One typed decisions (Choice, Score, Noul).
- [jev judgment](https://github.com/hyunjunjeon/jev-judgment) - Agent Skill: send closed coding-agent judgments to TypeSafe Jev.
- [jev pref](https://github.com/doeixd/jev-pref) - Turn your AGENTS.md preferences into a fast, Jev-powered AI linter.
- [Jev Review MCP](https://github.com/niazmorshed2007/jev-review) - Local-first MCP plugin for continuous software-quality review by AI coding agents, powered by Jev.
- [jev scout](https://github.com/AkashPriyadarshii/jev-scout) - Zero-hallucination repository and crate scout powered by TypeSafe AI Jev System One scoring.
- [jev seo](https://github.com/AkashPriyadarshii/jev-seo) - 100% free ₹0 agent-first SEO & GEO CLI suite and MCP server in Rust replacing Semrush and OpenSEO via DuckDuckGo and TypeSafe Jev System One.
- [jev shell history](https://github.com/mrnugget/jev-shell-history) - Fish-style zsh history autosuggestions ranked by Jev (TypeSafe).
- [Jev Skill](https://github.com/wuyoscar/jev-skill) - Collection of Jev use cases, workflows, and agent skills for bounded decisions.
- [Jev Skill Suggester](https://github.com/win4r/jev-skill-suggester) - Codex skill and Python CLI that recommends an installed skill with TypeSafe Jev.
- [Jev Studio](https://github.com/utk2103/jev-studio) - CLI and MCP toolkit for Jev decisions, with prompt libraries and commands for classification, verification, reranking, routing, and compaction.
- [jev superpowers](https://github.com/AkashPriyadarshii/jev-superpowers) - Systematic software development framework for AI coding agents upgraded with TypeSafe Jev System One typed decisions.
- [jev tree](https://github.com/reachjalil/jev-tree) - Recursive Jev choice over a taxonomy. Select from more than 255 options without breaking TypeSafe Jev's choice cap.
- [jev use](https://github.com/shitianfang/jev-use) - Claude Code / Codex / pi plugin that hands agent steps needing no text output to Jev (TypeSafe's judgment model) — measured p50 ~230 ms and ~$0.02 per 1,000 judgments, with typed escalation back to the LLM.
- [jev-agent-kit](https://github.com/walidboulanouar/jev-agent-kit) - Zero-dependency CLI and MCP toolkit for Jev routing, triage, guardrails, search, ranking, and compaction.
- [jev-agent-tool](https://github.com/nandansrikrishna/jev-agent-tool) - BYOK CLI, Python API, and local MCP server for typed judgments with TypeSafe Jev.
- [jev-cli](https://github.com/tumf/jev-cli) - Dependency-free CLI and stdio MCP server for TypeSafe Jev Noul, Choice, and Score judgments.
- [Jev-cu](https://github.com/Sac-Y/Jev-cu) - Codex computer-use skill that delegates text-only action selection to Jev with local safety gates.
- [jev-dsh-decision](https://github.com/Devin-AXIS/jev-dsh-decision) - Agent-harness plugin that exposes Jev evaluations for tool, skill, and task selection.
- [jev-gateway](https://github.com/vinilana/jev-gateway) - Gateway that uses Jev to route coding-agent tool choices with fail-open passthrough.
- [jev-guard](https://github.com/leepokai/jev-guard) - Auto mode for every coding agent, built on Jev: risk-scores every tool call with session context (deny / ask / allow), flags prompt injection in results, checks skills and plugins. Claude Code, Codex, Copilot, Gemini, Cursor, pi, OpenCode, ACP.
- [jev-kit](https://github.com/jonathanavis96/jev-kit) - jev-kit adds TypeSafe Jev tool-call checks, task tiering, browser tools, and review workflows to Claude Code.
- [jev-mcp by burnigtm](https://github.com/burnigtm/jev-mcp) - Local stdio MCP server that exposes TypeSafe Jev judgments for coding agents and MCP clients.
- [jev-mcp by jkudish](https://github.com/jkudish/jev-mcp) - Fast, cheap, typed judgments from TypeSafe's Jev model, as MCP tools.
- [jev-mcp-spring](https://github.com/Ashfaqbs/jev-mcp-spring) - Java and Spring Boot MCP server that exposes TypeSafe Jev judgments to MCP clients.
- [jev-predict-skill](https://github.com/DanielKillenberger/jev-predict-skill) - Agent skill that predicts another skill's next closed decision with Jev without running that skill.
- [jev-pruner](https://github.com/tamaratran/jev-pruner) - Claude Code and Codex plugin that uses Jev to trim noisy Bash output before it reaches the main model.
- [jev-router](https://github.com/gargpratyush/jev-router) - Route to the cheapest model in claude code for your task using jev-router.
- [jev-rules](https://github.com/EliaAlberti/jev-rules) - Claude Code plugin that uses Jev to select applicable project rules and map documents.
- [jev-sift](https://github.com/kbhuw/jev-sift) - Portable agent plugin and MCP tool for batch relevance classification with Jev.
- [jevcore](https://github.com/PerryLink/jevcore) - Framework-independent Jev client with DeepSeek Harness and MCP adapters for typed questions, candidate ranking, and evidence checks.
- [JevGrep](https://github.com/nassim-arifette/jevgrep) - CLI and MCP server for Jev-scored semantic code search.
- [JevHarness](https://github.com/TianyuCodings/JevHarness) - Task-specific Python harnesses that combine LLM authoring with Jev decisions, execution traces, and optional reward-based reflection.
- [jevon](https://github.com/douglance/jevon) - Rust command-line interface and MCP server for TypeSafe Jev typed decisions.
- [JevRouter](https://github.com/BillionsBobby/JevRouter) - Typed agent router that selects models, subagents, skills, MCP tools, CLIs, and plugins.
- [jevwire](https://github.com/Brainwires/jevwire) - Jev decision layer for agents: MCP server, embeddable DecisionModel library, and an escalate-only Claude Code plugin (TypeSafe AI's Jev).
- [MemoraX Code](https://github.com/memorax-ai/memorax-code) - MemoraX Code can ask Jev whether a coding agent should retrieve stored engineering knowledge for a request.
- [MemSearch](https://github.com/zilliztech/memsearch) - Persistent agent memory layer with optional Jev reranking for hybrid search results.
- [Oh My ClaudeCode Jev Judgments](https://github.com/Yeachan-Heo/oh-my-claudecode) - Claude Code orchestration plugin with opt-in Jev judgments for skill triggers, model tiers, and loop progress.
- [Oh My Pi](https://github.com/can1357/oh-my-pi) - Coding agent with a native Jev judgment backend for typed questions and batch classification of files, logs, and other items.
- [OpenClaw TypeSafe Extension](https://github.com/openclaw/openclaw/tree/main/extensions/typesafe) - OpenClaw extension for typed decisions through TypeSafe's Jev API.
- [Pentest Swarm AI](https://github.com/Armur-Ai/Pentest-Swarm-AI) - Autonomous penetration-testing swarm with optional Jev filtering and adaptive attack-path scoring.
- [pi fast jev compaction](https://github.com/joelhooks/pi-fast-jev-compaction) - Pi extension: verbatim context compaction with TypeSafe Jev decisions.
- [Pi MCP Adapter Jev Search](https://github.com/nicobailon/pi-mcp-adapter) - Pi MCP adapter with optional Jev semantic tool search and typed script evaluations restricted to configured servers.
- [pi warden](https://github.com/devmortimer/pi-warden) - Guardrails for Pi built on pi-typesafe that steer the agent instead of interrupting you: Jev judges irreversible and off-task tool calls, detects stuck loops, checks unverified done claims, flags slop.
- [pi-jev](https://github.com/y0usaf/pi-jev) - TypeSafe Jev as a decision layer for the Pi coding agent: a measured tool-call gate plus jev_ask for typed, calibrated answers.
- [pi-jev by TheoOliveira](https://github.com/TheoOliveira/pi-jev) - Pi coding-agent extension for semantic tool routing, skill discovery, and typed Jev decisions.
- [pi-jev-auto-mode](https://github.com/jomatsu/pi-jev-auto-mode) - Pi coding-agent auto mode that uses Jev to judge Bash, write, and edit tool calls with fail-closed behavior.
- [PowerContext System One Adapter](https://github.com/oceanbase/powercontext) - Context and memory toolkit with an optional Jev adapter for advisory decisions and examples of memory applicability checks.
- [save-token-jev-clean](https://github.com/IAmUnbounded/save-token-jev-clean) - Cross-agent context-compaction plugins that use Jev to retain, bound, or drop tool results.
- [Supercov](https://github.com/supercorp-ai/supercov) - Supercov tells your coding agent what to fix and what to test with Jev-based code-quality scoring.
- [System 1 MCP](https://pypi.org/project/system1-mcp/) - MCP server that exposes Jev-powered guard, judge, verify, and score tools for AI agents.
- [System One Harness](https://github.com/HarnessRouter/SystemOneHarness) - Agent harness that turns finite actions into typed Jev decisions and confidence-gated execution.
- [treg Jev Memory](https://github.com/superdesigndev/treg/tree/main/examples/claude-code-mods/jev-memory) - Claude Code mod that uses Jev through treg to identify lasting preferences in prompts and save them for later sessions.
- [TypeSafe Agent Skills](https://github.com/typesafe-ai/skills) - Agent skills for building with TypeSafe's System One API.
- [typesafe-mcp](https://github.com/itsmostafa/typesafe-mcp) - mcp connector to give your AI agent direct access to typesafe ai's jev model.
- [VexJoy Agent](https://github.com/notque/vexjoy-agent) - VexJoy AI Agent with Jev Intelligent Routing - /do routes plain-English requests to the right specialist agent and gates the work with reviews, tests, and a learning loop.
- [wakegate](https://github.com/shitianfang/wakegate) - Ask Jev whether a sleeping agent's wakeup is worth a full LLM turn before you resume it. A fail-open wake gate for long-running agents on Workers, Durable Objects and Node.
- [winnow](https://github.com/GhalebDweikat/winnow) - Calibrated context sieve for Claude Code that filters large tool results before they enter the model context.
- [yoshi](https://github.com/compozy/yoshi) - Context-pruning proxy for Claude Code and Codex: Jev judges which history is still needed, measured not claimed. POC here now, heading soon into https://github.com/compozy/compozy.

## Browser and computer-use agents

- [Jev Browser](https://github.com/jkudish/jev-browser) - Browser use using Typesafe's Jev model.
- [jev browser](https://github.com/ying-kai-liao/jev-browser) - Browser automation where an LLM plans and Jev (Typesafe System One) decides. Library, CLI and MCP server.
- [Jev Browser Pilot](https://github.com/aidil2105/jev-browser-pilot) - Bounded browser and desktop automation layer where Jev chooses the next action.
- [Jev Browser Use](https://github.com/wy-coliney/jev-browser-use) - 5–10x faster browser operations: Jev clicks, Codex thinks and verifies. Built at EZCollegeApp.
- [jev canvas](https://github.com/gaborishka/jev-canvas) - Draw on a tldraw canvas with your voice and a pointing finger. Jev (TypeSafe System One) decides action, target and place in ~350 ms per spoken word.
- [Jev Desktop for Codex](https://github.com/yikangy873-gif/jev-desktop) - Bounded Jev decision loop for Codex Computer Use across browser tabs and native macOS apps.
- [jev ego](https://github.com/romaluev/jev-ego) - Fast browser agent for ego lite. One TypeSafe request per step; an agent or Jev picks the move.
- [jev for chrome](https://github.com/chy4pro/jev-for-chrome) - Jev for Chrome: drives the tab you are looking at with TypeSafe Jev, a sub-second decision model. Community port of browser-use/jev-ultrafast, not affiliated with TypeSafe.
- [Jev macOS Loop](https://github.com/jcpsimmons/jev-macos-loop) - Open-source native macOS computer-use agent combining local vision and Jev action selection.
- [Jev Ultrafast](https://github.com/browser-use/jev-ultrafast) - TypeSafe's Jev picks an operation and an element while a small LLM writes text only for TYPE_TEXT.
- [Jev Voice Browser](https://github.com/moritzkremb/jev-voice-browser) - Control a real browser by voice. Jev (TypeSafe System One) decides intent + target in ~300 ms per spoken word; Playwright acts — often before you finish the sentence.
- [jev-recruiter](https://github.com/skeptrunedev/jev-recruiter) - Local recruiting workspace where Jev screens visible LinkedIn profiles against a hiring brief.
- [jev-use](https://github.com/savka777/jev-use) - macOS voice and typed computer-use harness that selects actions from the Accessibility tree with Jev.
- [jev-voice](https://github.com/kevinbadi/jev-voice) - macOS voice-control app that uses Whisper and one TypeSafe Jev call per command.
- [jevnav](https://github.com/dtduc-git/jevnav) - Browser automation layer that uses Jev to select page elements, gates uncertain actions, and records traces for offline replay.
- [macOS Computer Use Kit Jev Guards](https://github.com/Sur-Cai/macos-computer-use-kit) - macOS MCP server and CLI with optional Jev judgments for semantic guardrails before irreversible actions.
- [Mobile Jev](https://github.com/droidrun/mobile-jev) - Mobile agent for Mobilerun that uses Jev to choose actions on a real Android device.
- [Needle](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_llm_apps/needle) - Chrome extension and React app that use Jev to rank webpage passages and highlight the most relevant sentence.
- [TipTour](https://github.com/milind-soni/tiptour-macos) - macOS computer-use app where Jev selects click targets from locally detected controls.
- [TypeSafe AdBlock](https://github.com/realZachi/typesafe-adblock) - 🧹 Fun project: a Chrome extension that asks a tiny AI decision model (TypeSafe Jev) "is this DOM element an ad?" and pops it off the page. BYOK, no backend, not a real ad blocker.
- [TypeSafe Computer Use](https://github.com/awlevin/typesafe-computer-use) - Computer use for about $0.0002 a step: OCR the screen, classify the next action with TypeSafe, click. macOS.
- [unclutter](https://github.com/kitze/unclutter) - WXT browser extension: Jev-powered page clutter removal with reusable template rules.

## Applications and developer tools

- [AI Hedge Fund](https://github.com/virattt/ai-hedge-fund) - Open-source AI hedge fund framework with a TypeSafe Jev provider for investor agents.
- [Astra and JEV Minecraft agent](https://github.com/rmalde/minecraft-agent) - Minecraft agent that uses Astra for planning and JEV for bounded player-action selection.
- [AutoRAG Jev Decisions](https://github.com/Marker-Inc-Korea/AutoRAG) - Search agent that uses Jev to route queries, check answer completeness, and expose typed judgment tools.
- [Bilingual Book Maker](https://github.com/yihong0618/bilingual_book_maker) - EPUB translation tool with an optional Jev classifier that selects which text blocks to translate and flags uncertain decisions.
- [Blink](https://github.com/ellipsis-dev/blink) - Codebase search powered by Jev from @typesafe-ai.
- [CodexBar TypeSafe Usage](https://github.com/steipete/CodexBar) - Menu bar usage monitor with an optional TypeSafe integration for Jev account spending, credit balances, and credit expiration dates.
- [DailyPaper Skills](https://github.com/huangkiki/dailypaper-skills) - Research-paper skills that use Jev to score abstracts for topical relevance before an agent reviews selected papers.
- [Dasheng](https://github.com/wquguru/dasheng) - English reading practice that uses Jev to judge word-level correctness and sentence-level scores.
- [Distill](https://github.com/samuelfaj/distill) - Coding-agent harness that uses Jev for model selection, effort choices, and tool-result compaction.
- [DocJev](https://github.com/jerryjliu/docjev) - Document classifier and splitter that uses Jev to assign categories and detect document boundaries after local text extraction.
- [Dub Jev Malicious Link Check](https://github.com/dubinc/dub/blob/main/apps/web/lib/api/links/malicious-link-check.ts) - Link attribution platform that screens destination URLs with Jev when links are created.
- [EdgeQuake Decision Extraction](https://github.com/raphaelmansuy/edgequake) - Knowledge-graph platform with experimental extraction through independent local Tev1 System One models served by Ollama.
- [EmbodiedJev](https://github.com/FBddcz/embodied-jev) - MuJoCo robot decision workbench with TypeSafe Jev, MiniCPM, and compatible model APIs.
- [evoke](https://github.com/evoke-build/evoke) - Rust CLI, reflex package manager, and TypeScript SDK where Jev selects a small installed program and its arguments.
- [Foreman](https://github.com/thruwire/foreman) - Software factory foreman based on TypeSafe's Jev model.
- [GenOffice](https://github.com/genspark-ai/genoffice) - Desktop office suite with optional Jev reranking for local file searches.
- [GPT Researcher](https://github.com/assafelovic/gpt-researcher) - Research agent that uses TypeSafe Jev to score scraped passages before context reaches its language model.
- [HA-Jev](https://github.com/AboveColin/HA-Jev) - Ask your house a question, get a number back. Home Assistant integration for TypeSafe Jev: typed answers as sensors, four actions for automations, and a conversation agent for Assist.
- [Inbox Zero TypeSafe Decision Provider](https://github.com/elie222/inbox-zero/tree/main/apps/web/utils/decision-model) - Email assistant with an optional TypeSafe decision provider.
- [invalidate](https://github.com/chopratejas/invalidate) - Agent memory invalidation layer that uses Jev to decide when stored facts are no longer valid.
- [is-malicious](https://github.com/luantak/is-malicious) - A codebase scanner that helps you not run malicous code.
- [Jev as Policy](https://github.com/YuanKJing/Jev-as-Policy) - MuJoCo robotics demo that uses Jev choices to select manipulation intent and bounded motor actions.
- [jev belay](https://github.com/valentynkit/jev-belay) - Claude Code Stop hook that blocks an unverified done: reads the transcript for evidence, asks Jev once, fails open on everything else.
- [Jev Chat](https://github.com/w3cj/jev-chat) - Tool-calling chat application that uses Jev without an LLM writing the reply.
- [Jev Chat Assistant](https://github.com/jev-chat/jev-chat-jarvis) - Android chat assistant that uses Jev to classify conversations and rank candidate replies before manual insertion.
- [jev commit](https://github.com/valentynkit/jev-commit) - pre-commit hook: one Jev call judges whether your commit message matches the diff, plus debug leftovers, scope creep, and a secret belt.
- [JEV DataOps](https://github.com/RenaGao/jev-dataops) - Data workbench that screens datasets with Jev before optional LoRA training and held-out evaluation.
- [Jev Drone](https://github.com/RomanSlack/jev-drone) - Camera-only autonomous drone in MuJoCo with a small judgment model (TypeSafe Jev) in the loop at 2.5Hz.
- [Jev Logs](https://jevlogs.com) - Open-source Jev log triage for OpenTelemetry. Score the signal before expensive LLM analysis.
- [jev moderation bot](https://github.com/brainstormity/jev-moderation-bot) - A Discord moderation bot built with Python and TypeSafe AI Jev System One.
- [jev plays pokemon red](https://github.com/valentynkit/jev-plays-pokemon-red) - Pokemon Red on PyBoy: code owns the route and the arithmetic, Jev picks at branches in about 100 ms, calibration measured instead of assumed.
- [Jev Review](https://github.com/devagrawal09/jev-review) - A staged code-review workflow and local dashboard built with TypeSafe Jev.
- [Jev Reviewer](https://github.com/choxos/jev-reviewer) - Browser-based systematic-review extraction tool that uses Jev to locate quoted evidence in research files.
- [Jev Search](https://github.com/superagents-lab/jev-search) - Search the web with TypeSafe's Jev: source selection, query understanding and relevance ranking. Built with Search1API.
- [jev skip](https://github.com/valentynkit/jev-skip) - YouTube sponsor skipper that reads the captions and decides at watch time: a probability heatmap on the seek bar, no crowd database.
- [Jev Social](https://github.com/socai-io/jev-social) - Jev-powered Instagram, TikTok, and LinkedIn research: typed routing, real browser evidence, streamed post cards, video capture, and cited socai reports.
- [Jev Trade](https://github.com/aowang-ai/jev-trade) - Live Jev trader on Hyperliquid.
- [Jev X Sentiment Analysis](https://github.com/brainstormity/Jev-X-Sentiment-Analysis) - Crypto market intelligence terminal that combines X sentiment, market data, and Jev decisions.
- [jev-align](https://github.com/sutro-sh/jev-align) - Experimental CLI for improving AI Functions with human labels, uncertain examples, and GEPA.
- [Jev-Mem](https://github.com/libingzheren/Jev-Mem) - Agent memory system that uses Jev to organize memories and route, score, and stop retrieval operations.
- [jev-preview](https://github.com/ArkadyBuryakov/jev-preview) - Keyboard-driven terminal UI for composing TypeSafe Jev requests and viewing probability responses.
- [jev-semgrep](https://github.com/uehaj/jev-semgrep) - Meaning-based grep that uses Jev to filter lines, paragraphs, structured records, and code by description.
- [jev-seo](https://github.com/AgriciDaniel/jev-seo) - Website audit CLI and agent skill that uses Jev to assess page intent, content, titles, descriptions, and citation readiness.
- [jev-test-filter](https://github.com/mizchi/jev-test-filter) - CLI that asks Jev which tests are likely affected by the current Git diff and runs the matching test subset.
- [jev-trader](https://github.com/jarrodwatts/jev-trader) - One AI trade decision every Monad block. Jev on Kuru MON-USDC.
- [jev.nvim](https://github.com/valentynkit/jev.nvim) - Neovim: ask the buffer a question, get a quickfix list. Treesitter splits functions, Jev scores each one, probabilities land as virtual text.
- [jevcache](https://github.com/hyperspaceai/jevcache) - Local decision cache for Jev-class models with deterministic replay and redacted state fingerprints.
- [JevCal](https://github.com/abhixhek/jevcal) - Stop guessing confidence thresholds: calibrate, threshold, and drift-check typed decision models (TypeSafe Jev) against an LLM teacher.
- [Jevgrep by dzhng](https://github.com/dzhng/jevgrep) - Code search CLI that uses Jev to judge folder, file, and declaration relevance and return source excerpts to coding agents.
- [Jevinik](https://github.com/unicodeveloper/jevocks) - Stock decision terminal that combines live market evidence with Jev probability estimates.
- [jevlang](https://github.com/sumanmichael/jevlang) - Python DSL and import hook that turns tilde expressions and jev blocks into TypeSafe Jev decisions.
- [Jevmail](https://github.com/fazlerocks/jevmail) - Local, read-only Gmail triage application that sorts messages into typed Jev categories.
- [JevMeter](https://github.com/chetaslua/jevmeter) - Put a live Jev (TypeSafe) meter on any video: every sentence scored, rendered as a 16:9 edit.
- [JevPilot](https://github.com/standardagents/jevpilot) - Three.js driving simulator with a Jev-powered autopilot.
- [JevQL](https://github.com/kylemclaren/jevql) - Semantic SQL for Postgres, powered by Jev.
- [jgrep](https://github.com/keltokhy/jgrep) - grep, but the pattern is a description. Filters lines by meaning with TypeSafe's Jev decision model: ~200 ms and a thousandth of a cent per line.
- [jsort](https://github.com/keltokhy/jsort) - CLI that orders lines by a plain-English dimension using pairwise Jev judgments.
- [killmyidea](https://github.com/monteduro/killmyidea) - Describe your startup idea. Jev decides: kill it, fix it or ship it.
- [LandPPT](https://github.com/sligter/LandPPT) - Presentation generator with an optional Jev decision model that scores slide content against candidate layouts.
- [Math-To-Manim](https://github.com/HarleyCoops/Math-To-Manim) - Math and physics animation pipeline that uses TypeSafe Jev to review staged explanation, equation, and code checkpoints.
- [NeuroSploit](https://github.com/JoasASantos/NeuroSploit) - Security testing framework that uses Jev to adjudicate vulnerability evidence and flag uncertain findings for review.
- [OpenCodex](https://github.com/lidge-jun/opencodex) - Codex and Claude Code provider proxy with an optional Jev route for selecting a model and reasoning effort.
- [OpenCompany](https://github.com/tinyhumansai/opencompany) - OpenCompany uses Jev to select which agent handles a room message or broadcast in its multi-agent runtime.
- [OpenHarness Jev Sheets](https://github.com/autonomous-ai/openharness/tree/main/store/agents/jev-sheets) - Spreadsheet harness that uses Jev to answer typed questions for imported rows and compare question wording on a fixed sample.
- [OpenHuman](https://github.com/tinyhumansai/openhuman) - Rust agent harness that uses Jev to rank tool-search candidates and select browser actions, with host-controlled approval gates for consequential actions.
- [OpenIntelligentUI](https://github.com/CopilotKit/OpenIntelligentUI) - Chat application that uses Jev to select the renderer and visualization type for tables, charts, diagrams, calculators, and maps.
- [OpenMausBot](https://github.com/milind-soni/OpenMausBot) - Multi-bot workspace that uses Jev to route unmentioned room messages to an appropriate bot, with a lead-bot fallback.
- [OpenMuse](https://github.com/CopilotKit/openmuse) - Personal agent that uses Jev to choose clarification or comparison panels and rank options in interactive conversations.
- [Paca](https://github.com/Paca-AI/paca) - Project management platform that uses Jev for agent routing, task field suggestions, assignment, and automation conditions.
- [perch](https://github.com/lakeday-org/perch) - Semantic code linting tool with a CLI, custom rules, and agent integrations.
- [pg-jev](https://github.com/realZachi/pg-jev) - Ask your Postgres tables questions in plain language. A PostgreSQL extension powered by TypeSafe's Jev.
- [PyGPT Jev Plugin](https://github.com/szczyglis-dev/py-gpt) - Desktop assistant with an inline Jev plugin for typed classification, routing, verification, selection, and scoring.
- [quackd](https://github.com/rokbenko/quackd) - One CLI for all your robots. Connect them, command them, and let them work together, each with an LLM for a brain, Jev for cheaper steps. Microduck, Open Duck Mini, LeRobot, XLeRobot, AlohaMini, ToddlerBot or any ROS base. Claude, OpenAI, Gemini, Grok, or local via Ollama or vLLM. Simulator, .duck safety contracts, MCP, memory between runs, flocks.
- [QuantDinger](https://github.com/OpenByteInc/QuantDinger) - Open-source AI Trading OS, agent trading, and vibe trading, with Jev System One integration. Research, build Python strategies, backtest, and paper/live trade across crypto, stocks, and forex. Launch your own multi-tenant trading SaaS with built-in user management, billing, payments, and settlement.
- [Quivr](https://github.com/The-Vibe-Company/quivr) - Content search and monitoring engine with Jev plugins for passage reranking and alerts based on natural-language descriptions.
- [RedAmon](https://github.com/samugit83/redamon) - Security testing framework that uses Jev to classify reconnaissance results, prioritize scan targets, and assess tool outcomes.
- [ShapeShift](https://github.com/anishfn/shapeshift) - ShapeShift turns natural-language input into interactive cards after Jev classifies intent across typed questions.
- [Sim TypeSafe Jev Provider](https://github.com/simstudioai/sim/tree/main/apps/sim/providers/typesafe) - Workflow builder with Jev evaluation models for structured agent decisions.
- [SiYuan TypeSafe Decision Tool](https://github.com/siyuan-note/siyuan/tree/master/kernel/mcp/tools) - Knowledge management system with an agent decision tool backed by TypeSafe System One.
- [skillranker](https://github.com/Dicklesworthstone/skillranker) - Rust CLI powered by Jev from TypeSafe.ai that ranks agent skills for the next step using live session context. Includes Claude Code hooks, structured JSON, abstention, and local feedback. Requires a TypeSafe API key.
- [Sponsor Skip](https://github.com/trungdq88/youtube-sponsor-detection) - Chrome extension that uses Jev to find and skip sponsored segments in YouTube videos.
- [sqlite-jev](https://github.com/mgaitan/sqlite-jev) - Batched natural-language judgments for SQLite, powered by TypeSafe Jev.
- [Stanley](https://github.com/devagrawal09/stanley-code) - Bounded TypeSafe Jev workflows for coding agents.
- [Tax Document Classifier](https://github.com/kyotofin/tax-doc-classifier) - Tax document page classifier built on Jev decisions. 100% strict accuracy across 261 IRS forms, ~$0.001 per page.
- [TradingAgents](https://github.com/TauricResearch/TradingAgents/blob/main/tradingagents/agents/post_screen.py) - Multi-agent trading framework that uses Jev to screen StockTwits and Reddit posts for relevance and stance before sentiment analysis.
- [TypeSafe Mario](https://github.com/fhshaik/typesafe-mario) - A TypeSafe/Jev agent that plays Super Mario Bros. from structured emulator state.
- [typesafe snake](https://github.com/sorrycc/typesafe-snake) - Snake auto-played by TypeSafe's Jev model: one System One choice per tick, legal moves and facts generated in code.
- [Vercel eve](https://github.com/vercel/eve) - Vercel's agent framework uses Jev for response-model selection, typed evaluations, and tool-call approval.
- [wagtail-jev](https://github.com/rinti/wagtail-jev) - Wagtail plugin that uses Jev to suggest page tags and rate text against declared qualities.
- [watfile](https://pypi.org/project/watfile/) - CLI that classifies documents into folders with Jev or local Laya models.
- [x-scanner](https://github.com/oso95/x-scanner) - Chrome extension that labels posts on X with typed Jev judgments and a live cost counter.
- [Yao Agents](https://github.com/YaoApp/yao) - Yao Agents connects its agent runtime to TypeSafe Jev through Tao for typed classification and scoring.

## Open System One implementations

- [AnyJev](https://github.com/nokia-applied-research/AnyJev) - Independent Jev-style library that extracts typed decisions from open LLMs with option rotation, calibration, and optional fitted decision heads.
- [choosekit](https://github.com/NotXf1le/choosekit) - Typed choices and probabilities from models running in llama.cpp.
- [CLM](https://github.com/Contrastive-LM/CLM) - CLM serves an independent contrastive System One model through a Jev-compatible API for typed decisions.
- [Colibri System One](https://github.com/JustVugg/colibri) - Independent local inference engine with a Jev-compatible System One endpoint for typed choices, scores, and yes/no probabilities.
- [CUA-S1 Forms](https://github.com/trycua/cua/tree/main/libs/cua-s1) - Open computer-use decision model inspired by Jev that scores form actions in one pass.
- [DeepOpen](https://github.com/deepopen-com/deepopen) - DeepOpen is an independent multilingual System One decision engine with reproducible evaluation code.
- [Intern-Decision](https://github.com/InternLM/Intern-Decision) - Independent Qwen-based decision models with training, inference, calibration, and evaluations for typed text and image questions.
- [Jeff](https://github.com/firelex/jeff) - Independent local decision models with a Jev-compatible API for typed choices, scores, and yes/no probabilities.
- [NeoHorse-Jev](https://github.com/TokenRhythm/NeoHorse/tree/main/jev) - Independent structured decision model with prefill-only inference, typed System One requests, and vLLM and SGLang backends.
- [oMLX System One](https://github.com/jundot/omlx) - Independent Apple Silicon inference server that runs Clef and OpenJev decision models through a typed System One API.
- [OpenDecision](https://github.com/deepanwadhwa/OpenDecision) - Open semantic decision engine that returns structured choices from state, questions, and criteria.
- [PlayJev](https://github.com/OmniJev/playjev) - 🚀🚀 A 0.8B JEV-like multimodal model playing GUI games directly from raw pixels.
- [Rapid-MLX System One Server](https://github.com/raullenchai/Rapid-MLX) - Independent Apple Silicon server for Laya and CLM decisions through a TypeSafe-compatible System One API.
- [RuVector TypeSafe](https://github.com/ruvnet/RuVector/tree/main/npm/packages/typesafe) - Independent local decision engine with embedding-based heads, abstention, and a Jev-compatible System One API.
- [Tev1](https://github.com/togethercomputer/tev1) - Independent Jev-inspired Qwen3.5-4B fine-tuning recipe with decision datasets, training examples, and evaluation results.
- [XERJ](https://github.com/xerj-org/xerj) - Search engine with optional Jev reranking and a separate local System One-compatible endpoint.

## Open-source Jev Alternatives

- [Decider](https://github.com/mapika/decider) - One-pass typed decisions with calibrated probabilities (System One style model), fine-tuned from Qwen3.5-2B.
- [Jeff](https://github.com/logan-markewich/jeff) - A self-hosted drop-in replacement for TypeSafe's jev, powered by GliFormer.
- [Jev Visual](https://github.com/hr98w/jev-visual) - Educational Jev-like visual inference project for Apple Silicon with a local UI, CLI, and HTTP API.
- [Jevlike](https://github.com/vinnylarouge/jevlike) - Experimental model for selecting among dynamically supplied text options.
- [jevmlx](https://github.com/bnsd55/jevmlx) - Jev-style parallel constrained decisions for any MLX model on Apple Silicon. Typed, schema-valid JSON in one forward pass.
- [JevOS](https://github.com/feder-cr/jev) - JevOS runs local yes/no decision inference and exposes a Jev-compatible endpoint for Noul requests.
- [KaLM-Jev](https://github.com/KaLM-Embedding/KaLM-Jev) - Local Choice, Score, and Noul service built on KaLM-Reranker-V1-R2 with a Jev-compatible System One endpoint.
- [Kev](https://github.com/jaredpalmer/kev) - tiny Jev-like model built on top of Qwen2.5-0.5B you can train and run on your MacBook.
- [Laya](https://github.com/NandhaKishorM/laya) - Laya evaluates typed questions (`choice`, `score`, `noul`) over any state (text, email, ticket or JSON document) in **a single forward pass** — 33 ms for one question, 7.2 ms/question batched, measured on a T4. No text generation, so nothing to parse and nothing to hallucinate.
- [Laya MLX](https://github.com/mizorewww/laya-mlx) - MLX runtime that runs Laya typed-decision models locally on Apple Silicon.
- [LightJev](https://github.com/rongxinzy/LightJev) - Trainable Qwen3-0.6B decision model with Choice, Boolean, and ordinal Score outputs.
- [LitJev](https://github.com/zhengxuyu/litjev) - Turn any off-the-shelf LLM into a Jev -like decision layer.
- [LLM2Jev](https://github.com/Yinsongxu/LLM2Jev) - Independent local model adapter that returns Jev-style Choice, Score, and Noul decisions.
- [LocalJev](https://github.com/githubnext/localjev) - Local Jev-compatible API server backed by DiffusionGemma.
- [mini-Jev](https://github.com/r-ms/mini-jev) - Preregistered Qwen3-4B experiment that reads option-letter logits for Jev-style typed decisions.
- [NanoJev](https://github.com/TianyuCodings/NanoJev) - A nano replica of Jev: parallel decisions, dynamic candidates, and an end-to-end training pipeline.
- [Ollaya](https://github.com/ollaya-dev/ollaya) - Ollaya serves local decision models through TypeSafe-compatible API and MCP endpoints for agent clients.
- [Open Alternative to Jev](https://github.com/ikermoel/open-alternative-jev) - Open-weight System One-style model layer for typed, calibrated decisions in one forward pass.
- [OpenJev](https://github.com/razorback16/openjev) - Open, Jev-compatible System One decision server on DiffusionGemma.
- [openjev](https://github.com/daseinlabs/open-jev) - Local one-pass option scoring server for Gemma on Apple Silicon using MLX.
- [OpenJev by zhihz](https://github.com/zhihz/openjev) - Local bilingual probability decisions from context, questions, and candidate answers. Independent research preview inspired by TypeSafe Jev.
- [openjev-sglang](https://github.com/ekzhang/openjev-sglang) - Jev-compatible API endpoint based on open models (prefill-only).
- [openJev-verdict-2.0](https://github.com/Heman10x-NGU/openJev-verdict-2.0) - Open 149.6M-parameter non-autoregressive decision model with calibrated outputs and a WebGPU playground.
- [OpenSourceJev](https://github.com/sabeel111/OpenSourceJev) - Local Qwen and llama.cpp decision engine for Jev-style typed judgments.
- [OpenThai-SystemOne](https://github.com/iapp-technology/openthai-systemone) - Thai and English System One model with a Jev-compatible typed decision API.
- [reflex](https://github.com/kshetrajna12/reflex) - Open re-creation of Jev on Qwen3.5 that returns typed decisions and calibrated probabilities.
- [Rizzo Flow](https://github.com/Rizzo-AI-Academy/rizzo-flow) - Local, open-source System One-style service with a Jev-compatible HTTP API backed by open model weights.
- [sarvam-jev](https://github.com/SAGAR-TAMANG/sarvam-jev) - Browser-based Jev-style inference engine for typed decisions on an Indic language model.
- [SemIf](https://github.com/TheoLeeCJ/SemIf-OpenJev) - Semantic ifs from open models, on a 3090 at home. Independent; not affiliated with Jev or TypeSafe.
- [Simple Jev](https://github.com/featherless-ai/simple-jev) - Turn any open model into a classifier/jev endpoint.
- [System One](https://github.com/sgoedecke/system-one) - Experimental local classifier that applies a System One-style single-pass decision interface to open models.
- [System One, open](https://github.com/mithalouni/system-one-open) - Open Gemma-based Jev replica with typed, calibrated decisions and a one-pass local API.
- [typesafe-local](https://github.com/aabolfazl/typesafe-local) - Local open-model experiment that returns probability distributions for typed questions without an API key.
- [Verdict-open-jev](https://github.com/Heman10x-NGU/Verdict-open-jev) - Open ModernBERT decision model with calibrated uncertainty, benchmark audits, and a WebGPU playground.
- [Von](https://github.com/wfzyx/von) - Open non-autoregressive System One decision model with calibrated discrete and ordinal inference.

## Benchmarks and evaluations

- [Cisco Skill Scanner System One Evaluations](https://github.com/cisco-ai-defense/skill-scanner) - Agent-skill security scanner with hosted Jev evaluation code and an optional advisory System One screen that leaves findings unchanged.
- [DeepEval TypeSafe integration](https://deepeval.com/integrations/models/typesafe-ai) - Experimental DeepEval integration routes supported metric verdicts, scores, and classifier labels to Jev.
- [DeepSearcher Jev Stopping Evaluation](https://github.com/zilliztech/deep-searcher/tree/master/evaluation/jev_stopping) - Evaluation of Jev and DeepSeek stopping strategies for multi-hop question answering.
- [Jev Benchmarks](https://github.com/AbdelStark/jev-benchmarks) - Benchmark suite that evaluates Jev on classification accuracy, calibration, risk coverage, resource use, and latency.
- [jev eval](https://github.com/4esv/jev-eval) - Benchmark TypeSafe Jev against any OpenRouter model on your own labelled classification data: accuracy, calibration, latency, cost.
- [Jev Eval Agent](https://github.com/vinilana/jev-eval-agent) - Agent evaluation harness comparing direct model tool selection with Jev-based routing.
- [jev phishing bench](https://github.com/anisselbd/jev-phishing-bench) - Jev (TypeSafe) vs Claude Haiku 4.5 on 2 000 phishing emails: accuracy, calibration, latency, cost. Reproducible benchmark.
- [Jev Reranker](https://github.com/hev/reranker) - Calibrated Jev reranker with a reproducible comparison against hosted rerankers and LLM judges.
- [jev research eval](https://github.com/jgridifier/jev-research-eval) - Reproducible Jev Ultrafast research-browser eval harness + field note (QC’d cases, suite runner, report generator). Not investment advice.
- [jev search rerank eval](https://github.com/zhuyansen/jev-search-rerank-eval) - Does a TypeSafe Jev rerank beat embedding search? Graded relevance eval (9,831 pairs, 164 zh/en queries) over the Agent Skills Hub catalog, with the judge-circularity bias measured.
- [jev sec bench](https://github.com/Gaurav-Gosain/jev-sec-bench) - Blind security benchmarks for Jev, TypeSafe's System One model: prompt injection and vulnerable code detection, built on jev-go.
- [jev spam eval](https://github.com/bitnovus/jev-spam-eval) - Zero-shot spam filtering with TypeSafe Jev Noul questions, compared with TF-IDF baselines.
- [JEV versus LLMs: Political Science Replications](https://arxiv.org/abs/2610.06625) - Independent evaluation of Jev accuracy, cost, speed, and probability calibration across seven political science replications.
- [jev-agent-failure-benchmark](https://github.com/TokenTrim/jev-agent-failure-benchmark) - Benchmarking Jev (Typesafe.ai) against a strong LLM on the Who&When Pro agent-failure-attribution benchmark (text subset).
- [jev-alpha-bench](https://github.com/Gaurav-Gosain/jev-alpha-bench) - Evaluation of Jev on financial-news and price-candle signals with reproducible event-level results.
- [jev-code-review-benchmark](https://github.com/gemanor/jev-code-review-benchmark) - Reproducible benchmark comparing Jev, Gemini Flash, and Claude Fable on Python code-review rules.
- [jev-measured](https://github.com/WallerChen/jev-measured) - Reproducible measurements of Jev API cost, latency, raw output, and accuracy across eight use cases.
- [jev-rerank-bench](https://github.com/anessbelbati/jev-rerank-bench) - Can a decision model beat dedicated rerankers? TypeSafe Jev vs Cohere Rerank 4 vs ZeroEntropy zerank-2 vs a chat-model baseline: 14 datasets, every raw API response, bootstrap ranges on every gap.
- [jevals](https://github.com/openlayer-ai/jevals) - Python toolkit for agent evaluation and guardrails with Jev, Kev, Laya, and chat-model backends.
- [jevcheck](https://github.com/sathariels/jevcheck) - Behavioral contract tests for Jev model upgrades that detect changed answers and confidence regressions, with baseline recording and replay.
- [jevcompat](https://github.com/mandu5/jevcompat) - Conformance spec, test runner, proxy, reference mock, and GitHub Action for Jev-compatible API servers.
- [JEVQA video-quality evaluation](https://arxiv.org/abs/2609.24395) - Preprint and public result data evaluating Jev for zero-shot video-quality prediction from metadata and codec features.
- [Openwork Jev Verification Dictionary](https://github.com/different-ai/openwork/blob/dev/evals/verification-dictionary.md) - Experimental evaluator that uses Jev to select author-defined checks before deterministic replay.
- [Phoenix Jev Evaluations](https://github.com/Arize-ai/phoenix/blob/main/js/packages/phoenix-evals/examples/typesafe_jev_example.ts) - Evaluation framework with a Jev hallucination evaluator example that compares labels, probabilities, and latency against a chat model.
- [pytest-jev](https://github.com/allebee/pytest-jev) - Pytest plugin that uses Jev probabilities to assert semantic properties of application outputs.
- [Taifoon Jev Grader](https://github.com/taifoon-io/jev) - Agent-job grader that combines deterministic checks with Jev rubric judgments and produces verifiable receipts with optional on-chain records.
- [Typed Evals](https://github.com/TrustifAI/typed_evals) - Python package and CLI for evaluating LLM, RAG, and agent outputs with Jev, optional calibration, and tool guards.
- [TypeSafe AI Benchmark](https://github.com/iammrduncan/typesafe-ai-benchmark) - This is a LLM Gateway that mimics typesafe ai structured output. Like an imposter Jev.
- [TypeSafe Workflow Evals](https://evals.typesafe.ai/) - Official workflow evaluations for Jev decision tasks.
- [World Monitor Jev Headline Evaluation](https://github.com/koala73/worldmonitor/tree/main/shared) - Experimental harness that scores news headlines against geopolitical threat levels and event categories.

## Examples and learning resources

- [Building with Jev](https://github.com/dbreunig/building-with-jev-skill) - Agent skill for designing, implementing, and diagnosing programs that call Jev.
- [GenAI Agents One-Step Decision Router](https://github.com/NirDiamant/GenAI_Agents) - Independent Jev-style tutorial that routes bank messages with Qwen first-token probabilities, measures calibration, and applies confidence gates.
- [Jev Experiments](https://github.com/dabit3/jev-experiments) - Collection of latency-focused TypeSafe Jev demos with separate app documentation and tests.
- [Jev for Engineers](https://github.com/Foadsf/jev-for-engineers) - Eight minimal working examples of TypeSafe's Jev (a System One model) applied to mechanical and electrical engineering: CAD/CAE/CAM routing, FEM result triage, DFM screening, BOM alignment, hallucination-proof extraction. Zero dependencies.
- [Jev playground](https://github.com/shivanathd/jev-playground) - Public BYOK playground demonstrating Jev decisions for agent gates, routing, review, and operator workflows.
- [Jev use cases](https://github.com/kenhuangus/jev-usecases) - Runnable Jev use-case harnesses that demonstrate typed decisions for software workflows.
- [json-render](https://github.com/vercel-labs/json-render) - Experimental Jev composition for choosing UI specifications from predefined components.
- [Learn Agent Architecture](https://github.com/hardness1020/learn-agent-architecture) - Learn Agent Architecture includes a runnable graph example that uses a Jev decision to route control flow.
- [MaxText Decision Models Tutorial](https://github.com/AI-Hypercomputer/maxtext/blob/main/docs/tutorials/decision_models.md) - Tutorial for independent Jev-style decision scoring on TPU with MaxText, vLLM, and Bespoke Nimble weights.
- [Pydantic AI + Jev examples](https://github.com/adtyavrdhn/pydantic-jev-examples) - Runnable Pydantic AI examples that use Jev for safety, routing, and game-state decisions.
- [TypeSafe AI StarCraft](https://github.com/phyous/tsai-sc) - TypeSafe Jev controls original StarCraft shareware through keyboard and mouse with recorded action probabilities.
- [TypeSafe Documentation and Cookbooks](https://docs.typesafe.ai/introduction/quickstart) - Official quickstarts, primitive guides, patterns, and Jev cookbooks.
- [TypeSafe Jev Examples](https://github.com/rajivkuriakose/typesafe-jev-examples) - Worked examples for TypeSafe's Jev System One decision model, runnable today through OpenRouter.
- [TypeSafe Playground](https://github.com/TypeSafeAI/typesafe-playground) - Community TypeSafe AI playground: 110 use cases, games, dilemmas and model challenges, with editable prompts, A/B comparisons and a mobile-friendly UI.

## Community resources

- [Jevify](https://github.com/altryne/jevify) - An agent skill to discover TypeSafe Jev opportunities, design typed questions, and learn from recent community experiments.
- [Learn Jev Tutorials](https://learnjev.com/tutorials) - Independent tutorials for Jev concepts, patterns, confidence, and reliability.
<!-- END GENERATED README RESOURCES -->

## Contributing

Contributions are welcome through pull requests. A submission must explain exactly how Jev is used and link to primary evidence.

This list is released under [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/).
