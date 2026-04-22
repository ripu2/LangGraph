from agent.root_finder.graph import build_graph
from app.schemas.roots_schema import RootRequest, RootResponse
from app.logger import setup_logger

logger = setup_logger(__name__)


class RootsController:
    def __init__(self):
        self.graph = build_graph()
        logger.debug("RootController initialized with compiled graph")

    def find_roots(self, request: RootRequest):
        input_state = {"a": request.a, "b": request.b, "c": request.c}
        logger.info("Invoking agent graph | input_state=%s", input_state)
        try:
            result = self.graph.invoke(input_state)
            logger.info("Agent graph completed | result=%s", result)
            root1 = result.get("root1", None)
            root2 = result.get("root2", None)
            return RootResponse(
                root1=str(root1) if isinstance(root1, complex) else root1,
                root2=str(root2) if isinstance(root2, complex) else root2,
            )
        except Exception as exc:
            logger.error("Error finding roots | error=%s", str(exc), exc_info=True)
            raise
