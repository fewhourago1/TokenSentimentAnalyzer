# Token Sentiment Analyzer 📊

## The Problem

Crypto sentiment is scattered across Twitter, Reddit, Telegram, and dozens of news sites. By the time you manually gauge the mood, the market has already moved. Worse, centralized sentiment tools can be gamed or go offline.

## The Solution

An on-chain Intelligent Contract that takes any token name, searches the web for real-time sentiment data, and produces a verified sentiment score through decentralized AI consensus.

**Input:** A token name (e.g., "Bitcoin", "Solana", "PEPE")  
**Output:** Sentiment classification + confidence score + social buzz level

## How To Use

**Step 1:** Deploy the contract on GenLayer Studio with your target token

```
Constructor Input: token_name = "Bitcoin"
```

**Step 2:** Call the `analyze_sentiment` method

**Step 3:** Read the result from contract state

```json
{
  "sentiment": "POSITIVE",
  "confidence": "78",
  "social_buzz": "HIGH",
  "summary": "Bitcoin sentiment positive as institutional accumulation continues."
}
```

## Understanding the Output

**Sentiment Scale:**
- `VERY_NEGATIVE` — Capitulation, extreme fear, panic
- `NEGATIVE` — Bearish mood, concern
- `NEUTRAL` — Mixed, indecisive
- `POSITIVE` — Optimistic, accumulation signals
- `VERY_POSITIVE` — Euphoria, potential top warning

**Social Buzz:** LOW → MEDIUM → HIGH → VIRAL

**Confidence:** 0-100, how confident the AI is in its assessment

## Technical Notes

- Contract searches Google dynamically for the token name
- AI analyzes search results for sentiment signals
- Multiple validators must agree via `gl.eq_principle.strict_eq`
- Works for literally any token — BTC, ETH, memecoins, anything

## Built On

GenLayer Testnet Bradbury | Python GenVM SDK | MIT License
