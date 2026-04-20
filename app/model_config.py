from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class ChatModelConfig:
    model: str
    temperature: float

    def to_kwargs(self) -> dict[str, object]:
        return asdict(self)


class ModelConfig:
    natural = ChatModelConfig(model="gpt-4.1", temperature=1.2)


model_config = ModelConfig()
