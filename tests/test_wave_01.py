from operator import contains
from app.models.video import Video
from app.models.customer import Customer

VIDEO_TITLE = "A Brand New Video"
VIDEO_ID = 1
VIDEO_INVENTORY = 1
VIDEO_RELEASE_DATE = "01-01-2001"

CUSTOMER_NAME = "A Brand New Customer"
CUSTOMER_ID = 1
CUSTOMER_POSTAL_CODE = "12345"
CUSTOMER_PHONE = "123-123-1234"

# --------------------------------
# ----------- VIDEOS -------------
# --------------------------------

# READ
def test_get_videos_no_saved_videos(client):
    # Act
    response = client.get("/videos")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_videos_one_saved_video(client, one_video):
    # Act
    response = client.get("/videos")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(response_body) == 1
    assert response_body[0]["title"] == VIDEO_TITLE
    assert response_body[0]["id"] == VIDEO_ID
    assert response_body[0]["total_inventory"] == VIDEO_INVENTORY

def test_get_video(client, one_video):
    # Act
    response = client.get("/videos/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body["title"] == VIDEO_TITLE
    assert response_body["id"] == VIDEO_ID
    assert response_body["total_inventory"] == VIDEO_INVENTORY

def test_get_video_not_found(client):
    # Act
    response = client.get("/videos/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {"message": "Video 1 was not found"}

def test_get_invalid_video_id(client, one_video):
    # Act
    response = client.get("/videos/hello")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400








