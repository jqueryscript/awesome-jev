# Jev Resource List

Meta title: Jev Resource List: SDKs, Agents, MCP Servers, and More

Meta description: Browse verified Jev SDKs, MCP servers, agents, integrations, examples, benchmarks, and open System One implementations for developers.

WordPress excerpt: Find official Jev documentation, SDKs, gateways, MCP servers, agents, applications, benchmarks, examples, and independent System One implementations in one maintained developer resource for practical software workflows.

Recommended slug: jev-resource-list

*Last updated: September 20, 2026.*

This Jev Resource List collects official TypeSafe material and public projects that use Jev for typed decisions inside software. You can find SDKs, API gateways, MCP servers, agent tools, browser automation, applications, evaluations, examples, and independent System One implementations.

Jev is TypeSafe AI's first public System One Model. It receives application state and predefined questions, then returns typed answers with probability and confidence information. The public API supports Choice, Score, and Noul questions for tasks such as classification, routing, ranking, scoring, screening, and action selection.

The collection separates TypeSafe resources, software that calls the hosted Jev model, and independent projects that implement a similar decision interface. Project links point to canonical documentation, repositories, model pages, or services verified on September 20, 2026.

<!-- BEGIN GENERATED ARTICLE RESOURCES -->
## Official Jev resources

