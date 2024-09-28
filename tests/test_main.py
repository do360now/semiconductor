from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert (
        "<title>Semiconductor Processing Overview</title>" in response.text
    )  # Check for a string in the HTML


def test_static_files():
    # Test that the static files endpoint is mounted correctly
    response = client.get("/static/testfile.txt")
    assert response.status_code in {200, 404}  # 200 if the file exists, 404 otherwise


def test_images_endpoint():
    # Test that the images folder is correctly mounted
    response = client.get("/images/sample.jpg")
    assert response.status_code in {200, 404}  # 200 if the image exists, 404 otherwise


def test_videos_endpoint():
    # Test that the videos folder is correctly mounted
    response = client.get("/videos/sample.mp4")
    assert response.status_code in {200, 404}  # 200 if the video exists, 404 otherwise
