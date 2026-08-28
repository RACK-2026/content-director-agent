from .models import Brief
from .workflow import create_script, review_script, revise_script


def main() -> None:
    brief = Brief(topic="学习新技能", audience="希望提升效率的人", goal="给出一个容易开始的行动")
    script = create_script(brief)
    review = review_script(script)
    revised = revise_script(script, review)
    print(revised.as_text())
    print(f"\nReview score: {review.score}/100")


if __name__ == "__main__":
    main()


