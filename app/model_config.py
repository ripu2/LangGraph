from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class ChatModelConfig:
    model: str
    temperature: float

    def to_kwargs(self) -> dict[str, object]:
        return asdict(self)


class ModelConfig:
    natural = ChatModelConfig(model="gpt-4.1", temperature=0.5)
    generator = ChatModelConfig(model="gpt-4o", temperature=0.5)
    evaluator = ChatModelConfig(model="gpt-4o-mini", temperature=0)
    optimizer = ChatModelConfig(model="gpt-4o", temperature=0.5)


model_config = ModelConfig()
