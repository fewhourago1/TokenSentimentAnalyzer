# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }

from genlayer import *

import json
import typing


class TokenSentimentAnalyzer(gl.Contract):
    has_scanned: bool
    sentiment: str
    confidence: str
    analysis: str
    token_name: str

    def __init__(self, token_name: str):
        self.has_scanned = False
        self.sentiment = "NEUTRAL"
        self.confidence = "0"
        self.analysis = "Awaiting scan"
        self.token_name = token_name

    @gl.public.write
    def analyze_sentiment(self) -> typing.Any:

        if self.has_scanned:
            return "Already scanned"

        def nondet() -> str:
            response = gl.nondet.web.render("https://www.coingecko.com/en/coins/bitcoin", mode="text")
            print(response)

            task = f"""You are a crypto sentiment analyst.
            Analyze the sentiment for Bitcoin based on this data:
            {response[:2000]}

            Respond with the following JSON format:
            {{
                "sentiment": str,
                "confidence": str,
                "social_buzz": str,
                "summary": str
            }}
            sentiment: one of VERY_NEGATIVE, NEGATIVE, NEUTRAL, POSITIVE, VERY_POSITIVE.
            confidence: 0-100 as string indicating how confident you are.
            social_buzz: one of LOW, MEDIUM, HIGH, VIRAL.
            summary: one sentence about current sentiment for this token.
            It is mandatory that you respond only using the JSON format above,
            nothing else. Don't include any other words or characters,
            your output must be only JSON without any formatting prefix or suffix.
            This result should be perfectly parsable by a JSON parser without errors.
            """
            result = gl.nondet.exec_prompt(task).replace("```json", "").replace("```", "")
            print(result)
            return json.dumps(json.loads(result), sort_keys=True)

        result_json = json.loads(gl.eq_principle.strict_eq(nondet))

        self.has_scanned = True
        self.sentiment = result_json["sentiment"]
        self.confidence = str(result_json["confidence"])
        self.analysis = result_json["summary"]

        return result_json
