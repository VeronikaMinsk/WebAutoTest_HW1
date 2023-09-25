import requests
import yaml

with open('config.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)

S = requests.Session()

def test_step1(user_login, post_title):
    post_data = {
        'title': data['title_new'],
        'description': data['description_new'],
        'content': data['content_new']
    }
    result_post = S.post(url=data['address'], headers={'X-Auth-Token': user_login}, params=post_data)
    created_post = result_post.json()
    created_title = created_post.get('title')
    assert created_title == post_title, 'Created post has incorrect title'

    result_get = S.get(url=data['address'], headers={'X-Auth-Token': user_login}, params=post_data)
    all_posts = result_get.json()['data']
    assert any(post['title'] == created_title for post in all_posts), 'Created post not found'




