from agent.iterative_agent.graph import IterativeAgentGraph
from app.schemas.tweet_schema import TweetRequest


class TweetController:
    def __init__(self):
        self.graph = IterativeAgentGraph().build_graph()

    def generate_tweet(self, request: TweetRequest) -> str:
        input_state = {"topic": request.topic}
        result = self.graph.invoke(input_state)
        return result
