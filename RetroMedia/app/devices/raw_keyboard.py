import pywinusb.hid as hid

registered_devices = {}

def list_keyboards():

    devices = hid.HidDeviceFilter().get_devices()

    keyboards = []

    for d in devices:

        if d.vendor_name:

            keyboards.append({
                "name": d.product_name,
                "vendor": d.vendor_name,
                "id": d.device_path
            })

    return keyboards
