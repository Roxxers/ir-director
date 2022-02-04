from flask import render_template, Flask, jsonify, request, abort
import irsdk

ir = irsdk.IRSDK()
app = Flask(__name__)


# this is our State class, with some helpful variables
class State:
    ir_connected = False
    last_car_setup_tick = -1


# here we check if we are connected to iracing
# so we can retrieve some data
def check_iracing():
    if state.ir_connected and not (ir.is_initialized and ir.is_connected):
        state.ir_connected = False
        ir.shutdown()
        print('irsdk disconnected')
    elif not state.ir_connected and ir.startup() and ir.is_connected:
        state.ir_connected = True
        print('irsdk connected')


state = State()

ir.startup()


@app.before_request
def before_request_func():
    if "api" in request.url:
        check_iracing()
        if not state.ir_connected:
            abort(503)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/api/changeview", methods=["POST"])
def change_camera():
    driver_num = request.form[
        "driver_number"] or 0  # CANT BE INT DUE TO PADDED 0 CONFLICT
    camera_group = int(request.form["camera_group"]) or 0
    ir.cam_switch_num(driver_num, camera_group)
    return "", 200


@app.route("/ack")
def heartbeat():
    check_iracing()
    if state.ir_connected:
        return jsonify({
            "message": "IRacing Simulator is running",
            "connected": True
        })
    else:
        return jsonify({
            "message": "IRacing Simulator is not running",
            "connected": False
        })


@app.route("/api/session/drivers")
def driver_info():

    drivers = ir["DriverInfo"]["Drivers"]
    drivers_filtered = []
    for driver in drivers:
        driver_filtered = {}
        driver_filtered["CarClassColor"] = driver["CarClassColor"]
        driver_filtered["CarIdx"] = driver["CarIdx"]
        driver_filtered["CarClassShortName"] = driver["CarClassShortName"]
        driver_filtered["CarClassID"] = driver["CarClassID"]
        driver_filtered["CarIsPaceCar"] = driver["CarIsPaceCar"]
        driver_filtered["CarNumber"] = driver["CarNumber"]
        driver_filtered["CarNumberDesignStr"] = driver["CarNumberDesignStr"]
        driver_filtered["CarNumberRaw"] = driver["CarNumberRaw"]
        driver_filtered["CarScreenNameShort"] = driver["CarScreenNameShort"]
        driver_filtered["IRating"] = driver["IRating"]
        driver_filtered["LicColor"] = driver["LicColor"]
        driver_filtered["LicString"] = driver["LicString"]
        driver_filtered["TeamID"] = driver["TeamID"]
        driver_filtered["TeamName"] = driver["TeamName"]
        driver_filtered["UserID"] = driver["UserID"]
        driver_filtered["UserName"] = driver["UserName"]
        drivers_filtered.append(driver_filtered)
    return jsonify(drivers_filtered)

if __name__ == "__main__":
    app.run()