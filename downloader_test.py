from downloader import URL, get_url_list


def test_source():
    chapters = get_url_list(URL.format('361'))
    assert len(chapters) > 0
