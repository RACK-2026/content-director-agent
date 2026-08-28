from .models import Brief, Review, Script


def create_script(brief: Brief) -> Script:
    """Create a deterministic baseline script from a generic creative brief."""
    hook = f"你是否也在寻找更简单的{brief.topic}方法？"
    body = [
        f"面向{brief.audience}，先说明他们最常遇到的一个具体问题。",
        f"用一个可验证的小步骤介绍解决思路，并保持{brief.tone}的表达。",
        f"围绕“{brief.goal}”给出一个可执行的示例。",
    ]
    return Script(hook=hook, body=body, call_to_action="欢迎留言分享你的做法。")


def review_script(script: Script) -> Review:
    """Review a script with transparent, reusable quality checks."""
    strengths: list[str] = []
    issues: list[str] = []
    if script.hook.strip().endswith("？"):
        strengths.append("开头有明确问题引导")
    else:
        issues.append("开头缺少清晰的注意力抓手")
    if len(script.body) >= 3:
        strengths.append("主体包含问题、方法和示例")
    else:
        issues.append("主体信息不足，缺少完整展开")
    if script.call_to_action.strip():
        strengths.append("结尾包含下一步行动")
    else:
        issues.append("结尾缺少行动引导")
    score = max(0, min(100, 60 + len(strengths) * 13 - len(issues) * 10))
    plan = tuple(f"优先处理：{issue}" for issue in issues)
    return Review(score=score, strengths=tuple(strengths), issues=tuple(issues), revision_plan=plan)


def revise_script(script: Script, review: Review) -> Script:
    """Apply safe, generic revisions without changing the topic or inventing facts."""
    notes = list(script.notes)
    hook = script.hook if "开头缺少" not in " ".join(review.issues) else f"先别急着处理{script.hook.rstrip('？')}，试试这个思路。"
    cta = script.call_to_action or "如果这个方法有帮助，可以收藏并分享你的反馈。"
    if review.issues:
        notes.extend(review.revision_plan)
    return Script(hook=hook, body=list(script.body), call_to_action=cta, notes=notes)


