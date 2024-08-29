import pytest
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from notice_board.models import Ad, Comment
from notice_board.serializers import AdDetailSerializer, AdSerializer, CommentSerializer


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user(api_client):
    User = get_user_model()
    user = User.objects.create_user(email='test@example.com', password='password')
    return user


@pytest.fixture
def authenticated_client(api_client, user):
    api_client.force_authenticate(user=user)
    return api_client


@pytest.fixture
def ad(user):
    return Ad.objects.create(title='Test Ad', description='Test Description', author=user)


@pytest.fixture
def comment(user, ad):
    return Comment.objects.create(text='Test Comment', author=user, ad=ad)


@pytest.mark.django_db
def test_retrieve_comment(authenticated_client, comment):
    print(f"Ad ID: {comment.ad.id}, Comment ID: {comment.id}")
    url = f'/api/ads/{comment.ad.id}/comments/{comment.id}/'
    print(f"Requesting URL: {url}")

    response = authenticated_client.get(url)
    print(f"Response Status Code: {response.status_code}")

    assert response.status_code == status.HTTP_200_OK
    assert response.data['text'] == comment.text


@pytest.mark.django_db
def test_update_comment(authenticated_client, comment):
    url = f'/api/ads/{comment.ad.id}/comments/{comment.id}/'
    data = {'text': 'Updated Comment'}
    response = authenticated_client.patch(url, data, format='json')
    assert response.status_code == status.HTTP_200_OK
    comment.refresh_from_db()
    assert comment.text == 'Updated Comment'


@pytest.mark.django_db
def test_delete_comment(authenticated_client, comment):
    url = f'/api/ads/{comment.ad.id}/comments/{comment.id}/'
    response = authenticated_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Comment.objects.count() == 0


@pytest.mark.django_db
def test_create_ad(authenticated_client):
    url = '/api/ads/create/'
    data = {
        'title': 'New Ad',
        'description': 'New Description'
    }
    response = authenticated_client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert Ad.objects.count() == 1
    assert Ad.objects.get().title == 'New Ad'


@pytest.mark.django_db
def test_list_ads(authenticated_client, ad):
    url = '/api/ads/'
    response = authenticated_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]['title'] == ad.title


@pytest.mark.django_db
def test_retrieve_ad(authenticated_client, ad):
    url = f'/api/ads/{ad.id}/'
    response = authenticated_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['title'] == ad.title


@pytest.mark.django_db
def test_update_ad(authenticated_client, ad):
    url = f'/api/ads/{ad.id}/update/'
    data = {
        'title': 'Update Ad',
        'description': 'Update Description'
    }
    response = authenticated_client.patch(url, data, format='json')
    assert response.status_code == status.HTTP_200_OK
    ad.refresh_from_db()
    assert ad.title == 'Update Ad'


@pytest.mark.django_db
def test_delete_ad(authenticated_client, ad):
    url = f'/api/ads/{ad.id}/delete/'
    response = authenticated_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Ad.objects.count() == 0


@pytest.mark.django_db
def test_create_comment(authenticated_client, ad):
    url = f'/api/ads/{ad.id}/comments/'
    data = {
        'text': 'New Comment'
    }
    response = authenticated_client.post(url, data, format='json')
    print(response.data)
    assert response.status_code == status.HTTP_201_CREATED
    assert Comment.objects.count() == 1
    assert Comment.objects.get().text == 'New Comment'


@pytest.mark.django_db
def test_list_comments(authenticated_client, comment):
    url = f'/api/ads/{comment.ad.id}/comments/'
    response = authenticated_client.get(url)
    print(response.data)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]['text'] == comment.text