- **[Introducing System One Models and Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev)**: The article explains Jev's typed probabilistic decisions, model design, evaluations, and early-access release.
- **[TypeSafe AI](https://typesafe.ai/)**: The site introduces Jev, access paths, decision primitives, and current product information.
- **[TypeSafe System One API Reference](https://docs.typesafe.ai/api)**: The reference defines Jev request fields, typed questions, answers, errors, and model access.

## SDKs and API clients

- **[System One Adapter for Python](https://github.com/typesafe-ai/system-one-adapter-python)**: The adapter provides one decision interface for Jev and supported LLM comparison runs.
- **[TypeSafe JavaScript and TypeScript SDK](https://github.com/typesafe-ai/typesafe-sdk-js)**: The SDK sends typed Jev questions and exposes inferred structured answer types.
- **[TypeSafe Python SDK](https://github.com/typesafe-ai/typesafe-sdk-python)**: The SDK calls Jev with state and typed questions and returns structured answers.

## Gateways and integrations

- **[Jev on Cloudflare Workers AI](https://developers.cloudflare.com/ai/models/typesafe/jev/)**: Workers AI accepts shared state and typed questions for Jev evaluation requests.
- **[Jev on Netlify AI Gateway](https://docs.netlify.com/build/ai-gateway/overview/)**: The gateway routes Jev model requests and supplies gateway credentials to deployed functions.
- **[Jev on Vercel AI Gateway](https://vercel.com/ai-gateway/models/jev)**: The gateway runs Jev evaluations through AI SDK's experimental evaluate interface.
- **[Pydantic AI TypeSafeModel](https://pydantic.dev/docs/ai/models/typesafe/)**: The adapter maps Pydantic output fields into Jev questions and thresholded typed answers.
- **[TypeSafe Jev on OpenRouter](https://openrouter.ai/typesafe)**: OpenRouter exposes Jev model IDs through its dedicated decisions endpoint.

## Agent tools and MCP servers

- **[fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction)**: Jev scores tool calls and results to keep, truncate, or remove during context compaction.
- **[jev-guard](https://github.com/leepokai/jev-guard)**: Jev scores tool-call risk and screens returned content for prompt injection.
- **[jev-mcp by jkudish](https://github.com/jkudish/jev-mcp)**: Jev supplies typed judgments for verify, screen, find, rerank, classify, decide, and review tools.
- **[jev-router](https://github.com/gargpratyush/jev-router)**: Jev selects a model tier for each new coding-agent turn.
- **[jevwire](https://github.com/Brainwires/jevwire)**: Jev gates, escalates, or steers coding-agent actions through typed policy decisions.
- **[TypeSafe Agent Skills](https://github.com/typesafe-ai/skills)**: The skills teach agents to formulate Jev state, typed questions, thresholds, and evaluations.
- **[typesafe-mcp](https://github.com/itsmostafa/typesafe-mcp)**: Jev evaluates Choice, Score, and Noul questions through TypeSafe or OpenRouter.

## Browser and computer-use agents

- **[Jev Browser](https://github.com/jkudish/jev-browser)**: Jev selects browser actions and reports confidence, progress, and stuck state.
- **[Jev Ultrafast](https://github.com/browser-use/jev-ultrafast)**: Jev chooses the browser operation and target element while a smaller model handles text.

## Applications and developer tools

- **[Foreman](https://github.com/thruwire/foreman)**: Jev selects and supervises bounded actions across a software production workflow.
- **[Jev Logs](https://jevlogs.com)**: Jev scores log usefulness and directs records to annotation, archival, or deeper analysis.
- **[Jev Search](https://github.com/superagents-lab/jev-search)**: Jev interprets queries, selects sources, and scores result relevance.
- **[pg-jev](https://github.com/realZachi/pg-jev)**: Jev judges table rows through Noul, Choice, and Score questions called from SQL.
- **[skillranker](https://github.com/Dicklesworthstone/skillranker)**: Jev scores candidate skills and supports abstention before an agent selects its next capability.
- **[Stanley](https://github.com/devagrawal09/stanley-code)**: Jev routes requests and checks changes, tests, security, performance, and compatibility.
- **[Tax Document Classifier](https://github.com/kyotofin/tax-doc-classifier)**: Jev assigns IRS form categories from page text and confidence-aware rules.

## Open System One implementations

- **[jevmlx](https://github.com/bnsd55/jevmlx)**: The runtime produces batched schema-valid decisions over booleans, enums, and multi-select fields.
- **[Kev](https://github.com/jaredpalmer/kev)**: Kev trains and runs typed decision tasks on local hardware.
- **[LocalJev](https://github.com/githubnext/localjev)**: The server translates typed questions into local model classifications and returns Jev-compatible responses.
- **[NanoJev](https://github.com/TianyuCodings/NanoJev)**: NanoJev maps state and dynamic candidates to probability distributions without text decoding.
- **[OpenJev](https://github.com/razorback16/openjev)**: OpenJev returns typed probabilities and confidence from open DiffusionGemma models.
- **[SemIf](https://github.com/TheoLeeCJ/SemIf)**: SemIf produces option probabilities from open models without autoregressive decoding.
- **[Simple Jev](https://github.com/featherless-ai/simple-jev)**: The server reads next-token logits and constructs Choice, Score, and truth judgments.

## Benchmarks and evaluations

- **[jev-agent-failure-benchmark](https://github.com/TokenTrim/jev-agent-failure-benchmark)**: Jev predicts structured failure categories for comparison with published LLM baselines.
- **[jev-benchmarks](https://github.com/AbdelStark/jev-benchmarks)**: Jev produces probability distributions for classification, calibration, and abstention analysis.
- **[jev-rerank-bench](https://github.com/anessbelbati/jev-rerank-bench)**: Jev scores candidate relevance through typed questions across eight English datasets.
- **[TypeSafe Workflow Evals](https://evals.typesafe.ai/)**: Jev answers typed questions inside security, observability, invoice, and customer-service workflows.

## Examples and learning resources

- **[Jev for Engineers](https://github.com/Foadsf/jev-for-engineers)**: Jev supplies Choice, Score, and Noul judgments for eight engineering examples.
- **[TypeSafe Documentation and Cookbooks](https://docs.typesafe.ai/introduction/quickstart)**: The documentation demonstrates typed decisions, batching, routing, scoring, confidence, and agent integration.
- **[TypeSafe Jev Examples](https://github.com/rajivkuriakose/typesafe-jev-examples)**: Jev applies typed questions to support classification and search-result reranking.
- **[TypeSafe Playground](https://github.com/TypeSafeAI/typesafe-playground)**: Jev drives typed decisions across a collection of interactive experiments.

## Community resources

- **[Awesome Jev by TypeSafe](https://github.com/valentynkit/awesome-jev-typesafe)**: The directory groups projects using Jev for decisions, routing, ranking, verification, and guardrails.
- **[Jevify](https://github.com/altryne/jevify)**: The skill guides agents through Choice, Score, Noul, threshold, and evaluation design.
- **[Learn Jev Tutorials](https://learnjev.com/tutorials)**: The tutorials teach typed decision design with cURL, Python, and TypeScript examples.
<!-- END GENERATED ARTICLE RESOURCES -->

## How to choose a Jev resource

Start with the official documentation and one official SDK if you have direct TypeSafe access. The API reference defines the request and response contract, while the JavaScript and Python clients handle authentication, request construction, and typed answers.

A gateway integration supplies another access path. Check the gateway's current model ID, endpoint shape, authentication flow, limits, and billing before adapting an example. Gateway access can differ from the direct TypeSafe endpoint even when both services expose the same Jev model.

MCP servers and Agent Skills fit coding tools that need Jev as a callable judgment layer. Review each server's tool descriptions and policy thresholds before connecting it to file, shell, browser, or account actions. A probability supports a policy decision; it does not replace authorization, validation, or human review for consequential actions.

Browser agents and developer applications show concrete decision loops. These projects reveal what state they send, which choices Jev receives, and how software acts on the response. That information matters more than a repository name or a passing Jev mention.

Independent System One implementations do not run the TypeSafe model. They use open models, local runtimes, training pipelines, or compatible wire formats to explore the same typed-decision pattern. Compare their calibration, latency, hardware requirements, supported schemas, and evaluation methods before treating them as interchangeable.

Benchmarks need the same scrutiny as software. Check the dataset, split, sample size, model version, baselines, number of runs, committed outputs, and stated limitations. Vendor evaluations describe TypeSafe's own results. Community evaluations provide separate evidence when their methods and artifacts are reproducible.

## Jev resource FAQ

### What is Jev used for?

Jev is designed for bounded software decisions. Common tasks include selecting one label from a known set, scoring an item against an ordered rubric, estimating support for a yes-or-no statement, choosing an agent tool, ranking candidates, and screening content before another action runs.

### Does Jev generate text?

Jev returns typed answers and probability information for questions defined by the application. Text generation remains a separate step when a workflow needs prose, code, or another open-ended output.

### Are OpenJev projects official TypeSafe releases?

The open implementations in this directory are independent community projects. Their model weights, training methods, probability calculations, performance, and hardware requirements differ from TypeSafe Jev. Each entry links to the project's own technical material.

### Can an agent trust a high Jev confidence score automatically?

Confidence thresholds belong to the application's policy and evaluation data. Test the complete workflow against representative inputs, add an abstention or review path, and keep security and authorization checks outside the model decision.

### Which Jev resource is the best starting point?

Read the TypeSafe quickstart and API reference, then use the official SDK for your language. The examples and cookbooks show how to define state and typed questions. Agent, browser, and open-model projects make more sense after that interface is clear.

## Related resources

- [The Ultimate Claude Code Resource List 2026: Agents, Skills, Plugins & More](https://www.scriptbyai.com/claude-code-resource-list/)
- [The Ultimate Codex Resource List 2026: Skills, Plugins, MCP, SDKs & More](https://www.scriptbyai.com/codex-resource-list/)
- [agent-browser: Free Open-Source Browser Automation CLI for AI Agents](https://www.scriptbyai.com/agent-browser-automation-cli/)
- [Agent Skills Specification: SKILL.md Format, Fields, and Directory Structure](https://www.scriptbyai.com/agent-skills-specification/)
