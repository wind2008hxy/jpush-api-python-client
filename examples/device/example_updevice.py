import jpush as jpush
from conf import app_key, master_secret
_jpush = jpush.JPush(app_key, master_secret)

device = _jpush.create_device()
reg_id = '1507bfd3f7c466c355c'
entity = jpush.device_tag(jpush.add("ddd", "tageee"))
#entity = jpush.device_tag("")
device.set_devicemobile(reg_id, entity)
