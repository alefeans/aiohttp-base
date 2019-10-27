async def test_redirect_root_url(cli):
    resp = await cli.get('/')
    assert resp.status == 200
    text = await resp.json()
    assert "I'm fine and you ?" in text.get('message')


async def test_healthcheck_endpoint(cli):
    resp = await cli.get('/healthcheck')
    assert resp.status == 200
    text = await resp.json()
    assert "I'm fine and you ?" in text.get('message')
