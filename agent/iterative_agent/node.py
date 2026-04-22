from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import END
from agent.iterative_agent.state import TweetState
from agent.prompts.prompts import Prompts
from app.logger import setup_logger
from app.model_config import model_config
from app.schemas.tweet_schema import TweetResponse

_generatorModel = ChatOpenAI(**model_config.generator.to_kwargs())
_evaluatorModel = ChatOpenAI(**model_config.evaluator.to_kwargs())
_optimizerModel = ChatOpenAI(**model_config.optimizer.to_kwargs())

_structuredEvaluatorModel = _evaluatorModel.with_structured_output(TweetResponse)


logger = setup_logger(__name__)


def generate_tweet(state: TweetState) -> TweetState:
    logger.info("[Node: generate_tweet] Executing")
    topic = state["topic"]
    message = [
        SystemMessage(content=Prompts.tweet_generation),
        HumanMessage(content=f"Generate a tweet about: {topic}"),
    ]
    response = _generatorModel.invoke(message)
    tweet = response.content
    logger.debug("[Node: generate_tweet] Tweet: %s", tweet)
    state["iteration_count"] = 0
    state["MAX_ITERATIONS"] = 3
    return {
        "tweet": tweet,
        "iteration_count": state["iteration_count"],
        "MAX_ITERATIONS": state["MAX_ITERATIONS"],
    }


def evaluate_tweet(state: TweetState) -> TweetState:
    logger.info("[Node: evaluate_tweet] Executing")
    tweet = state["tweet"]
    message = [
        SystemMessage(content=Prompts.evaluate_tweet),
        HumanMessage(content=f"Evaluate the following tweet: {tweet}"),
    ]
    response = _structuredEvaluatorModel.invoke(message)
    logger.debug("[Node: evaluate_tweet] Evaluation: %s", response)
    return {"evaluation": response.evaluation, "feedback": response.feedback}


def optimize_tweet(state: TweetState) -> TweetState:
    logger.info("[Node: optimize_tweet] Executing")
    tweet = state["tweet"]
    feedback = state["feedback"]
    message = [
        SystemMessage(content=Prompts.optimize_tweet),
        HumanMessage(
            content=f"Optimize the following tweet: {tweet} with the following feedback: {feedback}"
        ),
    ]
    response = _optimizerModel.invoke(message)
    optimized_tweet = response.content
    state["iteration_count"] += 1
    logger.debug("[Node: optimize_tweet] Optimized tweet: %s", optimized_tweet)
    return {"tweet": optimized_tweet, "iteration_count": state["iteration_count"]}


REFUSAL_MARKERS = ("i'm sorry", "i am sorry", "can't assist", "cannot assist", "unable to help")


def _is_refusal(text: str) -> bool:
    lowered = text.lower()
    return any(marker in lowered for marker in REFUSAL_MARKERS)


def route_after_generate(state: TweetState) -> str:
    if _is_refusal(state["tweet"]):
        logger.info("[Router: route_after_generate] Refusal detected, ending graph")
        return END
    return "evaluate_tweet"


def route_by_evaluation(state: TweetState) -> str:
    evaluation = state["evaluation"]
    if evaluation == "positive" or state["iteration_count"] >= state["MAX_ITERATIONS"]:
        return END
    return "optimize_tweet"
