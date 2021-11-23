from flask import request, jsonify
from mib.dao.lottery_manager import LotteryManager
from mib.models.lottery import Lottery


def create_lottery_play():
    post_data = request.get_json()
    id = post_data.get('id')
    lottery_number = post_data.get('lottery_number')

    lottery_play = Lottery()

    lottery_play.id = id
    lottery_play.set_number(lottery_number)

    LotteryManager.create_lottery_play(lottery_play)

    response_object = {
        'lottery': lottery_play.serialize(),
        'status': 'success',
        'message': 'Successfully play',
    }

    return jsonify(response_object), 201

'''

def get_user(user_id):
    """
    Get a user by its current id.

    :param user_id: user it
    :return: json response
    """
    user = UserManager.retrieve_by_id(user_id)
    if user is None:
        response = {'status': 'User not present'}
        return jsonify(response), 404

    return jsonify(user.serialize()), 200


def get_user_by_email(user_email):
    """
    Get a user by its current email.

    :param user_email: user email
    :return: json response
    """
    user = UserManager.retrieve_by_email(user_email)
    if user is None:
        response = {'status': 'User not present'}
        return jsonify(response), 404

    return jsonify(user.serialize()), 200


def delete_user(user_id):
    """
    Delete the user with id = user_id.

    :param user_id the id of user to be deleted
    :return json response
    """
    UserManager.delete_user_by_id(user_id)
    response_object = {
        'status': 'success',
        'message': 'Successfully deleted',
    }

    return jsonify(response_object), 202
'''