import requests
import json
from .models import DailyImage

app_id = "db91e8d5fd9279b3e8ce22a101b760cc32efef87d5f6b6a29fb2c79f3f5561da"

def get_image():
    resp = requests.get("https://api.unsplash.com/photos/random/?client_id=" + app_id)
    if resp.status_code != 200:
        raise ApiError('Get /photos/ {}'.format(resp.status_code))
    r = resp.json()
    name = r['user']['name']
    image = r['urls']['full']
    if r['location']['city'] is None:
        location = r['location']['country']
    else:
        location = "{}, {}".format(r['location']['city'], r['location']['country'])
    x = [name, image, location]
    return x

def new_daily_image():
    new_image = DailyImage()
    fetch_image = get_image()
    new_image.name = fetch_image[0]
    new_image.image = fetch_image[1]
    new_image.location = fetch_image[2]
    new_image.save()


""" json format:
{
'likes': 63,
'height': 4000,
'user': {
    'name': 'Raphael Schaller',
    'total_likes': 13,
    'last_name': 'Schaller',
    'total_collections': 2,
    'username': 'isumaki',
    'bio': '',
    'id': 'SYccbNfj6-w',
    'portfolio_url': 'http://raphaelphoto.ch',
    'links': {
        'likes': 'https://api.unsplash.com/users/isumaki/likes',
        'photos': 'https://api.unsplash.com/users/isumaki/photos',
        'followers': 'https://api.unsplash.com/users/isumaki/followers',
        'portfolio': 'https://api.unsplash.com/users/isumaki/portfolio',
        'html': 'http://unsplash.com/@isumaki',
        'self': 'https://api.unsplash.com/users/isumaki',
        'following': 'https://api.unsplash.com/users/isumaki/following'
        },
    'location': 'Höfen',
    'first_name': 'Raphael',
    'total_photos': 26,
    'profile_image': {
        'large': 'https://images.unsplash.com/profile-1459116744182-63b6987fad08?ixlib=rb-0.3.5&q=80&fm=jpg&crop=faces&cs=tinysrgb&fit=crop&h=128&w=128&s=4e2918921936646750ea43db54bedc7a',
        'medium': 'https://images.unsplash.com/profile-1459116744182-63b6987fad08?ixlib=rb-0.3.5&q=80&fm=jpg&crop=faces&cs=tinysrgb&fit=crop&h=64&w=64&s=85225703970385f82df3ffdb594aeb55',
        'small': 'https://images.unsplash.com/profile-1459116744182-63b6987fad08?ixlib=rb-0.3.5&q=80&fm=jpg&crop=faces&cs=tinysrgb&fit=crop&h=32&w=32&s=d27a379ca47ed5cd977caf7940736ef0'
        }
    },
    'exif': {
        'exposure_time': '0.016666666666666666',
        'focal_length': '28',
        'make': 'SONY',
        'iso': 125,
        'model': 'ILCE-7M2',
        'aperture': '4.970854'
        },
    'links': {
    'self': 'https://api.unsplash.com/photos/tTBWN0wpg94',
    'download': 'http://unsplash.com/photos/tTBWN0wpg94/download',
    'html': 'http://unsplash.com/photos/tTBWN0wpg94',
    'download_location': 'https://api.unsplash.com/photos/tTBWN0wpg94/download'
    },
'color': '#F4F8F1',
'id': 'tTBWN0wpg94',
'current_user_collections': [],
'downloads': 796,
'width': 6000,
'categories': [],
'liked_by_user': False,
'urls': {
    'thumb': 'https://images.unsplash.com/photo-1474924967440-18d9113d8bba?ixlib=rb-0.3.5&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=200&fit=max&s=30851e2b04381fad4b0fd2920cc1e59d',
    'raw': 'https://images.unsplash.com/photo-1474924967440-18d9113d8bba',
    'small': 'https://images.unsplash.com/photo-1474924967440-18d9113d8bba?ixlib=rb-0.3.5&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=400&fit=max&s=18ffde978bf739f79bcbb223b3ad13fb',
    'regular': 'https://images.unsplash.com/photo-1474924967440-18d9113d8bba?ixlib=rb-0.3.5&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&s=4f8a2aba7d07b4e4544a91c353774e09',
    'full': 'https://images.unsplash.com/photo-1474924967440-18d9113d8bba?ixlib=rb-0.3.5&q=80&fm=jpg&crop=entropy&cs=tinysrgb&s=b38a0e76e2af789a8847be6cc63aab76'
    },
'created_at': '2016-09-26T17:24:09-04:00',
'location': {
    'position': {
        'longitude': 7.56450708360592,
        'latitude': 46.7232919789662
        },
    'country':
    'Switzerland',
    'city': 'Höfen'
    }
}
"""
