"""
Main program for point of interest finder program.
"""

import flask
from flask import request
import config
import logging
import make_poi_list
import best_route

###
# Globals
###
app = flask.Flask(__name__)
CONFIG = config.configuration()
app.secret_key = CONFIG.SECRET_KEY
app.mapbox_key = CONFIG.MAPBOX_KEY
app.poi_list = CONFIG.POI_LIST
app.debug = CONFIG.DEBUG
if app.debug:
    app.logger.setLevel(logging.DEBUG)

full_poi_list = make_poi_list.make_list(app.poi_list)


###
# Pages
###
@app.route("/")
@app.route("/index")
def index():
    app.logger.debug("Main page entry")
    flask.g.mapbox_key = app.mapbox_key
    return flask.render_template('maps.html')


@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug("Page not found")
    flask.session['linkback'] = flask.url_for("index")
    return flask.render_template('404.html'), 404


###############
# AJAX request handlers
#   These return JSONs, rather than rendering pages.
###############
@app.route("/_poi")
def _poi():
    app.logger.debug("Got a JSON request")
    app.logger.debug("request.args: {}".format(request.args))
    max_dist = request.args.get('max_dist', type=float)
    lat = request.args.get('lat', type=float)
    long = request.args.get('long', type=float)
    type_of_pois = request.args.get('type_of_pois')
    cur_mode = request.args.get('cur_mode')

    # Filter the list of points of interest to only the poi types we want.
    filter_pois = make_poi_list.filter(full_poi_list, type_of_pois)
    # Crop the filtered list to a circle with radius max dist at our start location.
    crop_pois = make_poi_list.crop(filter_pois, lat, long, max_dist)
    if cur_mode == "disp":
        result = {"points": crop_pois}
        return flask.jsonify(result=result)
    else:
        # If cur mode is not disp, we need to calculate the best route:
        optimal = best_route.route(lat, long, max_dist, crop_pois)
        result = {"points": optimal}
        return flask.jsonify(result=result)


if __name__ == "__main__":
    print("Opening for global access on port {}".format(CONFIG.PORT))
    app.run(port=CONFIG.PORT, host="0.0.0.0")
