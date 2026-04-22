from langgraph.graph.state import StateGraph

from agent.iterative_agent.state import TweetState
from agent.iterative_agent.node import (
    generate_tweet,
    evaluate_tweet,
    optimize_tweet,
    route_by_evaluation,
    route_after_generate,
)
from app.logger import setup_logger


logger = setup_logger(__name__)


class IterativeAgentGraph:

    def build_graph(self):
        graph = StateGraph(TweetState)
        graph.add_node("generate_tweet", generate_tweet)
        logger.debug("Added node: generate_tweet")
        graph.add_node("evaluate_tweet", evaluate_tweet)
        logger.debug("Added node: evaluate_tweet")
        graph.add_node("optimize_tweet", optimize_tweet)
        logger.debug("Added node: optimize_tweet")

        graph.set_entry_point("generate_tweet")
        logger.debug("Set entry point: generate_tweet")

        graph.add_conditional_edges("generate_tweet", route_after_generate)
        logger.debug("Added conditional edges: generate_tweet -> route_after_generate")

        graph.add_conditional_edges("evaluate_tweet", route_by_evaluation)
        logger.debug("Added conditional edges: evaluate_tweet -> route_by_evaluation")

        graph.add_edge("optimize_tweet", "evaluate_tweet")
        logger.debug("Added Iterative edge: optimize_tweet -> evaluate_tweet")

        graph.set_finish_point("evaluate_tweet")
        logger.debug("Set finish point: evaluate_tweet")

        compiled = graph.compile()
        logger.debug("Compiled graph: %s", compiled)
        return compiled
