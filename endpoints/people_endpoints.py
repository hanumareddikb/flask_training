from services.people_services import People, logging
from flask import Blueprint, request, jsonify, make_response
from models.people_model import PeopleModel

people_blueprint = Blueprint('people_blueprint', __name__)


class RegisterEndpoints(PeopleModel):

    @people_blueprint.app_errorhandler(404)
    def handle_404_error(error):
        return make_response(jsonify({'error': 'Not found'}), 404)

    @people_blueprint.route('/add_people', methods=['POST'])
    def add_people_request():
        logging.info("Entered in service...")

        try:
            people = request.get_json()

        except Exception as e:
            logging.error('Error in request: {}'.format(e))
            response = make_response(jsonify({"error": "Unexpected error"}), 500)
            return response

        # create a people object
        new_people = RegisterEndpoints()
        new_people.name = people['name']
        new_people.age = people['age']
        new_people.city = people['city']

        # add people to csv file
        try:
            People.add_people(new_people.name, new_people.age, new_people.city)
        except Exception as e:
            logging.error('Error adding people: {}'.format(e))
            response = make_response(jsonify({"error": "Error adding people"}), 500)
            return response

        return (new_people.to_dict()), 201, logging.info("Exited from service...")

    @people_blueprint.route('/list_people', methods=['GET'])
    def list_people_request():
        logging.info("Entered in service...")
        return (People.list_people()), 200, logging.info("Exited from service...")
