from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai.chat_models import ChatOpenAI
from agent.blog_agent.state import BlogState
from agent.prompts.prompts import Prompts
from app.logger import setup_logger
from app.model_config import model_config


logger = setup_logger(__name__)
_model = ChatOpenAI(**model_config.natural.to_kwargs())


def generate_outline(state: BlogState) -> BlogState:
    logger.info("[Node: generate_outline] Executing")
    title = state["title"]

    message = [
        SystemMessage(content=Prompts.generate_outline),
        HumanMessage(content=f"Generate an outline for a blog post about: {title}"),
    ]

    response = _model.invoke(message)
    outline = response.content
    logger.debug("[Node: generate_outline] Outline: %s", outline)
    return {"outline": outline}


def generate_content(state: BlogState) -> BlogState:
    logger.info("[Node: generate_content] Executing")
    outline = state["outline"]
    title = state["title"]
    messages = [
        SystemMessage(content=Prompts.generate_content),
        HumanMessage(
            content=f"Please generate the content for a blog post about: {title} and the outline is: {outline}"
        ),
    ]
    response = _model.invoke(messages)
    content = response.content
    logger.debug("[Node: generate_content] Content: %s", content)
    return {"content": content}
