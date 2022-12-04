from requests import get
def GetUID():
    _AlfUid = []
    try:
        _ip = get('https://api.ipify.org').text

        for i in _ip:
            _AlfUid.append

        for x in _AlfUid:
            _AlfUid[x] = chr(_AlfUid[x])
        _Uid = _AlfUid
        return _Uid
    except:
        print('ERROR: Make shure you are connected to the internet')