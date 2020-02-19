from finance_blog.views import sanity_check


def test_sanity_check(rf):
    # `rf` = pytest-django RequestFactory
    request = rf.get("/sanity")
    response = sanity_check(request)
    assert response.status_code == 200
    assert response.content == (b"Congratulations, application installed successfully!")
