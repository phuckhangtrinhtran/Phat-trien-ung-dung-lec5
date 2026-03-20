def test_auth_fail(client):
    response = client.get(
        "/todos",
        headers={"Authorization": "Bearer sai_token"}
    )
    assert response.status_code == 401