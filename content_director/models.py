from dataclasses import dataclass, field


@dataclass(frozen=True)
class Brief:
    topic: str
    audience: str
    goal: str
    duration_seconds: int = 30
    tone: str = "clear and natural"


@dataclass
class Script:
    hook: str
    body: list[str]
    call_to_action: str
    notes: list[str] = field(default_factory=list)

    def as_text(self) -> str:
        sections = [f"Hook: {self.hook}", *self.body, f"CTA: {self.call_to_action}"]
        return "\n".join(sections)


@dataclass(frozen=True)
class Review:
    score: int
    strengths: tuple[str, ...]
    issues: tuple[str, ...]
    revision_plan: tuple[str, ...]


