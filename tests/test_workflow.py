from content_director import Brief, create_script, revise_script, review_script


def test_brief_to_script_review_round_trip():
    script = create_script(Brief(topic="时间管理", audience="初学者", goal="完成一个小行动"))
    review = review_script(script)
    revised = revise_script(script, review)

    assert script.hook
    assert review.score >= 0
    assert "CTA:" in revised.as_text()


def test_review_explains_missing_cta():
    script = create_script(Brief(topic="阅读", audience="学生", goal="建立习惯"))
    script.call_to_action = ""
    review = review_script(script)

    assert any("行动引导" in issue for issue in review.issues)
    assert review.revision_plan


