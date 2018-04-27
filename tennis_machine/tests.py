def _test_url(url):
    assert url is not None, 'There was no url'
    assert url != '', 'There was no url'

def _test_response(response, status_code):
    assert response is not None
    assert status_code == 200, 'Connection error'