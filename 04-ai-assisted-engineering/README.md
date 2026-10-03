# Level 4 — AI-Assisted Software Engineering

> 🎯 **Target:** not *"AI helps me code"*, but **controlling an AI coding agent**. If your CV already lists OpenCode / [CC] / Kiro, now you level up from user to operator. Many roles explicitly want people comfortable using AI assistants/agents in a developer workflow.

---

## 📚 Learn

```
context engineering     prompt engineering      agent instructions
repository context      tool calling            MCP
subagents               verification            test-driven development
code review             diff review             plan mode
```

### Ideal workflow
```
AI Agent → Analyze repo → Plan → Implement → Run tests
   → Find failure → Fix → Run tests again → Review diff → Human approval
```

### Free sources
- [Building Effective Agents (Anthropic)](https://www.anthropic.com/engineering/building-effective-agents)
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/)
- [OpenCode Docs](https://opencode.ai/docs)
- [Prompt Engineering Overview (Anthropic)](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)

---

## 🧪 Exercise

Create the **`agent-workflow-lab`** repo:

- [ ] Write an `AGENTS.md` that governs how an agent works in that repo (conventions, test commands, prohibitions).
- [ ] Prepare a real task (e.g. add a small feature), then run the agent end-to-end: plan → implement → test → fix.
- [ ] Document each step + where the agent failed and why.
- [ ] Compare results with 2 different prompt approaches (little context vs complete context).
- [ ] Build 1 subagent / custom command (e.g. `review-diff`, `write-tests`).

### Context engineering drill
- Give the agent **too little** context → observe hallucination.
- Give it **precise** context (relevant files + tests) → observe accuracy.
- Write your findings in `docs/context-engineering.md`.

---

## 🐛 Bug Hunt

Ask the agent to fix a bug. Deliberately don't give it tests. Check:
- Does the patch actually fix the bug, or just mask the symptom?
- Are there regressions?
- Write a test that proves the patch is right/wrong.

---

## 🤖 AI Challenge

Design an "AI challenge" for yourself: hand a broken repo to the agent, ask it to fix it, then **you grade** the result (correctness, diff precision, test quality).

---

## 📝 Evaluation

Build an **AI diff evaluation rubric**:

| Criterion | Weight |
|-----------|--------|
| Fixes the root cause | 35% |
| No regressions | 25% |
| Test quality | 20% |
| Diff clarity | 10% |
| Efficiency/cleanliness | 10% |

Use it to grade 5 AI diffs. Save to `evaluation/diff-scores.md`.

---

## 🏆 Final Task

- [ ] `agent-workflow-lab` with `AGENTS.md` + custom command/subagent
- [ ] `docs/context-engineering.md` with real findings
- [ ] 5 AI diffs graded with the rubric
- [ ] Can explain when an agent fails and how to fix its context

---

## ✅ Level 4 pass checklist

- [ ] Understand the difference between prompt vs context engineering
- [ ] Can write an effective `AGENTS.md`
- [ ] Understand how tool calling & MCP work
- [ ] Always verify agent output with tests, never trust blindly
- [ ] Can measure AI diff quality systematically
